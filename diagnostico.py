import pandas as pd

# Carregar o dataset
dados = pd.read_csv("dataset.csv")

print("\n===== TAMANHO DO DATASET =====")
print(f"Linhas: {dados.shape[0]}")
print(f"Colunas: {dados.shape[1]}")

print("\n===== COLUNAS =====")
print(dados.columns.tolist())

print("\n===== TIPOS DE DADOS =====")
print(dados.dtypes)

print("\n===== VALORES AUSENTES =====")
print(dados.isnull().sum())

print("\n===== PRIMEIRAS LINHAS =====")
print(dados.head())