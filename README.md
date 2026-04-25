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

# Dashboard RH — Analyse turnover & performance

Projet perso pour pratiquer Python et Power BI sur un cas RH concret.
Dataset fictif de 5 000 employés généré avec des distributions réalistes.

## Ce que j'ai fait

- Génération et nettoyage des données avec pandas
- Exploration : turnover par département, absentéisme, scores de performance
- Modélisation d'un schéma SQL pour structurer les données
- Dashboard Power BI pour visualiser les KPIs RH

## Stack

Python (pandas, numpy, matplotlib, seaborn) · PostgreSQL · Power BI

## Ce que j'ai trouvé 

Sans analyse, un DRH regarderait juste le taux de turnover global (16,5%) 
et conclurait que "ça va à peu près". 

L'analyse révèle ce que l'oeil nu ne voit pas :
le turnover n'est pas homogène — le département RH atteint 18,9% 
alors que Operations est à 15,7%. Sans segmentation par département, 
cette disparité reste invisible et les actions correctives sont mal ciblées.

Plus important : les employés avec un score de performance < 3 
partent 3,9x plus souvent que les bons performers. 
Ce chiffre permet de prioriser les entretiens de rétention 
sur les profils à risque avant qu'ils ne partent 
plutôt que de subir le turnover sans l'anticiper.
