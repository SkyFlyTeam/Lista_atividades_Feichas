from typing import List

import matplotlib.pyplot as plt


def calculate_division_point(array: List):
    return len(array) // 2

def calculate_median(array: List):
    division_point = calculate_division_point(array)
    if len(array) % 2 != 0:
        return array[division_point]
    return (array[division_point] + array[division_point - 1]) / 2

def calculate_iqr(q1: float, q3: float):
    return q3 - q1

def is_outlier_value(inferior_limit, superior_limit, value):
    return value < inferior_limit or value > superior_limit


def plot_boxplot(data: List):
    plt.figure(figsize=(6, 4))
    plt.boxplot(data, tick_labels=["tempos"])
    plt.title("Boxplot - visualizando outliers")
    plt.ylabel("valor")
    plt.savefig("ex11/boxplot.png", dpi=120, bbox_inches="tight")
    plt.show()


def main(data: List):
    print(f"Recebido a lista {data} com {len(data)} elementos")

    sorted_data = sorted(data)

    # 1. boxplot
    plot_boxplot(sorted_data)

    division_point = calculate_division_point(sorted_data)

    if len(sorted_data) % 2 != 0:
        inferior_half = sorted_data[:division_point]
        superior_half = sorted_data[(division_point + 1):]
    else:
        inferior_half = sorted_data[:division_point]
        superior_half = sorted_data[division_point:]

    # 2. Q1  /  3. Q3
    q1 = calculate_median(inferior_half)
    q3 = calculate_median(superior_half)
    print("Q1: ", q1)
    print("Q3: ", q3)

    # 4. IQR
    iqr = calculate_iqr(q1, q3)
    print("IQR: ", iqr)

    # 5. limites
    iqr_limit = iqr * 1.5
    inferior_limit = q1 - iqr_limit
    superior_limit = q3 + iqr_limit
    print("Limite inferior: ", inferior_limit)
    print("Limite superior: ", superior_limit)

    # 6. candidatos a outlier (numericamente)
    outliers = []
    for number in sorted_data:
        if is_outlier_value(inferior_limit, superior_limit, number):
            outliers.append(number)

    print("Candidatos a outliers: ", outliers)

    # Comparacao com o grafico
    print()
    print("Comparacao com o boxplot:")
    print(
        "O ponto que aparece isolado alem do 'bigode' superior do boxplot e o 80. "
        "A Regra do IQR tambem aponta o 80 como candidato a outlier "
        f"(80 > limite superior {superior_limit})."
    )
    print(
        "Resposta: Sim. O valor destacado visualmente no boxplot (80) e o mesmo "
        "identificado pela Regra do IQR."
    )


tempos = [20, 21, 22, 23, 24, 25, 26, 80]

main(tempos)
