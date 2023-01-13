import requests
from bs4 import BeautifulSoup
import json
from datetime import date

def parseInfoMercadolibre(producto, type_id, user_id):
    enlace = producto.find(class_ = 'ui-search-item__group__element shops__items-group-details ui-search-link')
    nombre = producto.find(class_ = 'ui-search-item__title shops__item-title')
    precio = producto.find('div', {'class' : 'ui-search-price__second-line shops__price-second-line'} )
    precio = precio.find(class_ = 'price-tag-fraction')
    imagen = producto.find(class_ = 'slick-slide slick-active')
    product_data = {
        "item_name" : " ".join(nombre.text.split()),
        "item_price" : int(precio.text.replace('.', '')),
        "item_picture" : str(imagen.img['data-src']),
        "item_description" : "Kevin",
        "item_url" : str(enlace['href']),
        "type_id" : type_id,
        "user_id" : user_id,
        "item_date": date.today().strftime("%Y-%m-%d")
    }
    return product_data


def mercadolibre():
    
    print("Obteniendo información de mercadolibre Ryzen 3...")
    urlR3 = 'https://listado.mercadolibre.com.co/computacion/componentes-pc/procesador-ryzen-3_LINE_1260236_NoIndex_True#applied_filter_id%3DLINE%26applied_filter_name%3DL%C3%ADnea%26applied_filter_order%3D17%26applied_value_id%3D1260236%26applied_value_name%3DRyzen+3%26applied_value_order%3D1%26applied_value_results%3D56%26is_custom%3Dfalse'
    mercadolibreR3 = requests.get(urlR3)
    soupR3 = BeautifulSoup(mercadolibreR3.text, 'html.parser')

    print("Obteniendo información de mercadolibre Ryzen 5...")
    urlR5 = 'https://listado.mercadolibre.com.co/computacion/componentes-pc/procesador-ryzen-5_LINE_2244215_NoIndex_True#applied_filter_id%3DLINE%26applied_filter_name%3DL%C3%ADnea%26applied_filter_order%3D18%26applied_value_id%3D2244215%26applied_value_name%3DRyzen+5%26applied_value_order%3D4%26applied_value_results%3D245%26is_custom%3Dfalse'
    mercadolibreR5 = requests.get(urlR5)
    soupR5 = BeautifulSoup(mercadolibreR5.text, 'html.parser')

    print("Obteniendo información de mercadolibre Ryzen 7...")
    urlR7 = 'https://listado.mercadolibre.com.co/computacion/componentes-pc/procesador-ryzen-7_LINE_968657_NoIndex_True#applied_filter_id%3DLINE%26applied_filter_name%3DL%C3%ADnea%26applied_filter_order%3D18%26applied_value_id%3D968657%26applied_value_name%3DRyzen+7%26applied_value_order%3D7%26applied_value_results%3D114%26is_custom%3Dfalse'
    mercadolibreR7 = requests.get(urlR7)
    soupR7 = BeautifulSoup(mercadolibreR7.text, 'html.parser')
    

    listaProductosR3 = soupR3.find_all('li', {'class': 'ui-search-layout__item shops__layout-item'})
    listaProductosR5 = soupR5.find_all('li', {'class': 'ui-search-layout__item shops__layout-item'})
    listaProductosR7 = soupR7.find_all('li', {'class': 'ui-search-layout__item shops__layout-item'})
    dataR3 = []
    dataR5 = []
    dataR7 = []

    print("Parseando elementos de Ryzen 3...")
    for producto in listaProductosR3:
        product_data = parseInfoMercadolibre(producto,1, 'auth0|639e3ee1aacda0152647f763')
        dataR3.append(product_data)

    print("Parseando elementos de Ryzen 5...")
    for producto in listaProductosR5:
        product_data = parseInfoMercadolibre(producto,1, 'auth0|639e3ee1aacda0152647f763')
        dataR5.append(product_data)
    
    print("Parseando elementos de Ryzen 7...")
    for producto in listaProductosR7:
        product_data = parseInfoMercadolibre(producto,1, 'auth0|639e3ee1aacda0152647f763')
        dataR7.append(product_data)

    print("Almacenamiento completado")

    print("Iniciando almacenamiento en bd")

    print("Almacenando datos...")

    backurl = 'http://127.0.0.1:6060/api/item/create2'

    dataFull = dataR3[:10] + dataR5[:10] + dataR7[:10]
    #dataFull = dataFull[:1]
    res = requests.post(backurl, json = dataFull)

    #print(len(dataR3))
    #print(len(dataR5))
    #print(len(dataR7))
    #print (json.dumps(dataR3[0], indent=2, default=str))
    #print (json.dumps(dataR5[0], indent=2, default=str))
    #print (json.dumps(dataR7[0], indent=2, default=str))


