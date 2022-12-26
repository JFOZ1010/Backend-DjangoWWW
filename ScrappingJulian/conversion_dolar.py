import requests
from bs4 import BeautifulSoup
from datetime import date

url_dolar = 'https://dolar.wilkinsonpc.com.co/'

def dolar_convert():
    content = requests.get(url_dolar).text
    soup = BeautifulSoup(content, 'html.parser')
    PRECIO = soup.find_all('span', class_ = 'baja-numero')

    ## Ajuste de la moneda
    auxPrecio = PRECIO[0].text[1:]
    auxPrecio = auxPrecio.replace(',', '')
    try:
        auxPrecio = float(auxPrecio)
    except ValueError:
        print('error en la conversion')

    return auxPrecio


def getFecha():
    fecha = date.today().strftime('%m/%d/%Y')
    ## print(fecha)
    return fecha