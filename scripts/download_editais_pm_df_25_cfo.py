from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

API_URL = "https://apis.cebraspe.org.br/cebraspe/eventos/pm_df_25_cfo"
CDN_BASE = "https://cdn.cebraspe.org.br/concursos/pm_df_25_cfo/arquivos"
DEST_DIR = Path("/Users/gabrielramos/CFOPMDF/EDITAIS")
MANIFEST = DEST_DIR / "PM_DF_25_CFO_manifest.json"
SLUG_MAX = 140


def slugify(text: str) -> str:
    text = text.lower().replace("nº", "n").replace("n°", "n")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "arquivo"


def get_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_pdf(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=120) as resp:
        body = resp.read()
        ctype = (resp.headers.get("Content-Type") or "").lower()
    if not body:
        raise ValueError("arquivo vazio")
    if b"%PDF-" not in body[:16] and "pdf" not in ctype:
        raise ValueError(f"conteudo nao parece PDF (content-type={ctype})")
    return body


def build_local_name(date_iso: str, descricao: str, used: set[str]) -> str:
    day = date_iso[:10] if date_iso else "sem-data"
    slug = slugify(descricao)[:SLUG_MAX].strip("-") or "arquivo"
    base = f"{day}_{slug}"
    name = f"{base}.pdf"
    i = 2
    while name in used:
        name = f"{base}-{i}.pdf"
        i += 1
    used.add(name)
    return name


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    data = get_json(API_URL)
    arquivos = sorted(data.get("arquivosEdital", []), key=lambda x: x.get("dataArquivoObj", ""))

    used_names: set[str] = set()
    records: list[dict] = []
    ok = 0
    fail = 0

    for item in arquivos:
        nome = str(item.get("nomeArquivo", "")).strip()
        desc = str(item.get("descricaoArquivo", "")).strip() or nome
        date_iso = str(item.get("dataArquivoObj", "")).strip()
        url = f"{CDN_BASE}/{quote(nome)}"
        local_name = build_local_name(date_iso, desc, used_names)
        local_path = DEST_DIR / local_name
        part_path = DEST_DIR / f".{local_name}.part"

        try:
            payload = download_pdf(url)
            part_path.write_bytes(payload)
            part_path.replace(local_path)
            rec = {
                "status": "ok",
                "dataArquivoObj": date_iso,
                "dataArquivo": item.get("dataArquivo"),
                "descricaoArquivo": desc,
                "nomeArquivo": nome,
                "url_cdn": url,
                "arquivo_local": local_name,
                "bytes": len(payload),
                "sha256": sha256_hex(payload),
            }
            records.append(rec)
            ok += 1
        except Exception as exc:
            if part_path.exists():
                part_path.unlink(missing_ok=True)
            rec = {
                "status": "erro",
                "dataArquivoObj": date_iso,
                "dataArquivo": item.get("dataArquivo"),
                "descricaoArquivo": desc,
                "nomeArquivo": nome,
                "url_cdn": url,
                "arquivo_local": local_name,
                "erro": str(exc),
            }
            records.append(rec)
            fail += 1

    manifest = {
        "concurso": "pm_df_25_cfo",
        "api_url": API_URL,
        "total_api": len(arquivos),
        "baixados_ok": ok,
        "falhas": fail,
        "itens": records,
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"total_api={len(arquivos)}")
    print(f"baixados_ok={ok}")
    print(f"falhas={fail}")
    print(f"manifest={MANIFEST}")
    return 0 if fail == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
