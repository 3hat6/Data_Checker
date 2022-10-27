import requests
import bs4
import settings

url = 'https://jsonplaceholder.typicode.com/todos'

page = requests.get(url).text
soup = bs4.BeautifulSoup(page, 'html.parser').text
modify = settings.making_dict(soup)
#txt = open('text.txt').read()
#modify = settings.making_dict(txt)
keys = list(dict(modify[0]).keys())
result = settings.checker(modify, keys)
for res in result:
    print(res)
