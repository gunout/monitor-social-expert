# 🏛️ Monitor Social Expert+

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made in France](https://img.shields.io/badge/Made%20in-France-000091?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5IDYiPjxyZWN0IHdpZHRoPSIzIiBoZWlnaHQ9IjYiIGZpbGw9IiMwMDAwOTEiLz48cmVjdCB4PSIzIiB3aWR0aD0iMyIgaGVpZ2h0PSI2IiBmaWxsPSIjZmZmIi8+PHJlY3QgeD0iNiIgd2lkdGg9IjMiIGhlaWdodD0iNiIgZmlsbD0iI0UxMDAwRiIvPjwvc3ZnPg==)](https://github.com/gunout/monitor-social-expert)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?logo=chart.js&logoColor=white)](https://www.chartjs.org/)
[![Open Data](https://img.shields.io/badge/Open%20Data-data.caf.fr-blue)](https://data.caf.fr)
[![La Réunion](https://img.shields.io/badge/974-La%20Réunion-00A3E0)](https://www.departement974.fr)
[![CAF](https://img.shields.io/badge/CAF-CNAF-003DA5)](https://www.caf.fr)
[![MDPH](https://img.shields.io/badge/MDPH-Handicap-7C3AED)](https://www.mdph.fr)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Version](https://img.shields.io/badge/version-5.3-blue)](https://github.com/gunout/monitor-social-expert/releases)

> **Tableau de bord analytique complet pour les politiques sociales de La Réunion** — MDPH · CAF · Département · Région

Un outil **100% client-side** (aucun serveur, aucune base de données) qui transforme les données brutes Open Data de la CNAF en **tableau de bord interactif** avec 20 vues analytiques, projections, détection d'anomalies et rapports officiels.

---

## ✨ Fonctionnalités

### 📊 20 vues analytiques

| Vue | Description |
|---|---|
| 📊 **Vue d'ensemble** | Synthèse globale, répartition par thème |
| 🎯 **Scénario actif** | 7 scénarios experts pré-configurés |
| 🗂️ **Datasets** | Inventaire complet des datasets générés |
| 💶 **Prestations** | Tableau de synthèse AAH · RSA · PPA · AF · CF · ARS · ASF… |
| 📈 **Évolution** | Courbes temporelles 2016-2026 |
| 📆 **Mensuel** | Moyennes mensuelles et saisonnalité |
| 🔮 **Projections** | Modèle linéaire avec IC 95% et R² |
| 🚨 **Anomalies** | Détection Z-score (> 2.5σ) |
| 🔗 **Corrélations** | Matrice de Pearson / Spearman |
| 📅 **Timeline** | Chronologie des publications |
| 🔲 **Matrice** | Croisement années × thèmes |
| 📊 **Statistiques** | Moyenne, médiane, écart-type, skewness |
| 📐 **Indicateurs** | 12 indicateurs sociaux documentés |
| 🏝️ **Micro-régions** | Nord / Sud / Est / Ouest |
| 🗺️ **Géographie** | 12 communes principales |
| ⚖️ **Comparaison** | Multi-séries |
| 🏆 **Benchmark DOM** | Réunion vs Guadeloupe, Martinique… |
| 🧪 **Simulateur** | Impact de politiques sociales |
| ⚠️ **Avertissements** | Incertitudes documentées |
| 🏛️ **Rapport officiel** | Template MDPH/CAF/Département/Région |
| 📋 **Audit** | Traçabilité complète des calculs |

### 🔬 Moteur statistique intégré

- **Statistiques descriptives** : moyenne, médiane, écart-type, quartiles, skewness, kurtosis
- **Corrélations** : Pearson et Spearman
- **Régression linéaire** : pente, R², intervalles de confiance à 95%
- **Détection d'anomalies** : Z-scores, outliers (|Z| > 2.5)
- **Projections** : modèle linéaire sur 3 ans
- **Indice de Gini** : mesure d'inégalité territoriale

### 📁 Agrégation intelligente

- **Détection automatique** du format CAF (lignes brutes)
- **Agrégation par dimensions** : complément, âge, taux d'incapacité
- **Multi-prestations** : AAH, RSA, PPA, AF, CF, ARS, ASF, AEEH, PAJE, APL…
- **Filtrage 974** : La Réunion uniquement (bouton toggle)
- **Déduplication par ID** : fusion multi-fichiers

### 📥 Exports

| Format | Usage |
|---|---|
| 📥 **CSV** | Analyse Excel / LibreOffice |
| 📥 **JSON** | Intégration dans d'autres outils |
| 📥 **Rapport HTML** | Documentation interne |
| 🏛️ **Rapport officiel** | Transmission MDPH / CAF / Département |
| 📋 **Audit** | Traçabilité réglementaire |

---

## 🚀 Installation

### Prérequis

- **Navigateur moderne** : Firefox 90+, Chrome 90+, Edge 90+, Safari 14+
- **Python 3** (recommandé, pour le serveur local) — *ou tout autre serveur HTTP*

### Option 1 : Cloner le dépôt (recommandé)

```bash
# 1. Cloner le dépôt
git clone https://github.com/gunout/monitor-social-expert.git

# 2. Entrer dans le dossier
cd monitor-social-expert

# 3. Lancer le serveur local
python3 -m http.server 8000
```

Puis ouvrir dans le navigateur : **http://localhost:8000/index.html**

### Option 2 : Télécharger le ZIP

```bash
# 1. Télécharger le ZIP depuis GitHub
# https://github.com/gunout/monitor-social-expert/archive/refs/heads/main.zip

# 2. Extraire
unzip monitor-social-expert-main.zip
cd monitor-social-expert-main

# 3. Lancer le serveur
python3 -m http.server 8000
```

### Option 3 : Utiliser un autre serveur HTTP

```bash
# Avec Node.js (npx)
npx serve .

# Avec PHP
php -S localhost:8000

# Avec Ruby
ruby -run -e httpd . -p 8000
```

### Option 4 : Ouvrir directement (limité)

Vous pouvez ouvrir `index.html` directement dans le navigateur, mais **certaines fonctionnalités seront limitées** (lecture de fichiers locaux restreinte).

---

## 📦 Téléchargement des données

Le monitor fonctionne avec les fichiers JSON de **data.caf.fr**. Voici les 4 fichiers recommandés pour La Réunion :

### 1️⃣ AAH — Répartition par complément et âge (départemental)

```bash
curl -s "https://data.caf.fr/api/explore/v2.1/catalog/datasets/aah_s_complaah_age_5_dep/exports/json?limit=-1" \
  -o data/aah_s_complaah_age_5_dep.json
```

### 2️⃣ AAH — Répartition par taux d'incapacité (national)

```bash
curl -s "https://data.caf.fr/api/explore/v2.1/catalog/datasets/aah_s_tx_inca_age_1_nat/exports/json?limit=-1" \
  -o data/aah_s_tx_inca_age_1_nat.json
```

### 3️⃣ AAH — Répartition par taux d'incapacité (départemental)

```bash
curl -s "https://data.caf.fr/api/explore/v2.1/catalog/datasets/aah_s_tx_inca_dep/exports/json?limit=-1" \
  -o data/aah_s_tx_inca_dep.json
```

### 4️⃣ Bénéficiaires CAF — Toutes prestations (974 uniquement)

```bash
curl -s "https://data.caf.fr/api/explore/v2.1/catalog/datasets/s_ben_dep/exports/json?where=numdep%3D%22974%22&limit=-1" \
  -o data/s_ben_dep_974.json
```

### Script complet

```bash
#!/bin/bash
# Télécharger les 4 fichiers
mkdir -p data && cd data

curl -s "https://data.caf.fr/api/explore/v2.1/catalog/datasets/aah_s_complaah_age_5_dep/exports/json?limit=-1" -o aah_s_complaah_age_5_dep.json
curl -s "https://data.caf.fr/api/explore/v2.1/catalog/datasets/aah_s_tx_inca_age_1_nat/exports/json?limit=-1" -o aah_s_tx_inca_age_1_nat.json
curl -s "https://data.caf.fr/api/explore/v2.1/catalog/datasets/aah_s_tx_inca_dep/exports/json?limit=-1" -o aah_s_tx_inca_dep.json
curl -s "https://data.caf.fr/api/explore/v2.1/catalog/datasets/s_ben_dep/exports/json?where=numdep%3D%22974%22&limit=-1" -o s_ben_dep_974.json

ls -lh
```

---

## 🎯 Utilisation

### 1. Ouvrir le monitor

```
http://localhost:8000/index.html
```

### 2. Charger les fichiers JSON

**Glissez-déposez** les 4 fichiers JSON sur la zone en bas à gauche de la sidebar, ou **cliquez** pour les sélectionner.

### 3. Explorer les données

Naviguez dans les **20 onglets** :

- 📊 **Vue d'ensemble** : synthèse globale
- 💶 **Prestations** : AAH, RSA, PPA, AF…
- 📈 **Évolution** : courbes 2016-2026
- 🔮 **Projections** : prévisions 2027-2028
- 🚨 **Anomalies** : points atypiques (COVID, etc.)

### 4. Filtrer sur La Réunion

Le bouton **🇷🇪 974 uniquement** est actif par défaut. Cliquez pour basculer sur **🌍 France entière**.

### 5. Exporter

Utilisez les boutons en bas : **CSV**, **JSON**, **Rapport HTML**, **Rapport officiel**.

---

## 🏗️ Architecture

```
monitor-social-expert/
├── index.html              # Application complète (HTML + CSS + JS)
├── README.md               # Ce fichier
├── LICENSE                 # Licence MIT
├── data/                   # Fichiers JSON (à télécharger)
│   ├── aah_s_complaah_age_5_dep.json
│   ├── aah_s_tx_inca_age_1_nat.json
│   ├── aah_s_tx_inca_dep.json
│   └── s_ben_dep_974.json
└── screenshots/            # Captures d'écran
    ├── dashboard.png
    ├── prestations.png
    ├── evolution.png
    └── projections.png
```

### Stack technique

| Composant | Technologie |
|---|---|
| **UI** | HTML5 + CSS3 (Grid, Flexbox) |
| **Logique** | JavaScript vanilla (ES6+) |
| **Graphiques** | SVG natif (aucune dépendance) |
| **Design** | Charte graphique de l'État français |
| **Données** | Open Data CNAF (data.caf.fr) |

**Aucune dépendance externe** : pas de npm, pas de CDN, pas de framework. **100% autonome**.

---

## 📊 Données analysées

### Sources Open Data

| Dataset | Source | Lignes | Description |
|---|---|---|---|
| `aah_s_complaah_age_5_dep` | CNAF | 281 054 | AAH par complément × âge × département |
| `aah_s_tx_inca_age_1_nat` | CNAF | 19 354 | AAH par taux d'incapacité (national) |
| `aah_s_tx_inca_dep` | CNAF | 35 581 | AAH par taux d'incapacité (départemental) |
| `s_ben_dep` | CNAF | 12 499 | Bénéficiaires toutes prestations |

**Total** : **348 488 lignes brutes** → **82 datasets analytiques**

### Prestations couvertes

- **AAH** : Allocation aux Adultes Handicapés
- **RSA** : Revenu de Solidarité Active
- **PPA** : Prime d'activité
- **AF** : Allocations familiales
- **CF** : Complément familial
- **ARS** : Allocation de rentrée scolaire
- **ASF** : Allocation de soutien familial
- **AEEH** : Allocation d'éducation de l'enfant handicapé
- **PAJE** : Prestation d'accueil du jeune enfant
- **APL / ALS / ALF** : Aides au logement
- **Et plus…**

### Période couverte

**2016-06 → 2026-03** (10 ans de données mensuelles)

---

## 🎨 Charte graphique

Le monitor respecte la **charte de l'État français** :

| Couleur | Code | Usage |
|---|---|---|
| 🔵 Bleu France | `#000091` | Couleur principale |
| ⚪ Blanc | `#FFFFFF` | Fond |
| 🔴 Rouge Marianne | `#E1000F` | Accents |
| 🟡 Or | `#FBBF24` | Mises en avant |
| 🟢 Vert | `#16A34A` | Succès |
| 🟣 Violet | `#7C3AED` | Expert |

**Typographie** : Marianne (système), SF Mono (code)

---

## 📈 Exemples de résultats

### AAH La Réunion (2016-2026)

| Indicateur | 2016-06 | 2026-03 | Évolution |
|---|---|---|---|
| Foyers allocataires | 17 800 | 22 683 | **+27.4%** |
| Personnes couvertes | 26 943 | 33 478 | **+24.3%** |
| Montant mensuel | 12 985 569 € | 21 124 992 € | **+62.7%** |

### Répartition par âge (2026-03)

| Tranche d'âge | Foyers |
|---|---|
| Moins de 20 ans | ~20 |
| Entre 20 et 24 ans | ~1 300 |
| Entre 25 et 29 ans | ~1 500 |
| Entre 30 et 34 ans | ~1 650 |
| Entre 35 et 39 ans | ~1 660 |
| Entre 40 et 44 ans | ~1 990 |
| Entre 45 et 49 ans | ~2 010 |
| Entre 50 et 54 ans | ~2 570 |
| Entre 55 et 59 ans | ~3 260 |
| Entre 60 et 64 ans | ~2 290 |
| 65 ans ou plus | ~1 480 |

**Profil type** : les 55-59 ans sont la tranche la plus représentée.

---

## 🤝 Contribution

Les contributions sont **les bienvenues** !

### Signaler un bug

Ouvrez une [issue](https://github.com/gunout/monitor-social-expert/issues) avec :
- Le comportement observé
- Le comportement attendu
- Les étapes de reproduction
- Le navigateur et la version

### Proposer une amélioration

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/amelioration`)
3. Committez (`git commit -m 'Ajout de...'`)
4. Poussez (`git push origin feature/amelioration`)
5. Ouvrez une Pull Request

---
## BONUS - MISE A JOUR ( 2026-2027 ) *

## 🎯 Pour ajouter les prochaines années

Quand vous aurez les données 2026-2027 :
```bash

cd ~/monitor-social-expert

# 1. Télécharger les nouvelles données
curl -sL "https://data.caf.fr/api/explore/v2.1/catalog/datasets/aah_s_complaah_age_5_dep/exports/json?limit=-1" -o /tmp/aah_full.json
jq '[.[] | select(.numdep == "974")]' /tmp/aah_full.json > aah_s_complaah_age_5_dep_974.json
rm /tmp/aah_full.json
```
# 2. Commit + push
```bash
git add aah_s_complaah_age_5_dep_974.json
git commit -m "data: update AAH 2026"
git push

echo "✅ Données mises à jour"
```
Le monitor chargera automatiquement les nouvelles données.

---

## 📜 Licence

**MIT License** — Voir [LICENSE](LICENSE)

```
Copyright (c) 2026 gunout

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

### Licence des données

Les données utilisées proviennent de **data.caf.fr** et sont publiées sous :
- **Licence Ouverte v2.0 (Etalab)**
- **Usage libre** avec mention de la source

---

## 🙏 Remerciements

- **CNAF** (Caisse Nationale des Allocations Familiales) — pour l'Open Data
- **Département de La Réunion** — pour le contexte territorial
- **MDPH de La Réunion** — pour la collaboration
- **La communauté Open Data française** — pour les outils

---

## 📞 Contact

- **GitHub** : [@gunout](https://github.com/gunout)
- **Issues** : [github.com/gunout/monitor-social-expert/issues](https://github.com/gunout/monitor-social-expert/issues)

---

## 🔗 Liens utiles

| Ressource | URL |
|---|---|
| 📊 Open Data CNAF | [data.caf.fr](https://data.caf.fr) |
| 📊 Open Data France | [data.gouv.fr](https://www.data.gouv.fr) |
| 📊 Open Data Europe | [data.europa.eu](https://data.europa.eu) |
| 🏛️ Département La Réunion | [departement974.fr](https://www.departement974.fr) |
| 🏛️ MDPH La Réunion | [mdph.fr](https://www.mdph.fr) |
| 🏛️ CAF La Réunion | [caf.fr](https://www.caf.fr) |

---

<div align="center">

**🏛️ Monitor Social Expert+**

*Tableau de bord analytique pour les politiques sociales de La Réunion*

[![GitHub stars](https://img.shields.io/github/stars/gunout/monitor-social-expert?style=social)](https://github.com/gunout/monitor-social-expert/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/gunout/monitor-social-expert?style=social)](https://github.com/gunout/monitor-social-expert/network/members)
[![GitHub issues](https://img.shields.io/github/issues/gunout/monitor-social-expert)](https://github.com/gunout/monitor-social-expert/issues)

**Fait avec ❤️ à La Réunion 🇷🇪**

</div>

---

<div align="center">

### 🇫🇷 Gunout · 2026

![Made in France](https://img.shields.io/badge/Made_in-France-002395?style=flat-square&labelColor=FFFFFF&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MDAgNjAwIj48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjYwMCIgZmlsbD0iIzAwMjM5NSIvPjxyZWN0IHdpZHRoPSI5MDAiIGhlaWdodD0iNDAwIiB5PSIxMDAiIGZpbGw9IiNmZmYiLz48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjIwMCIgeT0iNDAwIiBmaWxsPSIjZWQyOTM5Ii8+PC9zdmc+)
![GitHub](https://img.shields.io/badge/GitHub-gunout-181717?style=flat-square&logo=github&logoColor=white)
![Year](https://img.shields.io/badge/2026-ED2939?style=flat-square&labelColor=FFFFFF)

<sub>© 2026 <strong>Gunout</strong> — Tous droits réservés.</sub>

</div>
