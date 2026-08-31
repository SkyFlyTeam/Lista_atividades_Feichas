import pandas as pd
import numpy as np

# Dados originais
temperaturas = [80, 82, 85, 81, 300, 83]

# Criando o DataFrame
df = pd.DataFrame({"temperatura": temperaturas})

print("DataFrame antes da correção:")
print(df)

# 1. Cálculo de Q1, Q3 e IQR
Q1 = df["temperatura"].quantile(0.25)
Q3 = df["temperatura"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)

# 2. Identificando o valor fora dos limites
outliers = df[
    (df["temperatura"] < limite_inferior) |
    (df["temperatura"] > limite_superior)
]

print("\nValor fora dos limites:")
print(outliers)

# 3. Calculando a mediana
mediana = df["temperatura"].median()

print("\nMediana:", mediana)

# 4. Substituindo somente o erro pela mediana
df["temperatura"] = np.where(
    (df["temperatura"] < limite_inferior) |
    (df["temperatura"] > limite_superior),
    mediana,
    df["temperatura"]
)

# 5. A quantidade de registros é preservada
print("\nDataFrame depois da correção:")
print(df)
