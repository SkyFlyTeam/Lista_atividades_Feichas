import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from ex05.ex05 import detectar_anomalias

dados = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]
multiplicador = 1.5

Q1, Q3, IQR, limite_inferior, limite_superior, candidatos = detectar_anomalias(
    dados, multiplicador
)

print("Dados originais:", dados)
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)
print("Candidatos a outlier:", candidatos)

for valor in candidatos:
    if valor < limite_inferior:
        print(
            f"O valor {valor} ficou abaixo do limite inferior "
            f"{limite_inferior}. Portanto, {valor} é candidato a outlier "
            "pela Regra do IQR."
        )
    elif valor > limite_superior:
        print(
            f"O valor {valor} ultrapassou o limite superior "
            f"{limite_superior}. Portanto, {valor} é candidato a outlier "
            "pela Regra do IQR."
        )
