# dashboard-rh-powerbi
Analyse RH interactive sur 5 000 employés — Python, PostgreSQL, Power BI
# Dashboard RH — Analyse turnover & performance

Projet perso pour pratiquer Python et Power BI sur un cas RH concret.
J'ai généré un dataset fictif de 5 000 employés et construit une analyse complète.

## Ce que j'ai fait

- Génération et nettoyage des données avec pandas
- Exploration : turnover par département, absentéisme, scores de perf
- Modélisation d'un schéma SQL pour structurer les données
- Dashboard Power BI pour visualiser les KPIs RH

## Stack

Python (pandas, numpy, matplotlib, seaborn) · PostgreSQL · Power BI

## Ce que j'ai trouvé

Le taux de turnover global est de 16,5%. Ce qui m'a surpris c'est la corrélation entre les scores de performance bas et les départs — les employés avec un score < 3/10 ont 3x plus de chance de quitter l'entreprise dans les 6 mois. Support client département avec le plus d'absence.
