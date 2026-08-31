from typing import List


def calculate_division_point(array: List):
    return len(array) // 2

def calculate_median(array: List):
    division_point = calculate_division_point(array)
    if len(array) % 2 != 0:
        return array[division_point]
    return (array[division_point] + array[division_point - 1]) / 2

def calculate_iqr(q1: float, q3: float):
    return q3 - q1


def main(data: List):
    print(f"Recebido a lista {data} com {len(data)} elementos")

    ponto_divisao = calculate_division_point(data)

    if len(data) % 2 != 0:
        metade_inferior = data[:(ponto_divisao)]
        metade_superior = data[(ponto_divisao + 1):]
    else:
        metade_inferior = data[:ponto_divisao]
        metade_superior = data[ponto_divisao:]

    print("Metade inferior: ", metade_inferior)
    print("Metade superior: ", metade_superior)

    q1 = calculate_median(metade_inferior)
    q3 = calculate_median(metade_superior)
    print("Q1: ", q1)
    print("Q3: ", q3)

    iqr = calculate_iqr(q1, q3)
    print("IQR: ", iqr)

dados = [100, 150, 200, 250, 300, 350]

main(dados)