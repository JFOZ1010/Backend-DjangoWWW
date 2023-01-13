import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
from datetime import date

def scrapMercadoLibre(url,typeId):
    #print(url)

    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')

    mlresponse = {
        "products": [
        ]
    }

    names = soup.find_all(
        'h2', class_='ui-search-item__title shops__item-title')
    urls = soup.find_all(
        'a', class_='ui-search-item__group__element shops__items-group-details ui-search-link')

    for i in range(0, 10, 1):
        try:
            innerResult = requests.get(urls[i]['href'])
        except Exception:
            continue

        innerContent = innerResult.text
        innerSoup = BeautifulSoup(innerContent, 'html.parser')
        img = innerSoup.find_all(
            'img', class_='ui-pdp-image ui-pdp-gallery__figure__image')
        price = innerSoup.find_all('div', class_='ui-pdp-price__second-line')

        if(len(price) == 0):
            #print(price)
            continue

        mlresponse["products"].append({
            "item_name": names[i].text,
            "item_price": int(price[0].text.split(' ')[0]),
            "item_url": urls[i]['href'],
            "item_picture": img[0]['src'],
            "item_description" : "Giron",
            "user_id":"auth0|639e3ee1aacda0152647f763",
            "type_id":typeId,
            'item_date': date.today().strftime('%Y-%m-%d') 

        })

    mlResponseJson = json.dumps(mlresponse, indent=4)

    return mlresponse['products']

    #print(mlResponseJson)


def scrapMLGiron():
    #Peticion de memorias RAM 8 GB RAM las tres marcas
    hyperx = scrapMercadoLibre('https://listado.mercadolibre.com.co/computacion/componentes-pc/memoria-ram-ddr4-8gb-hyperx_BRAND_448156_NoIndex_True#unapplied_filter_id=MEMORY_TECHNOLOGY%26unapplied_filter_name=Tecnolog%C3%ADa+de+la+memoria%26unapplied_value_id=2569307%26unapplied_value_name=DDR4%26unapplied_autoselect=false',2)
    crucial = scrapMercadoLibre('https://listado.mercadolibre.com.co/memoria-ram-ddr4-8gb-crucial#D[A:memoria%20ram%20ddr4%208gb%20%20crucial]',2)
    kingston = scrapMercadoLibre('https://listado.mercadolibre.com.co/computacion/componentes-pc/memorias-ram/kingston/memoria-ram-ddr4-8gb-kingston_NoIndex_True#applied_filter_id=BRAND%26applied_filter_name=Marca%26applied_filter_order=9%26applied_value_id=16360%26applied_value_name=Kingston%26applied_value_order=2%26applied_value_results=104%26is_custom=false',2)

    #Peticion de memorias Graficas Nvidia

    rtx30 = scrapMercadoLibre('https://listado.mercadolibre.com.co/computacion/componentes-pc/tarjetas/tarjetas-video/geforce-rtx-30-series/nvidia-rtx_NoIndex_True#applied_filter_id=SERIES%26applied_filter_name=Serie%26applied_filter_order=10%26applied_value_id=8958078%26applied_value_name=GeForce+RTX+30+Series%26applied_value_order=4%26applied_value_results=320%26is_custom=false',3)
    rtx20 = scrapMercadoLibre('https://listado.mercadolibre.com.co/computacion/componentes-pc/tarjetas/tarjetas-video/geforce-rtx-20-series/nvidia-rtx_NoIndex_True#applied_filter_id=SERIES%26applied_filter_name=Serie%26applied_filter_order=10%26applied_value_id=7043881%26applied_value_name=GeForce+RTX+20+Series%26applied_value_order=3%26applied_value_results=77%26is_custom=false',3)
    gtx16 = scrapMercadoLibre('https://listado.mercadolibre.com.co/computacion/componentes-pc/tarjetas/tarjetas-video/geforce-gtx-16-series/nvidia-gtx_NoIndex_True#applied_filter_id=SERIES%26applied_filter_name=Serie%26applied_filter_order=10%26applied_value_id=7045001%26applied_value_name=GeForce+GTX+16+Series%26applied_value_order=4%26applied_value_results=406%26is_custom=false',3)

    ##SUBMIT##

    URL = 'http://127.0.0.1:6060/api/item/create2'

    submit = requests.post(URL,json = hyperx)
    print("HyperX enviado")

    submit = requests.post(URL,json = crucial)
    print("Crucial enviado")

    submit = requests.post(URL,json = kingston)
    print("Kingston enviado")

    submit = requests.post(URL,json = rtx30)
    print("RTX30 enviado")

    submit = requests.post(URL,json = rtx20)
    print("RTX20 enviado")

    submit = requests.post(URL,json = gtx16)
    print("GTX16 enviado")