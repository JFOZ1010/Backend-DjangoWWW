import requests
from bs4 import BeautifulSoup
import json
from unidecode import unidecode
from datetime import date

def parseInfoAmazon(producto, type_id, user_id, dollarToday):
    enlace = producto.find(class_ = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    nombre = producto.find(class_ = 'a-size-medium a-color-base a-text-normal')
    precio = producto.find(class_ = 'a-price-whole')
    imagen = producto.find(class_ = 's-image')
    
    if (precio is not None):
        product_data = {
            "item_name" : unidecode(" ".join(nombre.text.split())),
            "item_price" : round(int(precio.text.replace('.', '')) * dollarToday) ,
            "item_picture" : str(imagen['src']),
            "item_description" : "Kevin",
            "item_url" : str('https://www.amazon.com' + enlace['href']),
            "type_id" : type_id,
            "user_id" : user_id,
            "item_date": date.today().strftime("%Y-%m-%d")
        }
        return product_data
    else:
        return {}


def amazon():

    print("Obteniendo precio dolar hoy")
    urlDollar = 'https://www.larepublica.co/indicadores-economicos/mercado-cambiario/dolar'
    dollar = requests.get(urlDollar)
    soupDollar = BeautifulSoup(dollar.content, 'html.parser')

    dollarToday = float(soupDollar.find( 'span', {'class': 'price' }).text.replace('$', '').replace('.', '').replace(',', '.').replace(' ', ''))
    print(dollarToday)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    print("Obteniendo información de Amazon Ryzen 3...")
    urlR3 = 'https://www.amazon.com/s?k=Ryzen+3+processor&rh=n%3A229189%2Cp_n_feature_four_browse-bin%3A18107800011&dc&language=es&ds=v1%3A8LFKWmdU90ODVVohNN7I7GmkHiaOQfCh8xphvHk%2BmOo&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3KA9B0T0N0V8Y&qid=1671332039&rnid=676578011&sprefix=ryzen+3+processo%2Caps%2C677&ref=sr_nr_p_n_feature_four_browse-bin_6'
    amazonR3 = requests.get(urlR3, headers = headers)
    soupR3 = BeautifulSoup(amazonR3.text, 'html.parser')

    print("Obteniendo información de Amazon Ryzen 5...")
    urlR5 = 'https://www.amazon.com/s?k=Ryzen+5+processor&i=computers&rh=n%3A229189%2Cp_n_feature_four_browse-bin%3A18107801011&dc&language=es&ds=v1%3AAan5OZ8zP00lhzgozCMYUI26d01DY2qSdtCAR6hUNpM&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1671334484&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_3'
    amazonR5 = requests.get(urlR5, headers = headers)
    soupR5 = BeautifulSoup(amazonR5.text, 'html.parser')

    print("Obteniendo información de Amazon Ryzen 7...")
    urlR7 = 'https://www.amazon.com/s?k=Ryzen+7+processor&i=computers&rh=n%3A229189%2Cp_n_feature_four_browse-bin%3A18107802011&dc&language=es&ds=v1%3A8TbQLWDR4dBlC6UEQ9CROBvDE%2B%2BePq87vpUM%2B8XrK%2Fo&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1671334521&rnid=676578011&ref=sr_nr_p_n_feature_four_browse-bin_5'
    amazonR7 = requests.get(urlR7, headers = headers)
    soupR7 = BeautifulSoup(amazonR7.text, 'html.parser')
    
    listaProductosR3 = soupR3.find_all('div', {'class' : 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'})
    listaProductosR5 = soupR5.find_all('div', {'class' : 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'})
    listaProductosR7 = soupR7.find_all('div', {'class' : 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'})
    
    dataR3 = []
    dataR5 = []
    dataR7 = []

    print("Parseando elementos de Ryzen 3...")
    for producto in listaProductosR3:
        product_data = parseInfoAmazon(producto, 1, 'auth0|638b682bbc99c67d7152083b', dollarToday)
        if (len(product_data)):
            dataR3.append(product_data)
    
    print("Parseando elementos de Ryzen 5...")
    for producto in listaProductosR5:
        product_data = parseInfoAmazon(producto, 1, 'auth0|638b682bbc99c67d7152083b', dollarToday)
        if (len(product_data)):
            dataR5.append(product_data)

    print("Parseando elementos de Ryzen 7...")
    for producto in listaProductosR7:
        product_data = parseInfoAmazon(producto, 1, 'auth0|638b682bbc99c67d7152083b', dollarToday)
        if (len(product_data)):
            dataR7.append(product_data)

    print("Almacenamiento completado")

    print("Iniciando almacenamiento en bd")

    print("Almacenando datos...")

    backurl = 'https://deploy-backendwww.onrender.com/api/item/create2'

    dataFull = dataR3[:10] + dataR5[:10] + dataR7[:10]
    #dataFull = dataR3[:1]
    res = requests.post(backurl, json = dataFull)
