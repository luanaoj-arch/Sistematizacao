from minhastats import (
    media,
    mediana,
    moda,
    amplitude,
    variancia_populacional,
    variancia_amostral,
    desvio_padrao_populacional,
    desvio_padrao_amostral,
    percentil, 
    quartis,
    coeficiente_variacao,
    covariancia,
    correlacao_pearson
)
dados = [10, 20, 30, 40, 50, 30]

resultado = media(dados)

print("Média:", resultado)

print("Mediana:", mediana(dados))
print("Moda:", moda(dados))
print("Amplitude:", amplitude(dados))
print("Variância Populacional:", variancia_populacional(dados))
print("Variância Amostral:", variancia_amostral(dados))
print("Desvio Padrão Populacional:", desvio_padrao_populacional(dados))
print("Desvio Padrão Amostral:", desvio_padrao_amostral(dados))
print("Percentil 25:", percentil(dados, 25))
print("Percentil 50:", percentil(dados, 50))
print("Percentil 75:", percentil(dados, 75))
print("Quartis:", quartis(dados))
print ("Coeficiente de Variação:", coeficiente_variacao(dados))
print("Covariância:", covariancia(dados, dados))
print("Correlação de Pearson:", correlacao_pearson(dados, dados))
