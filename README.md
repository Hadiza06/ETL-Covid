# ETL COVID-19 — Automatisation & Visualisation Power BI

## Description

Ce projet automatise la collecte, la transformation et le chargement de données COVID-19 en temps réel via l'API publique [disease.sh](https://disease.sh). Les données sont ensuite visualisées dans un dashboard Power BI.

---

## Stack technique

- **Python 3.12**
- **Pandas** — manipulation des données
- **Requests** — appel API
- **Logging** — traçabilité des exécutions
- **Task Scheduler (Windows)** — automatisation quotidienne
- **Power BI Desktop** — visualisation

---

## Architecture du projet

```
Automatisation/
│
├── run.py              # Script ETL principal
├── etl_covid.log       # Fichier de logs
└── covid_YYYY-MM-DD_HH-MM-SS.csv  # Fichiers de sortie horodatés
```

---

## Fonctionnement

### Extract
Appel à l'API publique disease.sh pour récupérer les données COVID-19 en temps réel pour 231 pays :
```
GET https://disease.sh/v3/covid-19/countries
```

### Transform
- Sélection des colonnes utiles : `country`, `cases`, `deaths`, `recovered`, `active`, `critical`, `population`, `casesPerOneMillion`, `deathsPerOneMillion`
- Calcul des indicateurs dérivés :
  - **Taux de mortalité** = (deaths / cases) × 100
  - **Taux de guérison** = (recovered / cases) × 100

### Load
- Sauvegarde en CSV avec horodatage automatique
- Exemple : `covid_2026-06-28_17-00-00.csv`

---

## Automatisation

Le script est planifié via **Windows Task Scheduler** pour s'exécuter tous les jours à 17h00, garantissant des données toujours à jour pour le dashboard Power BI.

---

## Dashboard Power BI

Le dashboard inclut les visualisations suivantes :
- **Cartes KPI** — Total mondial des cas, décès, guérisons, cas actifs
- **Histogramme** — Top 10 pays par nombre de cas
- **Graphique à barres** — Taux de mortalité par pays
- **Carte mondiale** — Répartition géographique des cas

---

## Logs

Chaque exécution est tracée dans `etl_covid.log` :
```
2026-06-28 17:00:00 [INFO] Début du script ETL
2026-06-28 17:00:01 [INFO] API appelée avec succès
2026-06-28 17:00:02 [INFO] CSV sauvegardé : covid_2026-06-28_17-00-00.csv - 231 lignes
```

---

## Lancement manuel

```bash
python run.py
```

---

## Source des données

- **API** : [disease.sh](https://disease.sh)
- **Endpoint** : `/v3/covid-19/countries`
- **Mise à jour** : temps réel (source mise à jour automatiquement)
