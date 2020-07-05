from bs4 import BeautifulSoup as soup
import requests
import time

url_path = "https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=USD,BTC,ETH,XRP,BCH,LTC&cryptocurrency_type=all&limit=200&sort=market_cap&sort_dir=desc&start=201"
list_price = {}
coin_info = open('coin_info','w')
line_1 = "Name, " + "Symbol, " + "Price 1, " + "Price 2, " + "Price 3, " + "Price 4, " + "Price 5, " + "Price 6, " + "Price 7, " + "Price 8, " + "Price 9, " + "Price 10, " + "Price 11, " + "Price 12, "
coin_info.write(line_1 + '\n')

for loop in range(0,13):
    respond = requests.get(url_path)
    headers = {
        "authority": "web-api.coinmarketcap.com",
        "method" : "GET",
        "path" : "/v1/cryptocurrency/listings/latest?convert=USD,BTC,ETH,XRP,BCH,LTC&cryptocurrency_type=all&limit=200&sort=market_cap&sort_dir=desc&start=201",
        "scheme" : "https",
        "accept" : "application/json, text/plain, */*",
        "accept-encoding" : "gzip, deflate, br",
        "accept-language" : "en-US,en;q=0.9",
        "origin" : "https://coinmarketcap.com",
        "referer" : "https://coinmarketcap.com/",
        "sec-fetch-dest" : "empty",
        "sec-fetch-mode" : "cors",
        "sec-fetch-site" : "same-site",
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }

    response = requests.get(url_path, headers=headers)
    response_json = response.json()
    items = response_json["data"]

    # for item in items:
    #     name = item['name']
    #     symbol =  item['symbol']
    #     price = item['quote']['USD']['price']

    #     # print(name + ': ' + symbol + ', ' + str(price))

    for item in items:
        name = item['name']
        symbol =  item['symbol']
        price = item['quote']['USD']['price']
        key = f'{name}, {symbol}'
        if key not in list_price:
            list_price[key] = []
        else: 
            list_price[key].append(price)
            print(list_price)

    if loop == 1:
        break
    time.sleep(300)
        
for key, prices in list_price.items():
    line_insert = f'{key}: '
    prices = str(prices)
    line_insert += prices[1:(len(prices)-1)]
    coin_info.write(line_insert + '\n')

coin_info.close()        

