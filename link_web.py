import requests
from bs4 import BeautifulSoup

def link_truy_cap(tag_brand, tag_year, tag_price):
    url1 = 'https://bonbanh.com/oto'
    url2 = '-cu-da-qua-su-dung'
    if tag_brand == 'All' and tag_year == 'All' and tag_price[0] == 0 and tag_price[1] == 2000:
        url1 = 'https://bonbanh.com/oto'
    else:
        if tag_brand == 'Other':
            url1 = 'https://bonbanh.com/oto/hang_khac'
        elif tag_brand != 'All':
            url1 = f'https://bonbanh.com/oto/{tag_brand}'

        if tag_year != 'All':
            url1 = url1 + f'-nam-{tag_year}'

    url = url1 + url2

    if tag_price[0] != 0 and tag_price[1] != 2000:
        url = url + f'-gia-tu-{tag_price[0]}-{tag_price[1]}-trieu'
    elif tag_price[0] != 0:
        url = url + f'-gia-tren-{tag_price[0]}-trieu'
    elif tag_price[1] != 2000:
        url = url + f'-gia-duoi-{tag_price[1]}-trieu'
    
    return url

def link_page(url):
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')

    link_list = []
    link_list.append(url)
    
    #Link truy cập vào từng trang của website
    for i in range(2, 11):
        new_link = url + f'/page,{i}'
        link_list.append(new_link)
    return link_list

def link_search_item(url, search):
    search = search.lower().split()
    link_list = link_page(url)
    search_find = [link_list[i] + '?q=' for i in range(len(link_list))]
    link_list_search = []
    for j in range(len(search_find)):
        for i in range(len(search)):
            search_find[j] += search[i] + '+'
        link_list_search.append(search_find[j].strip('+'))
    return link_list_search