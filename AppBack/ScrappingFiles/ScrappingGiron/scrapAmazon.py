import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
from datetime import date


def scrapAmazon(url,typeId):
    #print(url)
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Opera/73.0.3856.284',
        'Accept-Language': 'es-ES,es;q=0.9'
    }
    result = requests.get(url, headers=HEADER)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')

    mlresponse = {
        "products": [
        ]
    }

    names = soup.find_all(
        'span', class_='a-size-medium a-color-base a-text-normal')
    urls = soup.find_all(
        'a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')

    #BLOQUE DE CONVERSION DE DOLAR A PESOS#
    dolar = requests.get("https://www.google.com/search?q=dolar+a+cop&sourceid=chrome&ie=UTF-8", headers=HEADER)
    contentDolar = dolar.text
    dolarsoup = BeautifulSoup(contentDolar,'html.parser')

    dolarPrice = dolarsoup.find_all('span', class_= 'DFlfde SwHCTb')

    auxdolar = dolarPrice[0].text

    auxdolar = auxdolar.replace('.','')
    auxdolar = auxdolar.replace(',','.')

    dolar = float(auxdolar)

    print(dolar)

    #FIN DEL BLOQUE DE CONVERSION DE DOLAR A PESOS#
    print(len(urls))
    for i in range(0, 10, 1):
        try:
            innerResult = requests.get('https://www.amazon.com'+urls[i]['href'], headers=HEADER)
        except Exception:
            continue

        innerContent = innerResult.text
        innerSoup = BeautifulSoup(innerContent, 'html.parser')
        price = innerSoup.find_all('span', class_='a-offscreen')

        # Acomodamos la moneda
        auxPrice = price[0].text[3:]
        auxPrice = auxPrice.replace(',', '')

        try:
            auxPrice = float(auxPrice)
        except ValueError:
            continue

        img = innerSoup.find_all(
            'img', class_='a-dynamic-image')

        mlresponse["products"].append({
            "item_name": names[i].text,
            "item_price": int(auxPrice * dolar),
            "item_url": 'https://www.amazon.com'+urls[i]['href'],
            "item_picture": img[0]['src'],
            "item_description" : "Giron",
            "user_id":"auth0|638b682bbc99c67d7152083b",
            "type_id":typeId,
            'item_date': date.today().strftime('%Y-%m-%d') 
        })

    mlResponseJson = json.dumps(mlresponse, indent=4)

    return mlresponse['products']

    #print(mlResponseJson)

def scrapAmazonGiron():
    #MEMORIAS RAM CRUCIAL
    crucial = scrapAmazon('https://www.amazon.com/s?k=memoria+ram+ddr4+8gb&i=electronics&rh=n%3A172500%2Cp_89%3ACrucial%2Cp_n_feature_five_browse-bin%3A677427011&dc&language=es&ds=v1%3AsyEVmcL0wsjBkvhpPop%2Bbf3bwXrxlDvP4%2BuixOIAi5M&crid=3U2SXGALCNWVS&qid=1671655664&rnid=673240011&sprefix=memoria+ram+%2Caps%2C443&ref=sr_nr_p_n_feature_five_browse-bin_6',2)

    #MEMORIAS RAM HYPERX
    hyperx = scrapAmazon('https://www.amazon.com/s?k=memoria+ram+ddr4+8gb+hyper+x&i=computers&rh=n%3A172500%2Cp_89%3AHyperX&dc&language=es&ds=v1%3ADbtkK6YYgFHw0%2BvvH7wogu%2FVoq1L4qh%2B38yoRQtd4JE&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1671656737&rnid=2528832011&ref=sr_nr_p_89_6',2)

    #MEMORIAS RAM KINGSTON
    kingston = scrapAmazon('https://www.amazon.com/-/es/s?k=memoria+ram+ddr4+8gb&i=electronics&bbn=172500&rh=n%3A172500%2Cp_n_feature_five_browse-bin%3A677427011%2Cp_89%3AKingston&dc&language=es&crid=3U2SXGALCNWVS&qid=1671656679&rnid=2528832011&sprefix=memoria+ram+%2Caps%2C443&ref=sr_nr_p_89_1&ds=v1%3ATIiQ0lJwyEtH3Ds6Ww91Nd2YWUc%2FW2g0eprMjmgj778',2)

    #TARJETAS GRAFICAS SERIE RTX30
    rtx30 =scrapAmazon('https://www.amazon.com/s?k=GPU+NVIDIA+RTX+SERIE+30&rh=n%3A284822&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss',3)




    #SUBMIT
    URL = 'https://deploy-backendwww.onrender.com/api/item/create2'

    submit = requests.post(URL,json = hyperx)
    print("HyperX enviado")

    submit = requests.post(URL,json = crucial)
    print("Crucial enviado")

    submit = requests.post(URL,json = kingston)
    print("Kingston enviado")

    submit = requests.post(URL,json = rtx30)
    print("RTX30 enviado")