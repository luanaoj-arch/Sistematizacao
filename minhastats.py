def media(dados):
    """
    Calcula a média aritmética.

    Parâmetros:
        dados: lista de valores numéricos

    Retorna:
        Média dos valores
    """

    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia")

    soma = 0

    for valor in dados:
        soma += valor

    return soma / len(dados)


# mediana 
def mediana(dados):
    """
    Calcula a mediana dos valores.
    """

    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia")

    dados_ordenados = sorted(dados)

    n = len(dados_ordenados)
    meio = n // 2

    if n % 2 == 0:
        return (
            dados_ordenados[meio - 1]
            + dados_ordenados[meio]
        ) / 2

    else:
        return dados_ordenados[meio]
    
#Moda
def moda(dados):
    """
    Calcula a moda dos dados.

    Retorna todos os valores com maior frequência.
    """

    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia")

    frequencias = {}

    for valor in dados:
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1

    maior_frequencia = max(frequencias.values())

    modas = []

    for valor, frequencia in frequencias.items():
        if frequencia == maior_frequencia:
            modas.append(valor)

    return modas

    #amplitude

def amplitude(dados):
    """
    Calcula a amplitude dos dados.
    """

    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia")

    maior = dados[0]
    menor = dados[0]

    for valor in dados:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

    return maior - menor

    #Variancia Populacional
def variancia_populacional(dados):
    """
    Calcula a variância populacional.
    """

    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia")

    media_valores = sum(dados) / len(dados)

    soma_quadrados = 0

    for valor in dados:
        diferenca = valor - media_valores
        soma_quadrados += diferenca ** 2

    return soma_quadrados / len(dados)

# Variancia Amostral
import math
def variancia_amostral(dados):
    """
    Calcula a variância amostral.
    """

    if len(dados) < 2:
        raise ValueError(
            "São necessários pelo menos 2 valores"
        )

    media_valores = sum(dados) / len(dados)

    soma_quadrados = 0

    for valor in dados:
        diferenca = valor - media_valores
        soma_quadrados += diferenca ** 2

    return soma_quadrados / (len(dados) - 1)

#Desvio Padrap Populaciona

def desvio_padrao_populacional(dados):
    """
    Calcula o desvio padrão populacional.
    """

    variancia = variancia_populacional(dados)

    return math.sqrt(variancia)

#Desvio Padrao Amostral
def desvio_padrao_amostral(dados):
    """
    Calcula o desvio padrão amostral.
    """

    variancia = variancia_amostral(dados)

    return math.sqrt(variancia)

    # Quartis e Percentis

def percentil(dados, p):
    """
    Calcula um percentil usando interpolação linear.
    O valor de p deve estar entre 0 e 100.
    """

    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia")

    if p < 0 or p > 100:
        raise ValueError("O percentil deve estar entre 0 e 100")

    dados_ordenados = sorted(dados)

    posicao = (len(dados_ordenados) - 1) * (p / 100)

    inferior = int(posicao)
    superior = inferior + 1

    if superior >= len(dados_ordenados):
        return dados_ordenados[inferior]

    parte_decimal = posicao - inferior

    return (
        dados_ordenados[inferior]
        + parte_decimal
        * (
            dados_ordenados[superior]
            - dados_ordenados[inferior]
        )
    )


def quartis(dados):
    """
    Retorna o primeiro, segundo e terceiro quartis.
    """

    q1 = percentil(dados, 25)
    q2 = percentil(dados, 50)
    q3 = percentil(dados, 75)

    return q1, q2, q3

# Coeficiente de Variação

def coeficiente_variacao(dados):
    """
    Calcula o coeficiente de variação amostral em porcentagem.
    """

    if len(dados) < 2:
        raise ValueError("São necessários pelo menos 2 valores")

    media_valores = media(dados)

    if media_valores == 0:
        raise ValueError(
            "A média não pode ser igual a zero"
        )

    desvio = desvio_padrao_amostral(dados)

    return (desvio / media_valores) * 100

    # Covariância

def covariancia(x, y):
    """
    Calcula a covariância amostral entre duas listas.
    """

    if len(x) != len(y):
        raise ValueError(
            "As listas devem ter o mesmo tamanho"
        )

    if len(x) < 2:
        raise ValueError(
            "São necessários pelo menos 2 valores"
        )

    media_x = media(x)
    media_y = media(y)

    soma_produtos = 0

    for i in range(len(x)):
        diferenca_x = x[i] - media_x
        diferenca_y = y[i] - media_y

        soma_produtos += diferenca_x * diferenca_y

    return soma_produtos / (len(x) - 1)

    # Correlação de Pearson

def correlacao_pearson(x, y):
    """
    Calcula o coeficiente de correlação de Pearson.
    """

    if len(x) != len(y):
        raise ValueError(
            "As listas devem ter o mesmo tamanho"
        )

    if len(x) < 2:
        raise ValueError(
            "São necessários pelo menos 2 valores"
        )

    media_x = media(x)
    media_y = media(y)

    soma_xy = 0
    soma_x_quadrado = 0
    soma_y_quadrado = 0

    for i in range(len(x)):
        diferenca_x = x[i] - media_x
        diferenca_y = y[i] - media_y

        soma_xy += diferenca_x * diferenca_y
        soma_x_quadrado += diferenca_x ** 2
        soma_y_quadrado += diferenca_y ** 2

    denominador = (
        soma_x_quadrado * soma_y_quadrado
    ) ** 0.5

    if denominador == 0:
        raise ValueError(
            "A correlação não pode ser calculada"
        )

    return soma_xy / denominador

def regressao_linear(x, y):
    media_x = media(x)
    media_y = media(y)

    numerador = 0
    denominador = 0

    for i in range(len(x)):
        numerador += (x[i] - media_x) * (y[i] - media_y)
        denominador += (x[i] - media_x) ** 2

    coeficiente_angular = numerador / denominador

    coeficiente_linear = (
        media_y - coeficiente_angular * media_x
    )

    return coeficiente_linear, coeficiente_angular

