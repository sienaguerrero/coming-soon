import argparse
import html
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent / "page" / "index.html"


def render(title, message, back_url, back_label):
    if not back_url.startswith(("https://", "/")) or back_url.startswith("//"):
        raise SystemExit(f"back-url must be an https:// link or a same-site path like /, got {back_url!r}")
    page = TEMPLATE.read_text()
    for token, value in {
        "__TITLE__": title,
        "__MESSAGE__": message,
        "__BACK_URL__": back_url,
        "__BACK_LABEL__": back_label,
    }.items():
        page = page.replace(token, html.escape(value, quote=True))
    return page


def main():
    p = argparse.ArgumentParser(description="Write the Under construction page to a folder.")
    p.add_argument("--out", required=True)
    p.add_argument("--title", default="Under construction")
    p.add_argument("--message", default="This page is getting a fresh coat of paint. Check back soon.")
    p.add_argument("--back-url", default="https://siena.codes")
    p.add_argument("--back-label", default="back to siena.codes")
    a = p.parse_args()
    page = render(a.title, a.message, a.back_url, a.back_label)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "404.html"):
        (out / name).write_text(page)


if __name__ == "__main__":
    main()
