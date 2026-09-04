import numpy as np

dados = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

Q1 = np.percentile(dados, 25)
Q3 = np.percentile(dados, 75)

IQR = Q3 - Q1
limite_iqr = 1.5 * IQR
limite_inferior = Q1 - limite_iqr
limite_superior = Q3 + limite_iqr

print(f"Q1: {Q1}")
print(f"Q3: {Q3}")
print(f"IQR: {IQR}")
print(f"1.5 x IQR: {limite_iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")

valor = 150
if valor < limite_inferior or valor > limite_superior:
    print(f"O valor {valor} ultrapassa os limites e é candidato a outlier.")
else:
    print(f"O valor {valor} está dentro dos limites e não é candidato a outlier.")
