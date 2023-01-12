import requests
from .pruebaMercadoLibre import ScrappyML, urls_mercadoLibre
from .pruebaAmazon import ScrappyAmzn, urls_amazon
from .pruebaNewegg import ScrappyEgg, urls_newegg

URL = 'https://deploy-backendwww.onrender.com/api/item/create2'

## AMAZON
def doAmazonGPU():
    print('Iniciando Amazon...')
    resultadosAmazon = ScrappyAmzn(urls_amazon['RX500series']) + ScrappyAmzn(urls_amazon['RX5000series']) + ScrappyAmzn(urls_amazon['RX6000series']) + ScrappyAmzn(urls_amazon['RX7000series'])
    requests.post(URL, json = resultadosAmazon)
    #print(len(resultadosAmazon))
    ## return resultadosAmazon

def doMercadoLibreGPU():
    print('Iniciando Mercado Libre...')
    resultadosML = ScrappyML(urls_mercadoLibre['RX500series']) + ScrappyML(urls_mercadoLibre['RX5000series']) +  ScrappyML(urls_mercadoLibre['RX6000series']) + ScrappyML(urls_mercadoLibre['RX7000series'])
    requests.post(URL, json = resultadosML)
    print('Se han subido los datos de GPU de ML')
    ## return resultadosML

def doNewEggGPU():
    print('Iniciando NewEgg...')
    resultadosNew = ScrappyEgg(urls_newegg['RX500series']) + ScrappyEgg(urls_newegg['RX5000series']) + ScrappyEgg(urls_newegg['RX6000series']) + ScrappyEgg(urls_newegg['RX7000series'])
    requests.post(URL, json = resultadosNew)
    print('Se han subido los datos de GPU de New')

def doAmazonRAM():
    print('Iniciando Amazon...')
    resultadosAmazon =ScrappyAmzn(urls_amazon['ddr4 crucial']) + ScrappyAmzn(urls_amazon['ddr4 hiperx']) + ScrappyAmzn(urls_amazon['ddr4 kingston'])
    requests.post(URL, json = resultadosAmazon)
    print('Se han subido los datos de RAM de Amzn')

def doMercadoLibreRAM():
    print('Iniciando ML...')
    resultadosML =  ScrappyML(urls_mercadoLibre['ddr4 crucial']) + ScrappyML(urls_mercadoLibre['ddr4 hiperx']) + ScrappyML(urls_mercadoLibre['ddr4 kingston'])
    requests.post(URL, json = resultadosML)
    print('Se han subido los datos de ram de ML')

def doNewEggRAM():
    print('Iniciando New...')
    resultadosNew = ScrappyEgg(urls_newegg['ddr4 crucial']) + ScrappyEgg(urls_newegg['ddr4 hiperx']) + ScrappyEgg(urls_newegg['ddr4 kingston'])
    requests.post(URL, json = resultadosNew)
    print('Se han subido los datos de ram de New')


'''
x = requests.post(URL, json = ScrappyML(urls_mercadoLibre['RX500series']))
x = requests.post(URL, json = ScrappyML(urls_mercadoLibre['RX5000series']))
x = requests.post(URL, json = ScrappyML(urls_mercadoLibre['RX6000series']))
x = requests.post(URL, json = ScrappyML(urls_mercadoLibre['RX7000series']))
x = requests.post(URL, json = ScrappyML(urls_mercadoLibre['ddr4 crucial']))
x = requests.post(URL, json = ScrappyML(urls_mercadoLibre['ddr4 hiperx']))
x = requests.post(URL, json = ScrappyML(urls_mercadoLibre['ddr4 kingston']))
x = requests.post(URL, json = ScrappyAmzn(urls_amazon['RX500series']))
x = requests.post(URL, json = ScrappyAmzn(urls_amazon['RX5000series']))
x = requests.post(URL, json = ScrappyAmzn(urls_amazon['RX6000series']))
x = requests.post(URL, json = ScrappyAmzn(urls_amazon['RX7000series']))
x = requests.post(URL, json = ScrappyAmzn(urls_amazon['ddr4 crucial']))
x = requests.post(URL, json = ScrappyAmzn(urls_amazon['ddr4 hiperx']))
x = requests.post(URL, json = ScrappyAmzn(urls_amazon['ddr4 kingston']))
x = requests.post(URL, json = ScrappyEgg(urls_newegg['RX500series']))
x = requests.post(URL, json = ScrappyEgg(urls_newegg['RX5000series']))
x = requests.post(URL, json = ScrappyEgg(urls_newegg['RX6000series']))
x = requests.post(URL, json = ScrappyEgg(urls_newegg['RX7000series']))
x = requests.post(URL, json = ScrappyEgg(urls_newegg['ddr4 crucial']))
x = requests.post(URL, json = ScrappyEgg(urls_newegg['ddr4 hiperx']))
x = requests.post(URL, json = ScrappyEgg(urls_newegg['ddr4 kingston']))
'''
## print(x.text)