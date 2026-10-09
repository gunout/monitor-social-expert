#!/usr/bin/env python3
"""Patch index.html pour utiliser jsDelivr au lieu de GitHub Pages"""

from pathlib import Path

HTML_FILE = Path(__file__).parent / 'index.html'

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Vérifier si déjà patché
if 'cdn.jsdelivr.net' in html:
    print("ℹ️ Déjà patché pour jsDelivr")
    exit(0)

# 2. Ajouter la constante CDN au début de chargerFichiersAuto
old_start = """async function chargerFichiersAuto(){
  const manifestFile = 'manifest.json';"""

new_start = """async function chargerFichiersAuto(){
  // CDN jsDelivr (supporte Git LFS)
  const CDN = 'https://cdn.jsdelivr.net/gh/gunout/monitor-social-expert@main/';
  const manifestFile = 'manifest.json';"""

if old_start in html:
    html = html.replace(old_start, new_start)
    print("✅ Constante CDN ajoutée")
else:
    print("⚠️ Fonction chargerFichiersAuto non trouvée (format différent)")
    # Essayer une autre signature
    old_start2 = """async function chargerFichiersAuto(){
  const manifestFile = 'manifest.json';"""
    if old_start2 in html:
        html = html.replace(old_start2, new_start)
        print("✅ Constante CDN ajoutée (variante 2)")

# 3. Remplacer les fetch
html = html.replace(
    "const response = await fetch(manifestFile);",
    "const response = await fetch(CDN + manifestFile);"
)
html = html.replace(
    "const resp = await fetch(fichier);",
    "const resp = await fetch(CDN + fichier);"
)

# 4. Sauvegarder
with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print("✅ Patch appliqué")
print()
print("Vérifications :")
print(f"  - CDN : {'✅' if 'cdn.jsdelivr.net' in html else '❌'}")
print(f"  - fetch manifest : {'✅' if 'CDN + manifestFile' in html else '❌'}")
print(f"  - fetch fichier : {'✅' if 'CDN + fichier' in html else '❌'}")
