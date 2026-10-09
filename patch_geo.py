#!/usr/bin/env python3
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
HTML_FILE = SCRIPT_DIR / 'index.html'

if not HTML_FILE.exists():
    print(f"❌ Fichier introuvable : {HTML_FILE}")
    exit(1)

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'const COMMUNES_974 = \{[^}]+\};',
    'let COMMUNES_974 = [];  // Chargé depuis communes_974.json',
    html, count=1, flags=re.DOTALL
)

new_compute = '''async function computeMicroRegions(){
  try {
    const resp = await fetch('communes_974.json');
    if (!resp.ok) throw new Error('communes_974.json introuvable');
    COMMUNES_974 = await resp.json();
    state.microRegions = {Nord:[], Sud:[], Est:[], Ouest:[]};
    for (const c of COMMUNES_974){
      if (c.mr && state.microRegions[c.mr]) state.microRegions[c.mr].push(c);
    }
    console.log(`✅ ${COMMUNES_974.length} communes chargées`);
  } catch (err){
    console.warn('⚠️ communes_974.json non chargé :', err.message);
    COMMUNES_974 = [];
    state.microRegions = {};
  }
}'''

html = re.sub(r'function computeMicroRegions\(\)\{[\s\S]*?\n\}', new_compute, html, count=1)
html = html.replace('computeMicroRegions();', 'await computeMicroRegions();')

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Patch appliqué !")
