import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/employes.csv')

print("=== Aperçu des données ===")
print(df.head())
print(f"\nShape : {df.shape}")
print(f"\nValeurs manquantes :\n{df.isnull().sum()}")

# ── Taux de turnover global
taux_turnover = df['a_quitte'].mean() * 100
print(f"\nTaux de turnover global : {taux_turnover:.1f}%")

# ── Turnover par département
turnover_dept = df.groupby('departement')['a_quitte'].mean().sort_values(ascending=False) * 100
print(f"\nTurnover par département :\n{turnover_dept.round(1)}")

# ── Absentéisme moyen par département
absence_dept = df.groupby('departement')['jours_absence'].mean().sort_values(ascending=False)
print(f"\nAbsences moyennes par département :\n{absence_dept.round(1)}")

# ── Corrélation performance / départ
perf_bas = df[df['score_performance'] < 3]['a_quitte'].mean() * 100
perf_haut = df[df['score_performance'] >= 7]['a_quitte'].mean() * 100
print(f"\nTurnover score < 3 : {perf_bas:.1f}%")
print(f"Turnover score >= 7 : {perf_haut:.1f}%")
print(f"Les mauvais performers partent {perf_bas/perf_haut:.1f}x plus souvent")

# ── Graphique 1 : Turnover par département
plt.figure(figsize=(10, 5))
sns.barplot(x=turnover_dept.index, y=turnover_dept.values, palette='Blues_d')
plt.title('Taux de turnover par département (%)')
plt.ylabel('Turnover (%)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('analysis/turnover_departement.png', dpi=150)
plt.close()
print("\nGraphique 1 sauvegardé")

# ── Graphique 2 : Absentéisme par département
plt.figure(figsize=(10, 5))
sns.barplot(x=absence_dept.index, y=absence_dept.values, palette='Oranges_d')
plt.title('Jours d\'absence moyens par département')
plt.ylabel('Jours absence')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('analysis/absence_departement.png', dpi=150)
plt.close()
print("Graphique 2 sauvegardé")

# ── Graphique 3 : Performance vs Turnover
plt.figure(figsize=(8, 5))
df['score_bin'] = pd.cut(df['score_performance'], bins=[0,3,5,7,10], labels=['< 3','3-5','5-7','> 7'])
turnover_perf = df.groupby('score_bin')['a_quitte'].mean() * 100
sns.barplot(x=turnover_perf.index, y=turnover_perf.values, palette='Reds_d')
plt.title('Turnover selon le score de performance')
plt.ylabel('Turnover (%)')
plt.xlabel('Score de performance')
plt.tight_layout()
plt.savefig('analysis/performance_turnover.png', dpi=150)
plt.close()
print("Graphique 3 sauvegardé")
