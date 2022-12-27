import requests
from bs4 import BeautifulSoup
from conversion_dolar import getFecha

urls_mercadoLibre = {
    'RX500series' : { 'type': 3, 'link': 'https://listado.mercadolibre.com.co/computacion/componentes-pc/tarjetas/tarjetas-video/radeon-rx-500-series/radeon-rx-500_NoIndex_True#applied_filter_id%3DSERIES%26applied_filter_name%3DSerie%26applied_filter_order%3D9%26applied_value_id%3D7038739%26applied_value_name%3DRadeon+RX+500+Series%26applied_value_order%3D1%26applied_value_results%3D163%26is_custom%3Dfalse'},
    'RX5000series' : { 'type': 3, 'link': 'https://listado.mercadolibre.com.co/computacion/componentes-pc/radeon-rx-5000_NoIndex_True#applied_filter_id%3Dcategory%26applied_filter_name%3DCategor%C3%ADas%26applied_filter_order%3D5%26applied_value_id%3DMCO441358%26applied_value_name%3DComponentes+de+PC%26applied_value_order%3D1%26applied_value_results%3D37%26is_custom%3Dfalse'},
    'RX6000series' : { 'type': 3, 'link': 'https://listado.mercadolibre.com.co/computacion/componentes-pc/tarjetas/tarjetas-video/radeon-rx-6000-series/radeon-rx-6000_NoIndex_True#applied_filter_id%3DSERIES%26applied_filter_name%3DSerie%26applied_filter_order%3D10%26applied_value_id%3D10150597%26applied_value_name%3DRadeon+RX+6000+Series%26applied_value_order%3D3%26applied_value_results%3D25%26is_custom%3Dfalse'},
    'RX7000series' : { 'type': 3, 'link': 'https://listado.mercadolibre.com.co/computacion/componentes-pc/tarjetas/tarjetas-video/radeon-rx-7000_NoIndex_True#D[A:radeon%20rx%207000,on]'},
    'ddr4 crucial' : { 'type': 2, 'link': 'https://listado.mercadolibre.com.co/16gb-ddr4-crucial#D[A:16gb%20ddr4%20crucial%20]'},
    'ddr4 hiperx' : { 'type': 2, 'link': 'https://listado.mercadolibre.com.co/16gb-ddr4-hiperx#D[A:16gb%20ddr4%20hiperx]'},
    'ddr4 kingston' : { 'type': 2, 'link': 'https://listado.mercadolibre.com.co/16gb-ddr4-kingston#D[A:16gb%20ddr4%20kingston]'},
}

response = {
    "products" : []
}


def ScrappyML(urls):
    content = requests.get(urls['link']).text
    soup = BeautifulSoup(content, 'html.parser')
    LINK = soup.find_all('a', class_ = "ui-search-item__group__element shops__items-group-details ui-search-link")
    ## Ingresamos a cada producto y sacamos su imagen, precio, y nombre
    for i in LINK:
        resultClicked = requests.get(i['href'])
        resultContent = resultClicked.text
        resultSoup = BeautifulSoup(resultContent, 'html.parser')
        IMG = resultSoup.find_all('img', class_ = 'ui-pdp-image ui-pdp-gallery__figure__image')
        NOMBRE = resultSoup.find_all('h1', class_ = 'ui-pdp-title')
        PRECIO = resultSoup.find_all('span', class_ = 'andes-money-amount__fraction')

        ## Ajuste de la moneda
        auxPrecio = PRECIO[0].text.replace('.', '')
        auxPrecio = float(auxPrecio)

        response["products"].append({
            "item_picture": IMG[0]['src'],
            "item_url": i['href'],
            "item_name": NOMBRE[0].text,
            "item_price": auxPrecio,
            "type_id" : urls['type'],
            'item_description': 'details',
            'user_id': 'auth0|639e3ee1aacda0152647f763',
            'item_date': getFecha()
        })
    ## responseJson = json.dumps(response, indent = 4)
    ## print(responseJson, 'Num productos: ', len(response["products"]))
    return response['products']