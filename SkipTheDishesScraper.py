from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from urllib.request import urlopen as uReq
import json
import ssl
import urllib

ssl._create_default_https_context = ssl._create_unverified_context
data = {}

city = input("Enter the name of a city: ")
my_url = 'https://www.skipthedishes.com/' + city + '/restaurants'

# get the page data
uClient =uReq(my_url) 
page_html = uClient.read()
uClient.close()  
page_soup = soup(page_html, "html.parser")

for x in page_soup.findAll('div', attrs = {'class' : 'styles__Row-sc-1m5q2j3-0 styles__Title-sc-1xmhsgm-10 hgDKhm'}):
    holder = x.findNext("div")
    time = holder.find('span').text # get the delivery time
    time = time.replace("-","to") # replace irregular characters
    key = x.text
    key = key.replace("'","")
    pre_rating = x.findNext('span')
    rating = pre_rating.findNext('div') # get the rating
    data[key] = []

    data[key].append({
        'Delivery Time' : time,
        'Rating' : rating.text
    })

with open('skip_final.json', 'w+', encoding='utf-8') as out: # writing the ginal file
    json.dump(data, out, indent=4, ensure_ascii=False)
