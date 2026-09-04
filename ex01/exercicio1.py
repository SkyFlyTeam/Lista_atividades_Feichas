import numpy as np

dados = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

Q1 = np.percentile(dados, 25)
Q2 = np.percentile(dados, 50)
Q3 = np.percentile(dados, 75)

print(f"Q1 (percentil 25): {Q1}")
print(f"Q2 (mediana / percentil 50): {Q2}")
print(f"Q3 (percentil 75): {Q3}")
