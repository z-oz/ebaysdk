from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

keywords = input('Search eBay: ')
api = finding(appid='your_api_key', config_file=None)
api_request = {'keywords':keywords, 'output_selector': 'sellerinfo'}
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content, 'lxml')
totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')
count = 0
title_list = []
price_list = []
condition_list = []
category_list = []
for item in items:
    title = item.title.string.strip()
    price = int(float(item.currentprice.string))
    condition = item.conditiondisplayname.string.lower()
    cat = item.categoryid.string.lower()
    count += 1
    title_list.append(title)
    price_list.append(price)
    condition_list.append(condition)
    category_list.append(cat)
print('Total Results:', count)
average_price = sum(price_list) / len(price_list)

