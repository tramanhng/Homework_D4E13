from bs4 import BeautifulSoup as soup  #HTML data structure
import requests

# url_path = "https://www.foody.vn/ha-noi/food/nha-hang"
# response = requests.get(url_path)
# page_soup = soup(response.content, "html.parser")
# result_side = page_soup.find("div", {"class": "result-side"})
# result_items = result_side.find_all("div", {"class": "result-name"})

# for item in result_items:
#     # print(item.h2.text.strip())
#     print(item.find("h2").text.strip())
#     print(item.find("div", {"class": "point"}).text.strip())

url_path = "https://www.foody.vn/ha-noi/dia-diem?ds=Restaurant&vt=row&st=2&page=2&provinceId=218&categoryId=&append=true"
response = requests.get(url_path)
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "bc-jcb=1; fbm_395614663835338=base_domain=.foody.vn; flg=vn; floc=218; gcat=food; fd.keys=; _ga=GA1.2.864847503.1593766469; _gid=GA1.2.357084075.1593766469; _fbp=fb.1.1593766470548.661967586; fd.res.view.218=155; xfci=ZGI05ZJTPUKFBKA; __ondemand_sessionid=qkeqpvmvyuiqd02dqbjor2mg; __utmc=257500956; __utmz=257500956.1593783028.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _gat=1; __utma=257500956.864847503.1593766469.1593783028.1593786720.4; __utmt_UA-33292184-1=1; __utmb=257500956.1.10.1593786720",
    "Host": "www.foody.vn",
    "Referer": "https://www.foody.vn/ha-noi/food/dia-diem?ds=Restaurant",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "X-Foody-User-Token": "null",
    "X-Requested-With": "XMLHttpRequest"
}

response = requests.get(url_path, headers=headers)
response_json = response.json()
items = response_json['searchItems']
for item in items:
    name = item['Name']
    point = item['AvgRating']
    print(name + ": " + point)