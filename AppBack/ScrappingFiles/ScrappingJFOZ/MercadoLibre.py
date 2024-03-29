#importar librerias beautifulsoup
from bs4 import BeautifulSoup
import requests
from datetime import date

#titulos añaden precios que no deberian ser. 
# y los precios de los items deben tomar solo el precio no el del descuento. 

def mercadoLibre():

    #url = 'https://listado.mercadolibre.com.co/disco-ssd-500gb'
    url = 'https://listado.mercadolibre.com.co/discos-500-gb-ssd#D[A:discos%20500%20gb%20ssd]'
    r = requests.get(url)
    r.status_code
    # una variable que contenga el contenido de la pagina
    soup = BeautifulSoup(r.text, 'html.parser')


    #obtener los titulos de todos los discos ssd, que tienen un atributo ui-search-item (TITULOS SIN PRECIOS EN EL TITULO)
    titulos = soup.find_all('a', {'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})
    titulos = [titulo.find('h2', {'class': 'ui-search-item__title shops__item-title'}).text for titulo in titulos]
    #titulos = [titulo.text for titulo in titulos]
    #print(titulos)

    #Urls de todos los discos ssd, que tienen un atributo ui-search-item, de la primera pagina
    urls = soup.find_all('li', {'class': 'ui-search-layout__item shops__layout-item'})
    urls = [url.find('a', {'class': 'ui-search-link'}).get('href') for url in urls]
    #print(urls)


    #PRECIOS
    precios = soup.find_all('span', {'class': 'price-tag ui-search-price__part shops__price-part'})
    precios = [precio.find('span', {'class': 'price-tag-fraction'}).text for precio in precios]
    #precios = soup.find_all('span', {'class': 'price-tag ui-search-price__part shops__price-part'})
    #precios = [precio.find('span', {'class': 'price-tag-fraction'}).text for precio in precios]
    #precios a flotantes los precios
    #precios = [float(precio.replace('.','')) for precio in precios] #convierto los precios a flotante. 
    precios = [int(precio.replace('.','')) for precio in precios]
    precios = [precio for precio in precios if int(precio) > 100000] #solo precios mayores a 100000 para filtrar los precios errados (de cuotas)
    print(f"precios {precios}")
    
    #IMAGENES
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
            'item_description': 'Felipe', 
            'item_date': date.today().strftime('%Y-%m-%d') 
        }
        productos.append(diccionarioProducto)
    #print("Productos: ", productos)
    url = 'https://deploy-backendwww.onrender.com/api/item/create2'
    x = requests.post(url, json = productos)
    #print(x.text)

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
