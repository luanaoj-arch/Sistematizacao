
import numpy as np

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

def test_percentil():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = percentil(dados, 25)
    esperado = np.percentile(dados, 25)

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )


def test_coeficiente_variacao():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = coeficiente_variacao(dados)

    esperado = (
        np.std(dados, ddof=1)
        / np.mean(dados)
    ) * 100

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )


def test_covariancia():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    resultado = covariancia(x, y)

    esperado = np.cov(x, y, ddof=1)[0, 1]

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )


def test_correlacao_pearson():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    resultado = correlacao_pearson(x, y)

    esperado = np.corrcoef(x, y)[0, 1]

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )
def test_media():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = media(dados)
    esperado = np.mean(dados)

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )
def test_mediana():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = mediana(dados)
    esperado = np.median(dados)

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )
def test_moda():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = moda(dados)
    esperado = [30]

    assert resultado == esperado
    
def test_amplitude():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = amplitude(dados)
    esperado = np.ptp(dados)

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )
def test_variancia_populacional():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = variancia_populacional(dados)
    esperado = np.var(dados, ddof=0)

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )
def test_variancia_amostral():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = variancia_amostral(dados)
    esperado = np.var(dados, ddof=1)

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )
def test_desvio_padrao_populacional():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = desvio_padrao_populacional(dados)
    esperado = np.std(dados, ddof=0)

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )
def test_desvio_padrao_amostral():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = desvio_padrao_amostral(dados)
    esperado = np.std(dados, ddof=1)

    assert np.isclose(
        resultado,
        esperado,
        atol=1e-9
    )
    
def test_quartis():
    dados = [10, 20, 30, 30, 40, 50, 30]

    resultado = quartis(dados)
    esperado = (
        np.percentile(dados, 25),
        np.percentile(dados, 50),
        np.percentile(dados, 75)
    )

    assert np.allclose(
        resultado,
        esperado,
        atol=1e-9
    )