def detectar_anomalias(dados, multiplicador):
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)

    def mediana(valores):
        tamanho = len(valores)

        if tamanho % 2 == 0:
            meio = tamanho // 2
            return (valores[meio - 1] + valores[meio]) / 2
        else:
            return valores[tamanho // 2]

    if n % 2 == 0:
        metade_inferior = dados_ordenados[:n // 2]
        metade_superior = dados_ordenados[n // 2:]
    else:
        metade_inferior = dados_ordenados[:n // 2]
        metade_superior = dados_ordenados[n // 2 + 1:]

    Q1 = mediana(metade_inferior)
    Q3 = mediana(metade_superior)

    IQR = Q3 - Q1

    limite_inferior = Q1 - multiplicador * IQR
    limite_superior = Q3 + multiplicador * IQR

    candidatos = [
        valor for valor in dados
        if valor < limite_inferior or valor > limite_superior
    ]

    return Q1, Q3, IQR, limite_inferior, limite_superior, candidatos
