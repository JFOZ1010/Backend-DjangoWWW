from bs4 import BeautifulSoup
import requests
from datetime import date


def Walmart():

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Opera/93.0.4585.52',
        'Accept-Language': 'es-ES,es;q=0.9'
    }

    #BLOQUE DE CONVERSION DE DOLAR A PESOS#
    dolar = requests.get("https://www.google.com/search?q=dolar+a+cop&sourceid=chrome&ie=UTF-8", headers=header)
    contentDolar = dolar.text
    dolarsoup = BeautifulSoup(contentDolar,'html.parser')

    dolarPrice = dolarsoup.find_all('span', class_= 'DFlfde SwHCTb')

    auxdolar = dolarPrice[0].text

    auxdolar = auxdolar.replace('.','')
    auxdolar = auxdolar.replace(',','.')

    dolar = float(auxdolar)
    dolar = int(dolar)


    #print(dolar)

    #FIN DEL BLOQUE DE CONVERSION DE DOLAR A PESOS#

    #hacer scrapping a la pagina walmart y sacar los datos de los discos ssd
    url1 = 'https://www.walmart.com/search?q=disco+ssd+500'
    url2= 'https://www.walmart.com/search?q=disco+ssd+500&page=2&affinityOverride=default'
    r = requests.get(url1, headers=header)
    r2 = requests.get(url2, headers=header)
    r.status_code
    soup = BeautifulSoup(r.text, 'html.parser')
    soup2 = BeautifulSoup(r2.text, 'html.parser')

    # URLS
    urls = soup.find_all('div', {'class': 'sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity'})
    urls = [url.find('a', {'class': 'absolute w-100 h-100 z-1 hide-sibling-opacity'})['href'] for url in urls]
    #añadir la url base a cada url
    urls = ['https://www.walmart.com' + url for url in urls]
    #print("URLS 1: ", len(urls))

    urls2 = soup2.find_all('div', {'class': 'sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity'})
    urls2 = [url.find('a', {'class': 'absolute w-100 h-100 z-1 hide-sibling-opacity'})['href'] for url in urls2]
    #añadir la url base a cada url
    urls2 = ['https://www.walmart.com' + url for url in urls2]
    #print("URLS 2: ", len(urls2))

    # PRECIOS
    #preciosPage1 = soup.find_all('div',{'class': 'flex flex-wrap justify-start items-center lh-title mb2 mb1-m'})
    preciosPage1 = soup.find_all('div', {'class': 'mr1 mr2-xl b black lh-copy f5 f4-l'})
    preciosPage1 = [precio.text for precio in preciosPage1]
    #eliminar el simbolo de pesos
    preciosPage1 = [precio.replace('$', '') for precio in preciosPage1]
    # convertir a entero float los precios a peso colombiano
    preciosPage1 = [int(float(precio)) * dolar for precio in preciosPage1]

    preciosPage2 = soup2.find_all('div', {'class': 'mr1 mr2-xl b black lh-copy f5 f4-l'})
    preciosPage2 = [precio.text for precio in preciosPage2]
    #eliminar el simbolo de pesos
    preciosPage2 = [precio.replace('$', '') for precio in preciosPage2]
    # convertir a entero float los precios a peso colombiano
    preciosPage2 = [int(float(precio)) * dolar for precio in preciosPage2]
    #print("PRECIOS 2: ", len(preciosPage2))

    #precios de la segunda pagina a la primera, los dos primeros precios
    #preciosPage1.append(preciosPage2[0])
    #preciosPage1.append(preciosPage2[1])

    preciosPage1.extend(preciosPage2)
    #eliminando el ultimo precio, que no es de producto.
    preciosPage1.pop()

    #print("PRECIOS 1: ", len(preciosPage1)) 


    # TITULOS
    titulosPage1 = soup.find_all('a', {'class': 'absolute w-100 h-100 z-1 hide-sibling-opacity'})
    titulosPage1 = [titulo.find('span', {'class': 'w_iUH7'}).text for titulo in titulosPage1]
    #filtrar los titulos por los que contengan la palabra ssd
    titulosPage1 = [titulo for titulo in titulosPage1 if 'ssd' or 'gb' in titulo.lower()]
    #print("TITULOS 1: ", len(titulosPage1))

    titulosPage2 = soup2.find_all('a', {'class': 'absolute w-100 h-100 z-1 hide-sibling-opacity'})
    titulosPage2 = [titulo.find('span', {'class': 'w_iUH7'}).text for titulo in titulosPage2]
    #filtrar los titulos por los que contengan la palabra ssd
    titulosPage2 = [titulo for titulo in titulosPage2 if 'ssd' or 'gb' in titulo.lower()]
    #print("TITULOS 2: ", len(titulosPage2))


    # IMAGENES DE LOS DISCOS SSD
    imagenesPage1 = soup.find_all('div', {'class': 'relative overflow-hidden'})
    imagenesPage1 = [imagen.find('img', {'class': 'absolute top-0 left-0'})['src'] for imagen in imagenesPage1]
    #print("IMAGES 1: ", len(imagenesPage1))

    imagenesPage2 = soup2.find_all('div', {'class': 'relative overflow-hidden'})
    imagenesPage2 = [imagen.find('img', {'class': 'absolute top-0 left-0'})['src'] for imagen in imagenesPage2]
    #print("IMAGES 2: ", len(imagenesPage2))


    #UNIR TODOS LOS DATOS EN UN SOLO ARREGLO
    productos = [ ]

    for i in range(len(urls)):
        diccionarioProducto = {
            'type_id': 4, 
            'user_id': 'auth0|639e3ee1aacda0152647f763',
            'item_url': urls[i],
            'item_name': titulosPage1[i],
            'item_price': preciosPage1[i],
            'item_picture': imagenesPage1[i],
            'item_description': 'Description Generic', 
            'item_date': date.today().strftime('%Y-%m-%d') 
        } 
        productos.append(diccionarioProducto)

    url = 'http://127.0.0.1:6060/api/item/create2'
    x = requests.post(url, json = productos)


   
Walmart()