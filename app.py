import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

from minhastats import (
    media,
    mediana,
    moda,
    amplitude,
    desvio_padrao_amostral,
    quartis
)

st.title("Laboratório Estatístico Interativo")

st.write("Bem-vindo ao laboratório estatístico de Luanaaaaaaa!")

st.write("Módulo 2 - Estatística Descritiva")


# Carregando os dados
dados = pd.read_csv("Dataset.csv")
st.write("Quantidade de registros:", len(dados))

st.write("Dados do arquivo:")

st.dataframe(dados)

st.dataframe(dados)
st.write("## Escolha uma variável para analisar")

variavel = st.selectbox(
    "Selecione uma variável:",
    ["Age", "Rating", "Recommended IND", "Positive Feedback Count"]
)

st.write("Você escolheu:", variavel)

# Pegando os valores da variável escolhida
valores = dados[variavel].dropna().tolist()

# Calculando as estatísticas
resultado_media = media(valores)
resultado_mediana = mediana(valores)
resultado_moda = moda(valores)
resultado_amplitude = amplitude(valores)
resultado_desvio = desvio_padrao_amostral(valores)

st.write("## Resultados estatísticos")

st.write("Média:", resultado_media)
st.write("Mediana:", resultado_mediana)
st.write("Moda:", resultado_moda)
st.write("Amplitude:", resultado_amplitude)
st.write("Desvio padrão amostral:", resultado_desvio)

st.write("Desvio padrão amostral:", resultado_desvio)

# Tabela de frequência

st.write("## Tabela de frequência")

classes = pd.cut(
    dados[variavel].dropna(),
    bins=10
)

frequencia = classes.value_counts().sort_index()

tabela_frequencia = frequencia.reset_index()

tabela_frequencia.columns = [
    "Classe",
    "Frequência"
]

st.dataframe(
    tabela_frequencia,
    hide_index=True
)

# Gráfico da variável escolhida

st.write("## Gráfico de distribuição")

fig, ax = plt.subplots()

ax.hist(valores, bins=10)

ax.set_title(f"Distribuição de {variavel}")
ax.set_xlabel(variavel)
ax.set_ylabel("Frequência")

st.pyplot(fig)

# Detecção de outliers usando o método IQR

st.write("## Detecção de outliers (IQR)")

q1, q2, q3 = quartis(valores)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers = [
    valor for valor in valores
    if valor < limite_inferior or valor > limite_superior
]

st.write("Primeiro quartil (Q1):", q1)
st.write("Mediana (Q2):", q2)
st.write("Terceiro quartil (Q3):", q3)
st.write("Intervalo interquartil (IQR):", iqr)

st.write("Limite inferior:", limite_inferior)
st.write("Limite superior:", limite_superior)

st.write("Quantidade de outliers:", len(outliers))

if len(outliers) > 0:
    st.write("Alguns valores identificados:", outliers[:10])
else:
    st.write("Não foram encontrados outliers.")

    # Interpretação dos resultados

st.write("## Interpretação dos resultados")

if resultado_media > resultado_mediana:
    st.info(
        "A média é maior que a mediana, indicando que alguns valores "
        "mais altos podem estar influenciando a média."
    )

elif resultado_media < resultado_mediana:
    st.info(
        "A média é menor que a mediana, indicando que alguns valores "
        "mais baixos podem estar influenciando a média."
    )

else:
    st.info(
        "A média e a mediana são iguais, indicando maior equilíbrio "
        "entre os valores analisados."
    )

st.write(
    f"A variável analisada foi {variavel}. "
    f"A média encontrada foi {resultado_media:.2f}, "
    f"enquanto a mediana foi {resultado_mediana:.2f}."
)

st.write(
    f"O desvio padrão amostral foi {resultado_desvio:.2f}, "
    "representando a dispersão dos valores em relação à média."
)

st.write(
    f"Foram identificados {len(outliers)} possíveis outliers "
    "pelo método do intervalo interquartil (IQR)."
)

# Módulo 3 - Simulação de Monte Carlo
# Lei dos Grandes Números

st.write("## Módulo 3 - Lei dos Grandes Números")

st.write(
    "Simulação de lançamentos de uma moeda para observar "
    "a aproximação da proporção de caras a 50%."
)

quantidade_lancamentos = st.slider(
    "Quantidade de lançamentos:",
    min_value=10,
    max_value=10000,
    value=1000,
    step=10
)

lancamentos = np.random.choice(
    ["Cara", "Coroa"],
    size=quantidade_lancamentos
)

quantidade_caras = np.sum(lancamentos == "Cara")

proporcao_caras = quantidade_caras / quantidade_lancamentos

st.write("Quantidade de caras:", quantidade_caras)

st.write(
    "Proporção de caras:",
    f"{proporcao_caras:.2%}"
)

st.write(
    "A proporção esperada de caras em uma moeda equilibrada "
    "é aproximadamente 50%."
)

# Gráfico da Lei dos Grandes Números

st.write("## Evolução da proporção de caras")

resultados_caras = (lancamentos == "Cara").astype(int)

proporcao_acumulada = np.cumsum(resultados_caras) / np.arange(
    1, quantidade_lancamentos + 1
)

fig_lgn, ax_lgn = plt.subplots()

ax_lgn.plot(proporcao_acumulada)

ax_lgn.axhline(
    y=0.5,
    linestyle="--",
    label="Valor esperado: 50%"
)

ax_lgn.set_title("Lei dos Grandes Números")
ax_lgn.set_xlabel("Quantidade de lançamentos")
ax_lgn.set_ylabel("Proporção acumulada de caras")

ax_lgn.legend()

st.pyplot(fig_lgn)

# Teorema do Limite Central

st.write("## Teorema do Limite Central")

st.write(
    "Vamos observar a distribuição das médias de várias amostras "
    "retiradas de uma população."
)

tamanho_amostra = st.slider(
    "Tamanho de cada amostra:",
    min_value=5,
    max_value=100,
    value=30,
    step=5
)

quantidade_amostras = st.slider(
    "Quantidade de amostras:",
    min_value=100,
    max_value=2000,
    value=1000,
    step=100
)

# Utilizando dados  do dataset

populacao_tlc = pd.to_numeric(
    dados["Age"],
    errors="coerce"
).dropna().to_numpy()

medias_amostrais = []

for i in range(quantidade_amostras):
    amostra = np.random.choice(
        populacao_tlc,
        size=tamanho_amostra,
        replace=True
    )

medias_amostrais.append(np.mean(amostra))

fig_tlc, ax_tlc = plt.subplots()

ax_tlc.hist(
    medias_amostrais,
    bins=30
)

ax_tlc.set_title("Distribuição das Médias Amostrais")
ax_tlc.set_xlabel("Médias das amostras")
ax_tlc.set_ylabel("Frequência")

st.pyplot(fig_tlc)

st.write("Menor média amostral:", min(medias_amostrais))
st.write("Maior média amostral:", max(medias_amostrais))
st.write(
    "Desvio padrão completo:",
    np.std(medias_amostrais, ddof=0)
)
# Interpretação do Teorema do Limite Central

st.write("## Interpretação do TLC")

media_das_medias = np.mean(medias_amostrais)
desvio_das_medias = np.std(
    medias_amostrais,
    ddof=0
)

st.write(
    f"A média das médias amostrais foi "
    f"{media_das_medias:.2f}."
)

st.write(
    f"O desvio padrão das médias amostrais foi "
    f"{desvio_das_medias:.2f}."
)

st.info(
    "O Teorema do Limite Central afirma que, sob condições "
    "adequadas, a distribuição das médias amostrais tende "
    "a se aproximar de uma distribuição normal conforme "
    "o tamanho das amostras aumenta."
)

st.write(
    "Ao aumentar o tamanho da amostra, a variabilidade "
    "das médias tende a diminuir, fazendo com que elas "
    "se concentrem ao redor da média populacional."
)

# Módulo 4 - Distribuição Normal Teórica

st.write("## Módulo 4 - Distribuição Normal")

valores_normal = pd.to_numeric(
    dados["Age"],
    errors="coerce"
).dropna().to_numpy()

media_normal = np.mean(valores_normal)
desvio_normal = np.std(valores_normal, ddof=0)

eixo_x = np.linspace(
    min(valores_normal),
    max(valores_normal),
    200
)

densidade_normal = (
    1 / (desvio_normal * np.sqrt(2 * np.pi))
) * np.exp(
    -0.5 * ((eixo_x - media_normal) / desvio_normal) ** 2
)

fig_normal, ax_normal = plt.subplots()

ax_normal.hist(
    valores_normal,
    bins=30,
    density=True,
    alpha=0.6,
    label="Dados reais"
)

ax_normal.plot(
    eixo_x,
    densidade_normal,
    label="Distribuição Normal"
)

ax_normal.set_title(
    "Dados reais e Distribuição Normal"
)

ax_normal.set_xlabel("Idade")
ax_normal.set_ylabel("Densidade")

ax_normal.legend()

st.pyplot(fig_normal)

# Interpretação da Distribuição Normal

st.write("## Interpretação da Distribuição Normal")

st.write(
    f"A média das idades foi {media_normal:.2f}."
)

st.write(
    f"O desvio padrão populacional das idades foi "
    f"{desvio_normal:.2f}."
)

st.info(
    "O histograma representa a distribuição das idades "
    "observadas no dataset. A curva representa uma "
    "distribuição normal teórica calculada usando a "
    "média e o desvio padrão dos dados."
)

st.write(
    "Quanto mais o formato dos dados se aproximar da curva, "
    "maior será a semelhança visual com a distribuição normal. "
    "Essa comparação é apenas descritiva."
)# Distribuição de Poisson

st.write("## Distribuição de Poisson")

valores_poisson = pd.to_numeric(
    dados["Positive Feedback Count"],
    errors="coerce"
).dropna().to_numpy()

lambda_poisson = np.mean(valores_poisson)

maior_valor = int(np.percentile(valores_poisson, 99))

eixo_poisson = np.arange(0, maior_valor + 1)

probabilidades_poisson = []

for valor in eixo_poisson:
    probabilidade = math.exp(
        -lambda_poisson
    ) * (lambda_poisson ** valor) / math.factorial(valor)

    probabilidades_poisson.append(probabilidade)

fig_poisson, ax_poisson = plt.subplots()

limite_superior = maior_valor + 0.5

valores_grafico = valores_poisson[
    valores_poisson <= maior_valor
]

ax_poisson.hist(
    valores_grafico,
    bins=np.arange(-0.5, maior_valor + 1.5, 1),
    density=True,
    alpha=0.6,
    label="Dados reais"
)

ax_poisson.plot(
    eixo_poisson,
    probabilidades_poisson,
    marker="o",
    linestyle="-",
    label="Poisson teórica"
)

ax_poisson.set_title(
    "Dados reais e Distribuição de Poisson"
)

ax_poisson.set_xlabel("Quantidade de feedbacks positivos")
ax_poisson.set_ylabel("Probabilidade / Densidade")

ax_poisson.legend()

st.pyplot(fig_poisson)

st.write(
    f"Parâmetro estimado da distribuição (lambda): "
    f"{lambda_poisson:.2f}"
)st.write("### Discussão do ajuste")

st.info(
    "A qualidade do ajuste pode ser avaliada visualmente "
    "comparando o formato do histograma com a distribuição "
    "de Poisson. Quanto mais próximas forem as alturas e "
    "o formato das distribuições, maior será a semelhança "
    "visual. A comparação é descritiva e não representa "
    "um teste estatístico formal de ajuste."
)