#!/usr/bin/env python3
"""Ajoute le chargement automatique via jsDelivr"""

from pathlib import Path

HTML_FILE = Path(__file__).parent / 'index.html'

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# Vérifier si déjà présent
if 'chargerFichiersAuto' in html:
    print("ℹ️ Déjà présent")
    exit(0)

# Code à ajouter
auto_code = '''
<script>
// ============================================================
// CHARGEMENT AUTOMATIQUE VIA JSDELIVR (supporte Git LFS)
// ============================================================
async function chargerFichiersAuto(){
  const CDN = 'https://cdn.jsdelivr.net/gh/gunout/monitor-social-expert@main/';
  const manifestFile = 'manifest.json';
  
  console.log('🔄 Chargement automatique via jsDelivr...');
  const progress = document.getElementById('loadProgress');
  if (progress) progress.textContent = 'Lecture du manifeste…';

  try {
    const response = await fetch(CDN + manifestFile);
    if (!response.ok) throw new Error('manifest.json : HTTP ' + response.status);
    const manifest = await response.json();
    const fichiers = manifest.files || [];

    if (!fichiers.length){
      console.log('ℹ️ Manifeste vide');
      if (progress) progress.textContent = 'Manifeste vide';
      return;
    }

    console.log('📂 ' + fichiers.length + ' fichier(s) à charger');
    if (progress) progress.textContent = '0 / ' + fichiers.length;

    const loadedBruts = [];
    const fileReports = [];

    for (let i = 0; i < fichiers.length; i++){
      const fichier = fichiers[i];
      try {
        console.log('  ⏳ ' + fichier + '...');
        if (progress) progress.textContent = (i+1) + ' / ' + fichiers.length + ' · ' + fichier;
        
        const resp = await fetch(CDN + fichier);
        if (!resp.ok) throw new Error('HTTP ' + resp.status);
        const data = await resp.json();
        const bruts = extractBruts(data, fichier);
        loadedBruts.push(...bruts);
        fileReports.push({name:fichier, nbBrut:bruts.length, date:Date.now(), ok:true});
        console.log('  ✅ ' + fichier + ' : ' + bruts.length.toLocaleString('fr-FR') + ' lignes');
      } catch (err){
        console.error('  ❌ ' + fichier + ' : ' + err.message);
        fileReports.push({name:fichier, nbBrut:0, date:Date.now(), ok:false, error:err.message});
      }
    }

    if (!loadedBruts.length){
      console.warn('⚠️ Aucun fichier chargé');
      if (progress) progress.textContent = 'Aucun fichier';
      return;
    }

    if (progress) progress.textContent = 'Agrégation…';
    state.allDatasetsBruts = loadedBruts;
    state.allDatasets = aggregateAllCaf(loadedBruts);
    state.filteredDatasets = [...state.allDatasets];
    state.filesHistory = fileReports.filter(f => f.ok);
    state.source = state.filesHistory.length + ' fichiers (jsDelivr)';
    state.loadedAt = new Date();

    computeAll();
    
    // Mise à jour de l'UI
    if (typeof updateAllUI === 'function') {
      updateAllUI();
    } else {
      // Fallback si updateAllUI n'existe pas
      if (typeof updateStats === 'function') updateStats();
      if (typeof updateRightPanel === 'function') updateRightPanel();
      if (typeof renderRulesEngine === 'function') renderRulesEngine();
      if (typeof applyFilters === 'function') applyFilters();
      if (typeof renderScenarios === 'function') renderScenarios();
      if (typeof renderFilesLoaded === 'function') renderFilesLoaded();
      if (typeof renderAll === 'function') renderAll();
      
      const dot = document.getElementById('statusDot'); if (dot) dot.classList.remove('offline');
      const wb = document.getElementById('warningBanner'); if (wb) wb.hidden = false;
      ['exportCsv','exportJson','exportHtml','exportDce'].forEach(id => {
        const el = document.getElementById(id); if (el) el.disabled = false;
      });
      
      const setV = (id, v, cls) => {
        const el = document.getElementById(id);
        if (el) { el.textContent = v; if (cls) el.className = cls; }
      };
      setV('ivSource', state.source, 'v bleu');
      setV('ivStatus', '● CHARGÉ (jsDelivr)', 'v vert');
      setV('ivDate', state.loadedAt.toLocaleString('fr-FR'));
    }

    console.log('✅ ' + state.allDatasets.length + ' datasets · ' + Object.keys(state.seriesByTheme).length + ' séries');
    if (typeof toast === 'function') toast('✅ ' + state.allDatasets.length + ' datasets chargés', 'success', 4000);

  } catch (err){
    console.error('❌ Erreur chargement auto :', err.message);
    if (progress) progress.textContent = 'Erreur : ' + err.message;
    if (typeof toast === 'function') toast('⚠️ Chargement auto impossible · Glissez les fichiers', 'info', 5000);
  }
}

// Lancer après le chargement de la page
window.addEventListener('load', () => {
  setTimeout(chargerFichiersAuto, 1000);
});
</script>
'''

# Insérer avant </body>
if '</body>' in html:
    html = html.replace('</body>', auto_code + '\n</body>')
    print("✅ Code ajouté avant </body>")
else:
    html += auto_code
    print("✅ Code ajouté à la fin")

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print("Vérifications :")
print(f"  - chargerFichiersAuto : {'✅' if 'chargerFichiersAuto' in html else '❌'}")
print(f"  - CDN jsDelivr : {'✅' if 'cdn.jsdelivr.net' in html else '❌'}")
