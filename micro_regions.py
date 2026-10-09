# micro_regions.py
import json

# Mapping officiel des micro-régions de La Réunion
# Source : INSEE / Préfecture de La Réunion
MICRO_REGIONS = {
    # Nord
    '97411': 'Nord',    # Saint-Denis
    '97418': 'Nord',    # Sainte-Marie
    '97420': 'Nord',    # Sainte-Suzanne
    # Ouest
    '97407': 'Ouest',   # Le Port
    '97408': 'Ouest',   # La Possession
    '97413': 'Ouest',   # Saint-Leu
    '97415': 'Ouest',   # Saint-Paul
    '97423': 'Ouest',   # Les Trois-Bassins
    # Est
    '97402': 'Est',     # Bras-Panon
    '97406': 'Est',     # La Plaine-des-Palmistes
    '97409': 'Est',     # Saint-André
    '97410': 'Est',     # Saint-Benoît
    '97419': 'Est',     # Sainte-Rose
    '97421': 'Est',     # Salazie
    # Sud
    '97401': 'Sud',     # Les Avirons
    '97403': 'Sud',     # Entre-Deux
    '97404': 'Sud',     # L'Étang-Salé
    '97405': 'Sud',     # Petite-Île
    '97412': 'Sud',     # Saint-Joseph
    '97414': 'Sud',     # Saint-Louis
    '97416': 'Sud',     # Saint-Pierre
    '97417': 'Sud',     # Saint-Philippe
    '97422': 'Sud',     # Le Tampon
    '97424': 'Sud',     # Cilaos
}

# Charger les communes INSEE
with open('communes_974.json', 'r', encoding='utf-8') as f:
    communes = json.load(f)

# Ajouter les micro-régions
for c in communes:
    c['mr'] = MICRO_REGIONS.get(c['code'], 'Inconnu')

# Sauvegarder
with open('communes_974.json', 'w', encoding='utf-8') as f:
    json.dump(communes, f, indent=2, ensure_ascii=False)

print(f"✅ {len(communes)} communes enrichies avec micro-régions")