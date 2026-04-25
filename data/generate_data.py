import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

departements = ['Support client', 'Commercial', 'RH', 'Finance', 'IT', 'Marketing', 'Operations']
niveaux = ['Junior', 'Confirmé', 'Senior', 'Manager']

df = pd.DataFrame({
    'employe_id': range(1, n + 1),
    'departement': np.random.choice(departements, n, p=[0.25, 0.20, 0.10, 0.10, 0.15, 0.10, 0.10]),
    'niveau': np.random.choice(niveaux, n, p=[0.35, 0.30, 0.25, 0.10]),
    'anciennete_ans': np.random.exponential(scale=4, size=n).clip(0, 20).round(1),
    'salaire': np.random.normal(42000, 12000, n).clip(24000, 95000).
