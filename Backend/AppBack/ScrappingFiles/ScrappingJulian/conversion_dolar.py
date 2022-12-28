import requests
from bs4 import BeautifulSoup
from datetime import date

url_dolar = 'https://dolar.wilkinsonpc.com.co/'

def dolar_convert():
    print("Obteniendo precio dolar hoy")
    urlDollar = 'https://www.larepublica.co/indicadores-economicos/mercado-cambiario/dolar'
    dollar = requests.get(urlDollar)
    soupDollar = BeautifulSoup(dollar.content, 'html.parser')

    dollarToday = float(soupDollar.find( 'span', {'class': 'price' }).text.replace('$', '').replace('.', '').replace(',', '.').replace(' ', ''))

    return dollarToday


def getFecha():
    fecha = date.today().strftime("%Y-%m-%d")
    ## print(fecha)
    return fecha