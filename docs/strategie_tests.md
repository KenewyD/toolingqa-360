# Stratégie de test — ToolingQA 360

## Contexte et limites
Projet personnel, indépendant, reposant sur une application et des données fictives. Il ne représente ni ToolLive ni ses systèmes réels.

## Risques prioritaires
1. Affecter un outillage indisponible.
2. Créer des références en doublon.
3. Perdre l'historique de statut ou afficher des indicateurs erronés.
4. Accepter des informations obligatoires manquantes.

## Types de tests
- Fonctionnels manuels : 40 scénarios dans `cahier_recette_40_cas.csv`.
- Unitaires automatisés : règles métier avec `pytest`.
- Non-régression : réexécuter création, affectation, retour, recherche et indicateurs après toute modification.
- Tests négatifs : champs vides, doublons, transitions interdites.

## Procédure de ticket
Titre précis ; environnement ; préconditions ; étapes reproductibles ; attendu ; observé ; sévérité ; capture ; version ; statut ; contre-test après correction.

## Critères de sortie proposés
Aucune anomalie bloquante ou critique ouverte ; tous les tests prioritaires exécutés ; preuves de tests et anomalies documentées ; risques résiduels validés.

## Transparence
Le registre fourni contient des **exemples de tickets**, non des défauts avérés. Les 40 cas sont **à exécuter** : aucun taux de réussite n'est revendiqué sans preuve.
