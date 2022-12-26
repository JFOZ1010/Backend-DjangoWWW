import requests
from bs4 import BeautifulSoup
import json
from datetime import date

def parseInfowNewegg(producto, type_id, user_id, dollarToday):
    enlace = producto.find(class_ = 'item-title')
    nombre = producto.find(class_ = 'item-title')
    precio = producto.find(class_ = 'price-current')
    imagen = producto.find(class_ = 'item-img')
    
    if (precio.strong and precio.sup is not None):
        product_data = {
            "item_name" : " ".join(nombre.text.split()),
            "item_price" : round(float(precio.strong.text.replace(',','') + precio.sup.text) * dollarToday) ,
            "item_picture" : str(imagen.img['src']),
            "item_description" : "details",
            "item_url" : str(enlace['href']),
            "type_id" : type_id,
            "user_id" : user_id,
            "item_date": date.today().strftime("%Y-%m-%d")
        }
        return product_data
    else:
        return {}


def newegg():
    
    print("Obteniendo precio dolar hoy")
    urlDollar = 'https://www.larepublica.co/indicadores-economicos/mercado-cambiario/dolar'
    dollar = requests.get(urlDollar)
    soupDollar = BeautifulSoup(dollar.content, 'html.parser')

    dollarToday = float(soupDollar.find( 'span', {'class': 'price' }).text.replace('$', '').replace('.', '').replace(',', '.').replace(' ', ''))
    print(dollarToday)


    print("Obteniendo información de newegg Ryzen 3...")
    urlR3 = 'https://www.newegg.com/p/pl?N=50001028%20601295133%20100007671&d=ryzen+3'
    neweggR3 = requests.get(urlR3)
    soupR3 = BeautifulSoup(neweggR3.text, 'html.parser')

    print("Obteniendo información de mercadolibre Ryzen 5 y 7...")
    urlR5and7 = 'https://www.newegg.com/p/pl?d=ryzen+5&N=601350561%20100007671'
    neweggR5and7 = requests.get(urlR5and7)
    soupR5and7 = BeautifulSoup(neweggR5and7.text, 'html.parser')


    listaProductosR3 = soupR3.find_all('div', {'class': 'item-container'})
    listaProductosR5and7 = soupR5and7.find_all('div', {'class': 'item-container'})

    dataR3 = []
    dataR5and7 = []

    print("Parseando elementos de Ryzen 3...")
    for producto in listaProductosR3:
        product_data = parseInfowNewegg(producto, 1, 'auth0|639e3f6e9c43cd6f74e81ba0', dollarToday)
        if (len(product_data)):
            dataR3.append(product_data)

    print("Parseando elementos de Ryzen 5 y 7...")
    for producto in listaProductosR5and7:
        product_data = parseInfowNewegg(producto, 1, 'auth0|639e3f6e9c43cd6f74e81ba0', dollarToday)
        if (len(product_data)):
            dataR5and7.append(product_data)

    print("Almacenamiento completado")

    print("Iniciando almacenamiento en bd")

    print("Almacenando datos...")

    backurl = 'http://localhost:6060/api/item/create2'

    dataFull = dataR3 + dataR5and7
    res = requests.post(backurl, json = dataFull)
        
newegg()
