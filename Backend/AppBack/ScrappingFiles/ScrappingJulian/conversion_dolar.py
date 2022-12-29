import requests
from bs4 import BeautifulSoup
from datetime import date

url_dolar = 'https://www.google.com/search?q=dolar+a+cop&sourceid=chrome&ie=UTF-8'

HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Opera/73.0.3856.284',
        'Accept-Language': 'es-ES,es;q=0.9'
    }

def dolar_convert():
    content = requests.get(url_dolar, headers = HEADER).text
    soup = BeautifulSoup(content, 'html.parser')
    PRECIO = soup.find_all('span', class_ = 'DFlfde SwHCTb')

    ## Ajuste de la moneda
    auxPrecio = PRECIO[0].text
    auxPrecio = auxPrecio.replace('.', '')
    auxPrecio = auxPrecio.replace(',', '.')
    try:
        auxPrecio = float(auxPrecio)
    except ValueError:
        print('error en la conversion')
    return auxPrecio


def getFecha():
    fecha = date.today().strftime('%Y-%m-%d')
    ## print(fecha)
    return fecha