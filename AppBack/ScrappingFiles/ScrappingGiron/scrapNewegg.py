import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
from datetime import date


def scrapNewegg(url,typeId):
    #print(url)
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Opera/73.0.3856.284',
        'Accept-Language': 'es-ES,es;q=0.9'
    }
    result = requests.get(url, headers=HEADER)
    content = result.text
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')

    mlresponse = {
        "products": [
        ]
    }

    namesUrl = soup.find_all(
        'a', class_='item-title')


    #BLOQUE DE CONVERSION DE DOLAR A PESOS#
    dolar = requests.get("https://www.google.com/search?q=dolar+a+cop&sourceid=chrome&ie=UTF-8", headers=HEADER)
    contentDolar = dolar.text
    dolarsoup = BeautifulSoup(contentDolar,'html.parser')

    dolarPrice = dolarsoup.find_all('span', class_= 'DFlfde SwHCTb')

    auxdolar = dolarPrice[0].text

    auxdolar = auxdolar.replace('.','')
    auxdolar = auxdolar.replace(',','.')

    dolar = float(auxdolar)
    #print(dolar)
    #FIN DEL BLOQUE DE CONVERSION DE DOLAR A PESOS#
    print(len(namesUrl))
    for i in range(0, 10, 1):
        try:
            innerResult = requests.get(namesUrl[i]['href'], headers=HEADER)
        except Exception:
            continue

        innerContent = innerResult.text
        innerSoup = BeautifulSoup(innerContent, 'html.parser')
        
        price = innerSoup.find_all('li', class_='price-current')

        if(price[0].text==''):
            continue

        auxPrice = price[0].text
        auxPrice = auxPrice.replace(',','')
        #print(auxPrice)

        img = innerSoup.find_all('img', class_='product-view-img-original')

        mlresponse["products"].append({
            "item_name": namesUrl[i].text,
            "item_price": int(float(auxPrice[1:]) * dolar),
            "item_url": namesUrl[i]['href'],
            "item_picture": img[0]['src'],
            "item_description" : "Giron",
            "user_id":"auth0|639e3f6e9c43cd6f74e81ba0",
            "type_id":typeId,
            'item_date': date.today().strftime('%Y-%m-%d') 
        })

    mlResponseJson = json.dumps(mlresponse, indent=4)

    return mlresponse['products']
    
    #print(mlResponseJson)



def scrapNeweggGiron():

    #MEMORIAS RAM CRUCIAL
    hyperx = scrapNewegg('https://www.newegg.com/p/pl?N=500000512%20600561665%20100007611%2050001455&d=crucial+memory+ram',2)

    # #MEMORIAS RAM HYPERX
    crucial = scrapNewegg('https://www.newegg.com/p/pl?N=600561665%20100007611%2050011776%20500000512&d=memory+ram',2)

    # #MEMORIAS RAM KINGSTON
    kingston = scrapNewegg('https://www.newegg.com/p/pl?d=memory+ram&N=50001183%20600561665%20100007611',2)

    # #TARJETAS GRAFICAS SERIE RTX30
    rtx30 = scrapNewegg('https://www.newegg.com/p/pl?d=GPU&N=50001441%20601357282%20100007709',3)

    # #TARJETAS GRAFICAS SERIE RTX20
    rtx20 = scrapNewegg('https://www.newegg.com/p/pl?N=50001441%20100007709%20601321572&d=GPU',3)

    # #TARJETAS GRAFICAS SERIE GTX16
    gtx16 = scrapNewegg('https://www.newegg.com/p/pl?N=100007709%20601331379&d=GPU+NVIDIA',3)


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