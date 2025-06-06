# 📊 Visualisation & API des clubs de Ligue 1 2024-2025

Ce projet a pour objectif de collecter, enrichir, visualiser et exposer les données des clubs de **Ligue 1 française** via :

- 🕷️ Scraping des données depuis Wikipédia
- 📍 Géolocalisation des stades (GeoPy)
- 🗺️ Carte interactive avec filtres dynamiques (capacités, régions)
- 📊 Graphiques statistiques avec Matplotlib
- 🌐 API REST avec Flask pour exposer les données en JSON

---

## 🛠️ Technologies utilisées

| Outil / Lib          | Rôle                                                                 |
|----------------------|----------------------------------------------------------------------|
| **Python 3.x**       | Langage principal                                                    |
| **Pipenv**           | Gestion de l’environnement et des dépendances                        |
| **Pandas**           | Traitement de données tabulaires                                     |
| **BeautifulSoup**    | Web scraping des données sur Wikipédia                               |
| **GeoPy**            | Géocodage des stades en latitude / longitude                         |
| **Folium**           | Carte interactive avec affichage des stades                          |
| **Matplotlib**       | Graphiques pour visualiser capacités & budgets                       |
| **Flask**            | API REST exposant les données en JSON                                |
| **Ipywidgets**       | Filtres interactifs dans le notebook (capacité, région)              |
| **Jupyter Notebook** | Interface interactive pour la visualisation                          |

---

## 📦 Installation (avec Pipenv)

### 1. Cloner le projet

```bash
git clone https://github.com/Timeo10/visualisation_ligue1.git
cd visualisation_ligue1
```

### 2. Installer les dépendances avec Pipenv

```bash
pipenv install
```

### 3. Activer l’environnement virtuel

```bash
pipenv shell
```

---

## ▶️ Étapes d'utilisation

### 1. Scraping et enrichissement des données

Lancer le script pour scraper Wikipédia, géocoder les stades et générer `clubs_ligue1_2024_2025.csv` :

```bash
python scraping_ligue1.py
```

Ce fichier contient : club, entraîneur, stade, capacité, coordonnées GPS, etc.

---

### 2. Lancer l'API Flask

```bash
python api.py
```

**Endpoints disponibles** :

- `GET /clubs` → toutes les données en JSON  




---

### 3. Visualisation dans Jupyter

```bash
pipenv run jupyter notebook
```

Ouvrir le fichier `stats.ipynb` pour :

- 🗺️ Carte interactive des stades (avec filtres par région et capacité)
- 📊 Graphique : capacité des stades
- 📋 Tableau trié des capacités


---

## ✅ Exemple d'API JSON

```json
{
  "Club": "Paris Saint-Germain",
  "Stade": "Parc des Princes",
  "Capacité": 47929,
  "Latitude": 48.8414,
  "Longitude": 2.2530
}
```

---

