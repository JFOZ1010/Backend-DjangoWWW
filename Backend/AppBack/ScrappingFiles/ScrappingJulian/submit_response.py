import requests
from .pruebaMercadoLibre import ScrappyML, urls_mercadoLibre
from .pruebaAmazon import ScrappyAmzn, urls_amazon
from .pruebaNewegg import ScrappyEgg, urls_newegg

URL = 'http://127.0.0.1:6060/api/item/create2'

def amazonJulian():
    requests.post(URL, json = ScrappyAmzn(urls_amazon['RX500series']))
    requests.post(URL, json = ScrappyAmzn(urls_amazon['RX5000series']))
    requests.post(URL, json = ScrappyAmzn(urls_amazon['RX6000series']))
    requests.post(URL, json = ScrappyAmzn(urls_amazon['RX7000series']))
    requests.post(URL, json = ScrappyAmzn(urls_amazon['ddr4 crucial']))
    requests.post(URL, json = ScrappyAmzn(urls_amazon['ddr4 hiperx']))
    requests.post(URL, json = ScrappyAmzn(urls_amazon['ddr4 kingston']))

def mercadolibreJulian():
    requests.post(URL, json = ScrappyML(urls_mercadoLibre['RX500series']))
    requests.post(URL, json = ScrappyML(urls_mercadoLibre['RX5000series']))
    requests.post(URL, json = ScrappyML(urls_mercadoLibre['RX6000series']))
    requests.post(URL, json = ScrappyML(urls_mercadoLibre['RX7000series']))
    requests.post(URL, json = ScrappyML(urls_mercadoLibre['ddr4 crucial']))
    requests.post(URL, json = ScrappyML(urls_mercadoLibre['ddr4 hiperx']))
    requests.post(URL, json = ScrappyML(urls_mercadoLibre['ddr4 kingston']))

def neweggJulian():
    requests.post(URL, json = ScrappyEgg(urls_newegg['RX500series']))
    requests.post(URL, json = ScrappyEgg(urls_newegg['RX5000series']))
    requests.post(URL, json = ScrappyEgg(urls_newegg['RX6000series']))
    requests.post(URL, json = ScrappyEgg(urls_newegg['RX7000series']))
    requests.post(URL, json = ScrappyEgg(urls_newegg['ddr4 crucial']))
    requests.post(URL, json = ScrappyEgg(urls_newegg['ddr4 hiperx']))
    requests.post(URL, json = ScrappyEgg(urls_newegg['ddr4 kingston']))
