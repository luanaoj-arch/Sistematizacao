import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from minhastats import (
    media,
    mediana,
    moda,
    amplitude,
    desvio_padrao_amostral
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