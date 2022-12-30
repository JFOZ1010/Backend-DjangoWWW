import requests
from bs4 import BeautifulSoup
from .conversion_dolar import dolar_convert, getFecha
import json

urls_amazon = {
    'RX500series' : { 'type': 3, 'link': 'https://www.amazon.com/s?k=radeon+rx+500+series&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1ZGZT1NJVU8XJ&sprefix=radeon+rx+500+serie%2Caps%2C152&ref=nb_sb_noss_2'},
    'RX5000series' : { 'type': 3, 'link': 'https://www.amazon.com/s?k=radeon+rx+5000+series&rh=n%3A284822%2Cp_n_feature_browse-bin%3A23883927011&dc&language=es&ds=v1%3AsSP%2FyIXWZCKFxLC%2FkoSrk%2FmFbrzY7vrtnOg54TD%2FBhY&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1AR5RLOWCOMPO&qid=1671679777&rnid=23883919011&sprefix=radeon+rx+5000+series%2Caps%2C151&ref=sr_nr_p_n_feature_browse-bin_1'},
    'RX6000series' : { 'type': 3, 'link': 'https://www.amazon.com/s?k=radeon+rx+6000+series&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1J4G59CZU3KZA&sprefix=radeon+rx+6000+serie%2Caps%2C161&ref=nb_sb_noss_2'},
    'RX7000series' : { 'type': 3, 'link': 'https://www.amazon.com/s?k=radeon+rx+7000+series&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=15FRDG1GA84BS&sprefix=radeon+rx+7000+series%2Caps%2C224&ref=nb_sb_noss_1'},
    'ddr4 crucial' : { 'type': 2, 'link': 'https://www.amazon.com/s?k=16gb+drr4+crucial&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2X5P790UZ3R50&sprefix=16gb+drr4+crucial%2Caps%2C172&ref=nb_sb_noss'},
    'ddr4 hiperx' : { 'type': 2, 'link': 'https://www.amazon.com/s?k=16gb+drr4+hyper+x&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2RDVGIF7ZPV1O&sprefix=16gb+drr4+hyper+x%2Caps%2C185&ref=nb_sb_noss'},
    'ddr4 kingston' : { 'type': 2, 'link': 'https://www.amazon.com/s?k=16gb+drr4+kingston&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3FMC8ODCD6FMW&sprefix=16gb+drr4+kingston%2Caps%2C149&ref=nb_sb_noss'},
}

response = {
    "products" : []
}

## pesoCOP = dolar_convert() ## Descomentar en el caso de que se requiera hacer el scrappy muchas veces
def ScrappyAmzn(urls):
    response['products'] = []
    ## print('Buscamos en Amazon:', urls)
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Opera/73.0.3856.284',
        'Accept-Language': 'es-ES,es;q=0.9'
    }
    pesoCOP = dolar_convert()
    content = requests.get(urls['link'], headers = HEADER).text
    soup = BeautifulSoup(content, 'html.parser')
    LINK = soup.find_all('a', class_ = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    NOMBRE = soup.find_all('span', class_ = 'a-size-medium a-color-base a-text-normal')
    print('Numero de productos a buscar: ', len(LINK))

    for i in range(0, 10, 1):
        try:
            innerResult = requests.get('https://www.amazon.com' + LINK[i]['href'], headers = HEADER)
        except Exception:
            continue

        innerContent = innerResult.text
        innerSoup = BeautifulSoup(innerContent, 'html.parser')
        PRECIO = innerSoup.find_all('span', class_ = 'a-offscreen')

        ## Ajuste de moneda
        auxPrecio = PRECIO[0].text[3:]
        auxPrecio = auxPrecio.replace(',', '')

        try:
            auxPrecio = float(auxPrecio)
        except ValueError:
            continue
        IMG = innerSoup.find_all('img', class_='a-dynamic-image')

        response['products'].append({
            'item_name' : NOMBRE[i].text,
            'item_price' : int(auxPrecio * pesoCOP),
            'item_url':  'https://www.amazon.com'+LINK[i]['href'],
            'item_picture': IMG[0]['src'],
            'item_description': 'Julian',
            'user_id' : "auth0|638b682bbc99c67d7152083b",
            "type_id": urls['type'],
            'item_date' : getFecha()

        })

    #print(json.dumps(response, indent = 4))
    return response['products']