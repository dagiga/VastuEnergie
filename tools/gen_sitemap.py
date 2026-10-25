#!/usr/bin/env python3
"""Regenere sitemap.xml a partir des pages du site.

- une entree par index.html (hors pages en noindex / Disallow)
- <lastmod> = date du dernier commit git ayant touche la page
  (donc la date d'une vraie modification de contenu, pas celle du deploiement)
- pas de <changefreq> ni de <priority> : Google les ignore depuis 2023,
  il ne lit que <lastmod>

Usage : python3 tools/gen_sitemap.py   (depuis la racine du site)
"""
import subprocess, pathlib, datetime, sys

BASE = "https://vastuenergie.be"
EXCLUS = {"mentions-legales", "politique-confidentialite"}

root = pathlib.Path(__file__).resolve().parent.parent

def git_date(path):
    try:
        d = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)],
                           cwd=root, capture_output=True, text=True).stdout.strip()
        return d or datetime.date.today().isoformat()
    except Exception:
        return datetime.date.today().isoformat()

entrees = []
for f in sorted(root.rglob("index.html")):
    rel = f.parent.relative_to(root)
    parts = rel.parts
    if parts and parts[0] in EXCLUS:
        continue
    loc = BASE + "/" if str(rel) == "." else f"{BASE}/{rel.as_posix()}/"
    entrees.append((loc, git_date(f.relative_to(root))))

# accueil d'abord, puis pages, puis articles de blog par date decroissante
def cle(e):
    loc = e[0]
    if loc == BASE + "/": return (0, "")
    if "/blog/" in loc and loc != f"{BASE}/blog/": return (2, "9999-99-99")
    return (1, loc)
pages = [e for e in entrees if cle(e)[0] < 2]
articles = sorted([e for e in entrees if cle(e)[0] == 2], key=lambda e: e[1], reverse=True)
entrees = sorted(pages, key=cle) + articles

xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', '']
for loc, d in entrees:
    xml += ['  <url>', f'    <loc>{loc}</loc>', f'    <lastmod>{d}</lastmod>', '  </url>', '']
xml.append('</urlset>')

(root / "sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")
print(f"sitemap.xml regenere : {len(entrees)} URL")
