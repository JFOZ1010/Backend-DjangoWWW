import requests
from bs4 import BeautifulSoup
from datetime import date

####Scrapping de mercadolibre para intel core i3, i5 e i7:

##Método que escarba los procesadores intel desde mercadolibre, recibe un entero donde 0=core i3, 1=core i5 y 2=core i7
def ScrapProcessorsML(reference):
  if(reference==0):
    url='https://listado.mercadolibre.com.co/computacion/componentes-pc/procesadores/nuevo/procesador-intel-core-i3_NoIndex_True#applied_filter_id%3Dcategory%26applied_filter_name%3DCategor%C3%ADas%26applied_filter_order%3D2%26applied_value_id%3DMCO1693%26applied_value_name%3DProcesadores%26applied_value_order%3D2%26applied_value_results%3D98%26is_custom%3Dfalse'
  elif (reference==1):
    url='https://listado.mercadolibre.com.co/computacion/componentes-pc/procesadores/core-i5/nuevo/procesador-intel-core-i5_NoIndex_True#applied_filter_id%3DLINE%26applied_filter_name%3DL%C3%ADnea%26applied_filter_order%3D4%26applied_value_id%3D7769178%26applied_value_name%3DCore+i5%26applied_value_order%3D2%26applied_value_results%3D121%26is_custom%3Dfalse'
  else:
    url='https://listado.mercadolibre.com.co/computacion/componentes-pc/procesadores/core-i7/nuevo/procesador-intel-core-i7_NoIndex_True#applied_filter_id%3DLINE%26applied_filter_name%3DL%C3%ADnea%26applied_filter_order%3D2%26applied_value_id%3D7769180%26applied_value_name%3DCore+i7%26applied_value_order%3D2%26applied_value_results%3D82%26is_custom%3Dfalse'
  result = requests.get(url)
  content = result.text
  soup = BeautifulSoup(content, 'html.parser')
  # ProcessorsMLResponse = {
  #   "products": [
  #   ]
  # }
  response=[]
  names = soup.find_all('h2', class_='ui-search-item__title shops__item-title')
  urls = soup.find_all('a', class_='ui-search-item__group__element shops__items-group-details ui-search-link')
  for i in range(0, 10, 1):
    auxResult = requests.get(urls[i]['href'])
    auxContent = auxResult.text
    auxSoup = BeautifulSoup(auxContent, 'html.parser')
    img = auxSoup.find_all('img', class_='ui-pdp-image ui-pdp-gallery__figure__image')
    price = auxSoup.find_all('span', class_='andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact')
    if(len(price) == 0):
        # print(price)
        continue
    realPrice = price[0].text
    realPrice = realPrice.split()
    response.append({
      "item_name" : names[i].text,
      "item_price" : realPrice[0],
      "item_picture" : img[0]['src'],
      "item_description" : "Armando",
      "item_url" : urls[i]['href'],
      "type_id" : 1,
      "user_id" : 'auth0|639e3ee1aacda0152647f763',
      'item_date': date.today().strftime('%Y-%m-%d') 
    })

  return(response)

#Convertir dólares a pesos colombianos
def usdToCOP():
  s = HTMLSession()
  url='https://www.google.com/search?q=Cuanto+vale+el+dolar&hl=es&sxsrf=ALiCzsbd7U9Th2StFoLQRKQo_7AJVkJSMw%3A1671723763614&source=hp&ei=83qkY5i1H47YkPIP7Ku6sAU&iflsig=AJiK0e8AAAAAY6SJA5dqPmmET8tU12F1v1sRO7_qBVTo&ved=0ahUKEwjY-tioyI38AhUOLEQIHeyVDlYQ4dUDCAc&uact=5&oq=Cuanto+vale+el+dolar&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgoIABCABBCHAhAUMgUIABCABDIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoECAAQQzoRCC4QgAQQsQMQgwEQxwEQ0QM6CAgAEIAEELEDOggIABCxAxCDAToHCAAQyQMQQzoHCAAQsQMQQzoLCAAQgAQQsQMQgwE6CAgAEIAEEMkDOg8IABCABBCHAhAUEEYQggI6DQgAEIAEELEDEIMBEAo6BwgAEIAEEApQmQxY0R5gth9oAnAAeACAAdoBiAGEGpIBBjAuMTYuM5gBAKABAbABCg&sclient=gws-wiz'
  result = s.get(url)
  content = result.text
  soup = BeautifulSoup(content, 'html.parser')
  usdValue = soup.find_all('input', class_='lWzCpb a61j6')
  usdValue = float(usdValue[0]['value'])
  return usdValue

####Scrapping de Amazon para intel core i3, i5 e i7:
from requests_html import HTMLSession
##Método que escarba los procesadores intel desde amazon, recibe un entero donde 0=core i3, 1=core i5 y 2=core i7
def ScrapProcessorsAMZN(reference):
  usdValue = usdToCOP()
  HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'),
    'Accept-Language': 'en-US, en;q=0.5'
}
  s = HTMLSession()
  if(reference==0):
    url='https://www.amazon.com/s?k=Procesador+core+i3&i=electronics&rh=n%3A229189%2Cp_89%3AIntel%2Cp_n_feature_four_browse-bin%3A2289794011&dc&language=es&ds=v1%3AcT1ibgPL8SUJQF2AMGrEcHNA3NMK%2FFnV1SKUXh2DIZE&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=XOAIVW5KOQLV&qid=1671719760&rnid=676578011&sprefix=procesador+core+i3%2Caps%2C165&ref=sr_nr_p_n_feature_four_browse-bin_1'
  elif (reference==1):
    url='https://www.amazon.com/-/es/s?k=Procesador+core+i5&i=computers&rh=n%3A229189%2Cp_89%3AIntel%2Cp_n_feature_four_browse-bin%3A2289793011%2Cp_n_condition-type%3A2224371011&dc&language=es&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1671723429&rnid=2224369011&ref=sr_nr_p_n_condition-type_1&ds=v1%3AY%2BKVh%2F9Sn%2BmIqMCumXd3sKBAKOqVqBKxpPmpBga2YpY'
  else:
    url='https://www.amazon.com/-/es/s?k=Procesador+core+i7&i=computers&rh=n%3A229189%2Cp_89%3AIntel%2Cp_n_feature_four_browse-bin%3A2289792011%2Cp_n_condition-type%3A2224371011&dc&language=es&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1671723477&rnid=2224369011&ref=sr_nr_p_n_condition-type_1&ds=v1%3AxgjBZYkudF1z2ZcTbxvhf5y4wy%2Fx5bm4QX5N9X1D3po'
  result = s.get(url, headers=HEADERS)
  content = result.text
  soup = BeautifulSoup(content, 'html.parser')
  # ProcessorsMLResponse = {
  #   "products": [
  #   ]
  # }
  response=[]
  #<h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/-/es/Procesador-escritorio-i3-10100-n%C3%BAcleos-LGA1200/dp/B086MMRW87/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&amp;crid=XOAIVW5KOQLV&amp;keywords=core+processor+i3&amp;qid=1671719771&amp;refinements=p_89%3AIntel%2Cp_n_feature_four_browse-bin%3A2289794011&amp;rnid=676578011&amp;s=pc&amp;sprefix=procesador+core+i3%2Caps%2C165&amp;sr=1-1"><span class="a-size-medium a-color-base a-text-normal">Intel Procesador de escritorio Core i3-10100 de 4 núcleos de hasta 4.3 GHz LGA1200 (chip Intel 400 Series) 65W, número de modelo: BX8070110100</span> </a> </h2>
  names = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
  #print(names[0].text)
  urls = soup.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
  # print(urls[0]['href'])
  # wholePrice = soup.find_all('span', class_='a-price-whole')
  # decimalPrice = soup.find_all('span', class_='a-price-fraction')
  # print(wholePrice[0].text+decimalPrice[0].text)
  # img = soup.find_all('img', class_='s-image')
  # print(img[0]['src'])
  for i in range(0, 10, 1):
    auxResult = requests.get("https://www.amazon.com"+urls[i]['href'], headers=HEADERS)
    auxContent = auxResult.text
    auxSoup = BeautifulSoup(auxContent, 'html.parser')
    img = auxSoup.find_all('div', class_='imgTagWrapper')
    price = auxSoup.find_all('span', class_='a-offscreen')
    if(len(price) == 0):
        # print(price)
        continue
    # Acomodamos la moneda
    auxPrice = price[0].text[3:]
    try:
        auxPrice = float(auxPrice)
    except ValueError:
        continue
    # print(img[0].img['src'])
    response.append({
      "item_name" : names[i].text,
      "item_price" : round(usdValue*auxPrice),
      "item_picture" : img[0].img['src'],
      "item_description" : "Armando",
      "item_url" : "https://www.amazon.com"+urls[i]['href'],
      "type_id" : 1,
      "user_id" : 'auth0|638b682bbc99c67d7152083b',
      'item_date': date.today().strftime('%Y-%m-%d') 
    })

  # amznResponseJson = json.dumps(ProcessorsResponse, ensure_ascii= False, indent=4)
  return(response)

####Scrapping de NeweGG para intel core i3, i5 e i7:
##Método que escarba los procesadores intel desde NeweGG, recibe un entero donde 0=core i3, 1=core i5 y 2=core i7
def ScrapProcessorsNGG(reference):
  usdValue = usdToCOP()
  HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'),
    'Accept-Language': 'en-US, en;q=0.5'
}
  s = HTMLSession()
  if(reference==0):
    url='https://www.newegg.com/p/pl?N=100007671%2050001157%20601295137%204814'
  elif (reference==1):
    url='https://www.newegg.com/p/pl?N=100007671%2050001157%204814%20601295141'
  else:
    url='https://www.newegg.com/p/pl?N=100007671%2050001157%204814%20601295136'
  result = s.get(url, headers=HEADERS)
  content = result.text
  soup = BeautifulSoup(content, 'html.parser')
  # ProcessorsMLResponse = {
  #   "products": [
  #   ]
  # }
  response=[]
  names = soup.find_all('a', class_='item-title')
  #print(names[0].text)
  urls = soup.find_all('a', class_='item-title')
  # print(urls[0]['href'])
  priceTag = soup.find_all('li', class_='price-current')
  # print(priceTag[0].strong.text)
  # print(priceTag[0].sup.text)
  img = soup.find_all('a', class_='item-img')
  # print(img[0].img['src'])
  for i in range(0, 10, 1):
    try:
      realPrice = float(priceTag[i].strong.text+priceTag[i].sup.text)
    except Exception:
      continue
    response.append({
      "item_name" : names[i].text,
      "item_price" : round(realPrice*usdValue),
      "item_picture" : img[0].img['src'],
      "item_description" : "Armando",
      "item_url" : urls[i]['href'],
      "type_id" : 1,
      "user_id" : 'auth0|639e3f6e9c43cd6f74e81ba0',
      'item_date': date.today().strftime('%Y-%m-%d') 
    })

  return(response)

url = 'http://127.0.0.1:6060/api/item/create2'

def mercadolibreArmando():
  requests.post(url, json = ScrapProcessorsML(0) + ScrapProcessorsML(1) + ScrapProcessorsML(2))

def amazonArmando():
  requests.post(url, json = ScrapProcessorsAMZN(0) + ScrapProcessorsAMZN(1) + ScrapProcessorsAMZN(2) )

def neweggArmando():
  requests.post(url, json = ScrapProcessorsNGG(0) + ScrapProcessorsNGG(1) + ScrapProcessorsNGG(2))
