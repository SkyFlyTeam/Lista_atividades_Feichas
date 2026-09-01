import pandas as pd

dados = {
    'Pedido': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Valor': [100, 120, 110, 130, 125, 115, 140, 1000]
}

df = pd.DataFrame(dados)

q1 = df['Valor'].quantile(0.25)
q3 = df['Valor'].quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - (iqr * 1.5)
limite_superior = q3 + (iqr * 1.5)

# Q1 (25%): 113.75
print("Q1:", q1)
# Q3 (75%): 132.5
print("Q3:", q3)
# IQR (Q3 - Q1): 18.75
print("IQR:", iqr)
# Limite inferior: 85.625 (Q1 - 1.5 × IQR)
print("Limite inferior:", limite_inferior)
# Limite superior: 160.625 (Q3 + 1.5 × IQR)
print("Limite superior:", limite_superior)

df['Outlier'] = df['Valor'].apply(lambda x: x < limite_inferior or x > limite_superior)

print("\nDataFrame completo:")
print(df)
print("\nApenas outliers:")
print(df[df['Outlier'] == True])
