# ToolingQA 360 — Démonstrateur de recette logicielle

Projet portfolio **indépendant et fictif**, réalisé pour illustrer une démarche de test logiciel dans un contexte inspiré de la gestion d'outillages aéronautiques. **Aucune affiliation à Dedienne Aerospace / ToolLive.** Aucun accès ni utilisation de leurs données ou logiciels.

## Fonctionnalités
- Inventaire d'outillages fictifs et recherche
- Création avec contrôles de cohérence
- Affectation et retour selon les règles métier
- Tableau de bord des statuts
- 40 cas de recette manuelle (`docs/cahier_recette_40_cas.csv`)
- 8 exemples de tickets (`docs/registre_anomalies_exemples.csv`)
- 11 tests unitaires Python (`tests/test_qa_core.py`)
- Workflow CI GitHub Actions
- Stratégie de tests et de non-régression

## Installation
```bash
python -m venv .venv
# Windows : .venv\Scripts\activate
# macOS/Linux : source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Tests
```bash
python -m pytest -q
```

## Déploiement Streamlit Community Cloud
1. Créer un dépôt GitHub et y déposer **le contenu de ce dossier**.
2. Dans Streamlit Community Cloud, créer une application à partir de ce dépôt.
3. Fichier principal : `app.py`.
4. Tester le lien public, les opérations et l'affichage avant de le transmettre.

## Notes
Les données restent en mémoire de session ; elles ne sont pas persistantes. Les cas manuels n'ont pas été exécutés par défaut. Le registre d'anomalies est pédagogique et ne constitue pas un relevé de bugs constatés. Ne pas annoncer de couverture, de performance ou de taux de réussite non mesuré.
