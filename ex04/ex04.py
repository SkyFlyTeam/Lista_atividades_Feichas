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

def is_outlier_value(inferior_limit, superior_limit, value): 
    return value < inferior_limit or value > superior_limit


def main(data: List):
    print(f"Recebido a lista {data} com {len(data)} elementos")

    sorted_data = sorted(data)

    division_point = calculate_division_point(sorted_data)

    if len(sorted_data) % 2 != 0:
        inferior_half = sorted_data[:(division_point)]
        superior_half = sorted_data[(division_point + 1):]
    else:
        inferior_half = sorted_data[:division_point]
        superior_half = sorted_data[division_point:]

    q1 = calculate_median(inferior_half)
    q3 = calculate_median(superior_half)
    print("Q1: ", q1)
    print("Q3: ", q3)

    iqr = calculate_iqr(q1, q3)
    print("IQR: ", iqr)

    iqr_limit = iqr * 1.5
    inferior_limit = q1 - iqr_limit
    superior_limit = q3 + iqr_limit

    print("Limite inferior: ", inferior_limit)
    print("Limite superior: ", superior_limit)

    outliers = []
    for number in sorted_data: 
        if is_outlier_value(inferior_limit, superior_limit, number): 
            outliers.append(number)

    print("Candidatos a outliers: ", outliers)


tensoes = [110, 115, 120, 118, 112, 220, 116, 114, 119, 12]

main(tensoes)