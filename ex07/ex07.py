import pandas as pd

dados = {
    'ID_Maquina': [1, 2, 3, 4, 5],
    'Uso_Memoria_MB': [2048, 2100, 2050, 8192, 2080]
}

df = pd.DataFrame(dados)

q1 = df['Uso_Memoria_MB'].quantile(0.25)
q3 = df['Uso_Memoria_MB'].quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - (iqr * 1.5)
limite_superior = q3 + (iqr * 1.5)

outliers = df[(df['Uso_Memoria_MB'] < limite_inferior) | (df['Uso_Memoria_MB'] > limite_superior)]

# Q1 (25%): 2050.0 MB
print("Q1:", q1)
# Q3 (75%): 2100.0 MB
print("Q3:", q3)
# IQR (Q3 - Q1): 50.0 MB
print("IQR:", iqr)
# Limite inferior: 1975.0 MB (Q1 - 1.5 × IQR)
print("Limite inferior:", limite_inferior)
# Limite superior: 2175.0 MB (Q3 + 1.5 × IQR)
print("Limite superior:", limite_superior)
print("\nValores candidatos a outliers:")
for idx, row in outliers.iterrows():
    print(f"  ID: {row['ID_Maquina']} | Uso Memória: {row['Uso_Memoria_MB']} MB")
