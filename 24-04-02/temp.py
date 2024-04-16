import requests
from bs4 import BeautifulSoup

def obter_temperatura_maxima(url):
    # Fazendo a requisição da página
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Criando o objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrando a tag span com o atributo data-testid e a classe especificada
        temperatura_maxima_tag = soup.find('span', {'data-testid': 'TemperatureValue', 'class': 'DetailsSummary--highTempValue--3PjlX'})

        # Verificando se a tag foi encontrada
        if temperatura_maxima_tag:
            # Extraindo o valor da temperatura máxima
            temperatura_maxima = temperatura_maxima_tag.text.strip()
            return temperatura_maxima

    # Retorna None se não conseguir extrair a temperatura máxima
    return None

# URL da página
url = 'https://weather.com/weather/tenday/l/976c31acf89c4c04d005468381bdb7ee6ab478e7496b808f158080b044d68c3d'

# Obtendo a temperatura máxima
temperatura_maxima = obter_temperatura_maxima(url)

if temperatura_maxima:
    print(f'Temperatura Máxima: {temperatura_maxima}')
else:
    print('Não foi possível obter a temperatura máxima.')
