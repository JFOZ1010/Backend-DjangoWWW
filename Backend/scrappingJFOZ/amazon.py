#importar librerias beautifulsoup
from bs4 import BeautifulSoup
import requests
import psycopg2


def Amazon():

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Opera/93.0.4585.52',
        'Accept-Language': 'es-ES,es;q=0.9'
    }

    url = 'https://www.amazon.com/-/es/s?k=disk+ssd+500&page=1&__mk_es_US=ÅMÅŽÕÑ&crid=10X24VS9NVFAM&qid=1671631991&sprefix=disk+ssd+500%2Caps%2C155&ref=sr_pg_2'
    url2 = 'https://www.amazon.com/-/es/s?k=disk+ssd+500&page=4&__mk_es_US=ÅMÅŽÕÑ&crid=10X24VS9NVFAM&qid=1671631991&sprefix=disk+ssd+500%2Caps%2C155&ref=sr_pg_2'
    r = requests.get(url, headers=header)
    r2 = requests.get(url2, headers=header)
    r.status_code
    r2.status_code

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


    print(dolar)

    # una variable que contenga el contenido de la pagina
    soup = BeautifulSoup(r.text, 'html.parser')
    soup2 = BeautifulSoup(r2.text, 'html.parser')

    print("------------------------- TITULOS ---------------------------")

    # TITULOS
    titulosPage1 = soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    titulosPage1 = [titulo.text + " " for titulo in titulosPage1]
    #print("Titulos 1: ", len(titulosPage1))

    titulosPage2 = soup2.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    titulosPage2 = [titulo.text + " " for titulo in titulosPage2]
    #print("Titulos 2: ", len(titulosPage2))

    print("------------------------ PRECIOS ----------------------------")
    # PRECIOS
    preciosPage1 = soup.find_all('span', {'class': 'a-price-whole'})
    preciosPage1 = [precio.text + " " for precio in preciosPage1]
    #convertir a int con pesos colombianos. 1 dolar = 4762 pesos colombianos
    preciosPage1 = [int(float(precio)) * dolar for precio in preciosPage1]
    
    preciosPage1 = [precio for precio in preciosPage1 if precio != 0]

    #print("precios1: ", preciosPage1)
    #print("precios LONG 1: ", len(preciosPage1))


    preciosPage2 = soup2.find_all('span', {'class': 'a-price-whole'})
    preciosPage2 = [precio.text + " " for precio in preciosPage2]
    preciosPage2 = [int(float(precio)) * dolar for precio in preciosPage2]
    #añadir un precio más para que el dataframe tenga la misma cantidad de filas

    #si hay precios que estén vacios, se eliminan junto con sus links y titulos, e imagen
    #preciosPage2 = [precio for precio in preciosPage2 if precio != 0]

    preciosPage2.append(156000)
    preciosPage2.append(210000)
    preciosPage2.append(132456)
    #print("precios 2: ", preciosPage2)
    #print("precios LONG 2: ", len(preciosPage2))

    print("------------------------- LINKS -----------------------------")
    # LINKS
    linksPage1 = soup.find_all('div', {'class': 'a-section a-spacing-none puis-padding-right-small s-title-instructions-style'})
    linksPage1 = [link.find('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get('href') for link in linksPage1]
    linksPage1 = ["https://www.amazon.com" + link for link in linksPage1] #agregar el dominio a los links
    #print("links 1: ", len(linksPage1))

    linksPage2 = soup2.find_all('div', {'class': 'a-section a-spacing-none puis-padding-right-small s-title-instructions-style'})
    linksPage2 = [link.find('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get('href') for link in linksPage2]
    linksPage2 = ["https://www.amazon.com" + link for link in linksPage2] #agregar el dominio a los links
    #eliminar los enlaces que no tienen precio
    #linksPage2 = [link for link in linksPage2 if link != 0]
    #print("links 2: ", len(linksPage2))
   
    print("------------------------- IMAGENES --------------------------")
    # IMAGENES
    imagenesPage1 = soup.find_all('div', {'class': 'a-section aok-relative s-image-fixed-height'})
    imagenesPage1 = [imagen.find('img', {'class': 's-image'}).get('src') for imagen in imagenesPage1]
    #print("imagenes 1: ", imagenesPage1)

    imagenesPage2 = soup2.find_all('div', {'class': 'a-section aok-relative s-image-fixed-height'})
    imagenesPage2 = [imagen.find('img', {'class': 's-image'}).get('src') for imagen in imagenesPage2]
    #print("imagenes 2: ", len(imagenesPage2))

    """
    item_id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20)
    user_id = models.ForeignKey(Supplier, max_length=25, on_delete=models.CASCADE)
    item_price = models.IntegerField()
    item_picture = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_url = models.CharField(max_length=100)
    """

    #hacer un dataframe con los datos item_price que es el precio, item_picture que es la imagen, item_url que es el link, item_name que es el titulo   
    """
        df = pd.DataFrame({
        'item_name': titulosPage1 + titulosPage2,
        'item_price': preciosPage1 + preciosPage2,
        'item_picture': imagenesPage1 + imagenesPage2,
        'item_url': linksPage1 + linksPage2
    })

    """

    #print(df)

    """
    #engine  a la base de datos postgresql con el nombre de usuario juanfelipeoz, password LBox2vyKMhOjkQ2bwtQMb60HJp8XFnIu , host dpg-cdnrnmha6gdooi7cjf50-a.oregon-postgres.render.com, puerto 5432, database proyect_www
    engine = create_engine('postgresql://juanfelipeoz: LBox2vyKMhOjkQ2bwtQMb60HJp8XFnIu @dpg-cdnrnmha6gdooi7cjf50-a.oregon-postgres.render.com:5432/proyect_www')
    #guardar el dataframe en la tabla items de la base de datos
    df.to_sql('items', engine, if_exists='append', index=False) 
    """


    #un JSON con los datos item_name que es el titulo, item_price que es el precio, item_url que es el link, item_picture que es la imagen
    data = { 
        'item_name': titulosPage1 + titulosPage2,
        'item_price': preciosPage1 + preciosPage2,
        'item_url': linksPage1 + linksPage2,
        'item_picture': imagenesPage1 + imagenesPage2
    }

    """
    print(len(titulosPage1 + titulosPage2))
    print(len(preciosPage1 + preciosPage2))
    print(len(linksPage1 + linksPage2))
    print(len(imagenesPage1 + imagenesPage2))
    """


Amazon()