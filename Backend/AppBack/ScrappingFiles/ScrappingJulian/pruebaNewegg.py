import requests
from bs4 import BeautifulSoup
import json
from .conversion_dolar import dolar_convert, getFecha

urls_newegg = {
    'RX500series' : { 'type': 3, 'link': 'https://www.newegg.com/p/pl?d=rx+500+series'},
    'RX5000series': {'type': 3, 'link': 'https://www.newegg.com/p/pl?d=rx+5000+series'},
    'RX6000series' : { 'type': 3, 'link': 'https://www.newegg.com/p/pl?d=rx+6000+series'},
    'RX7000series' : { 'type': 3, 'link': 'https://www.newegg.com/p/pl?d=radeon+rx+7000+series+amd&N=100006662'},
    'ddr4 crucial' : { 'type': 2, 'link': 'https://www.newegg.com/p/pl?d=16gb+ddr4+crucial'},
    'ddr4 hiperx' : { 'type': 2, 'link': 'https://www.newegg.com/p/pl?d=16gb+ddr4+hyperx'},
    'ddr4 kingston' : { 'type': 2, 'link': 'https://www.newegg.com/p/pl?d=16gb+ddr4+kingston'},
}

response = {
    "products" : []
}

## pesoCOP = dolar_convert() ## Descomentar en el caso de que se requiera hacer el scrappy muchas veces
def ScrappyEgg(urls):
    response['products'] = []
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Opera/73.0.3856.284',
        'Accept-Language': 'es-ES,es;q=0.9'
    }
    pesoCOP = dolar_convert()
    content = requests.get(urls['link'], headers = HEADER).text
    soup = BeautifulSoup(content, 'html.parser')
    LINK = soup.find_all('a', class_ = 'item-title')
    IMG = soup.find_all('a', class_ = 'item-img')
    NOMBRE = soup.find_all('a', class_ =  'item-title')
    PRECIO = soup.find_all('li', class_ = 'price-current')

    print('Numero de productos a buscar: ', len(LINK))
    ## Ingresamos a cada producto y sacamos su imagen, precio y nombre
    for i in range(len(LINK)):
        ## Ajuste de la moneda
        auxPrecio = PRECIO[i].strong.text + PRECIO[i].sup.text
        auxPrecio = auxPrecio.replace(',', '')

        try:
            auxPrecio = float(auxPrecio)
        except ValueError:
            continue


        response["products"].append({
            "item_picture": IMG[i].img['src'],
            "item_url": LINK[i]['href'],
            "item_name": NOMBRE[i].text,
            "item_price": int(pesoCOP*auxPrecio),
            'type_id' : urls['type'],
            'item_description': 'details',
            'user_id': 'auth0|639e3f6e9c43cd6f74e81ba0',
            'item_date': getFecha()

        })
    ## responseJson = json.dumps(response, indent = 4)
    ## print(responseJson, 'Num Productos: ', len(response["products"]))
    return response['products']