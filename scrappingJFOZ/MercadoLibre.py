#importar librerias beautifulsoup
from bs4 import BeautifulSoup
import requests
from datetime import date

def mercadoLibre():

    url = 'https://listado.mercadolibre.com.co/disco-ssd-500gb'
    r = requests.get(url)
    r.status_code
    # una variable que contenga el contenido de la pagina
    soup = BeautifulSoup(r.text, 'html.parser')


    #obtener los titulos de todos los discos ssd, que tienen un atributo ui-search-item
    titulos = soup.find_all('li', {'class': 'ui-search-layout__item shops__layout-item'})
    titulos = [titulo.text for titulo in titulos]
    #print(titulos)

    #Urls de todos los discos ssd, que tienen un atributo ui-search-item, de la primera pagina
    urls = soup.find_all('li', {'class': 'ui-search-layout__item shops__layout-item'})
    urls = [url.find('a', {'class': 'ui-search-link'}).get('href') for url in urls]
    #print(urls)

    #sacar el precio de todos los discos que tienen un atributo price-tag-fraction de la etiqueta span que están dentro de la etiqueta, span que tiene un atributo price-tag-amount, que está dentro de la etiqueta li que tiene un atributo ui-search-item
    precios = soup.find_all('li', {'class': 'ui-search-layout__item shops__layout-item'})
    precios = [precio.find('span', {'class': 'price-tag-amount'}).find('span', {'class': 'price-tag-fraction'}).text for precio in precios]
    precios = [int(precio.replace('.','')) for precio in precios] #convierto los precios a flotante. 
    #print(precios)

    # obtener los enlaces de las imagenes de los discos ssd que están dentro de una etiqueta li con atributo ui-search-layout__item shops__layout-item
    imagenes = soup.find_all('li', {'class': 'ui-search-layout__item shops__layout-item'}) 
    imagenes = [imagen.find('img', {'class': 'ui-search-result-image__element'}).get('data-src') for imagen in imagenes]
    #print(imagenes)

    productos = [ ]

    for i in range(len(urls)): 
        diccionarioProducto = {
            'type_id': 4,
            'user_id': 'auth0|639e3ee1aacda0152647f763',
            'item_name': titulos[i], 
            'item_price': precios[i],
            'item_url': urls[i],
            'item_picture': imagenes[i],
            'item_description': 'Detalle del producto', 
            'item_date': date.today().strftime('%Y-%m-%d') 
        }
        productos.append(diccionarioProducto)
    #print("Productos: ", productos)
    url = 'http://127.0.0.1:6060/api/item/create2'
    x = requests.post(url, json = productos)
    print(x.text)


    # auth0|638b682bbc99c67d7152083b
    #organizar los datos en un dataframe
    #df = pd.DataFrame({'Imagen': imagenes,'Titulo': titulos, 'Precio': precios, 'Url': urls})
    #print(df)

    #exportar todo el dataframe a una base de datos postgresql desplegada en render.com
    #database: proyect_www
    #juanfelipeoz
    #password: LBox2vyKMhOjkQ2bwtQMb60HJp8XFnIu
    #host: dpg-cdnrnmha6gdooi7cjf50-a.oregon-postgres.render.com
    #port: 5432
    #conexion1 = psycopg2.connect(database='proyect_www', user='juanfelipeoz', password='LBox2vyKMhOjkQ2bwtQMb60HJp8XFnIu', )

 
mercadoLibre()
