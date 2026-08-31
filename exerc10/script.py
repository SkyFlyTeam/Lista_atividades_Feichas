import pandas as pd

grupo_a = [48, 49, 50, 50, 51, 52, 52, 53]
grupo_b = [20, 30, 40, 50, 60, 70, 80, 90]

df = pd.DataFrame({
    "grupo_a": grupo_a,
    "grupo_b": grupo_b
})

# Grupo A
q1_a = df["grupo_a"].quantile(0.25)
q3_a = df["grupo_a"].quantile(0.75)
iqr_a = q3_a - q1_a

# Grupo B
q1_b = df["grupo_b"].quantile(0.25)
q3_b = df["grupo_b"].quantile(0.75)
iqr_b = q3_b - q1_b

print("Grupo A")
print("Q1:", q1_a)
print("Q3:", q3_a)
print("IQR:", iqr_a)

print("\nGrupo B")
print("Q1:", q1_b)
print("Q3:", q3_b)
print("IQR:", iqr_b)

"""
Qual grupo possui o maior IQR? O Grupo B, com IQR igual a 35.

Em qual grupo os 50% centrais estão mais espalhados? 
No Grupo B, porque seu IQR é muito maior. Isso mostra que a metade central dos dados ocupa um intervalo maior.

Um IQR maior significa necessariamente que os dados estão errados? 
Não. Um IQR maior apenas indica maior dispersão nos 50% centrais dos dados. Isso pode ser uma característica perfeitamente 
normal do conjunto. Para afirmar que existem erros ou valores anômalos, é necessário analisar o contexto e, por exemplo, 
verificar se há observações fora dos limites definidos a partir do IQR.
"""
