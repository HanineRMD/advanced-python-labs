# 🧩 TP Pydantic – Validation et Sérialisation de Données en Python

---

## 🎯 Objectif du TP

Ce TP a pour but de comprendre et d’utiliser la bibliothèque **Pydantic** pour :
- Contrôler les types de données en Python.
- Créer des modèles de données robustes.
- Valider les champs automatiquement.
- Sérialiser et désérialiser des objets JSON.
- Comparer **Pydantic** avec le module standard `dataclasses`.

---

## 🧱 Structure du projet

Pydantic/
│
├── main.py # Script principal (TP complet)
├── test.py # Comparaison Pydantic vs Dataclass
└── README.md # Ce fichier

## ⚙️ Installation et préparation

### 1️⃣ Créer un environnement virtuel
```bash
python -m venv venv

Activer l’environnement virtuel

Windows :

venv\Scripts\activate


Installer Pydantic
pip install pydantic[email]


Exécution 
python main.py
python test.py