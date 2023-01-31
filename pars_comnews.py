import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

num_page = 0
ind = 200
url = f'https://www.comnews.ru/news?page={num_page}'
res = requests.get(url)
print (res.status_code)
k = 1
dict = {'date': '', 'title': '', 'body': '', 'tag': '', 'link': '', 'img': '' }
date = []
title = []
body = []
tag = []
link = []
img = []
# while res.status_code == 200:
while num_page < 269:
    url = f'https://www.comnews.ru/news?page={num_page}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    news = soup.find_all('div', class_ = 'views-row')

    for el in news:
        date.append(el.find('div', class_ = 'date').text)
        title.append(el.find('div', class_ = 'title').text)
        body.append(el.find('div', class_ = 'body').text)
        tag.append(el.find('div', class_ = 'tags').text)
        link.append('https://www.comnews.ru' + (el.find('a').get('href')))
        img.append(el.find('img'))

        dict['date'] = date
        dict['title'] = title
        dict['body'] = body
        dict['tag'] = tag
        dict['link'] = link
        dict['img'] = img

        k += 1  
    num_page += 1
# print(dict)

df = pd.DataFrame(dict)
df.to_excel('example.xlsx')
# print(f'Новость № {k}: {date}')
# print(f'Новость № {k}: {title}')
# print(f'Новость № {k}: {body}')
# print(f'Новость № {k}: {tag}')
# print(f'Новость № {k}: https://www.comnews.ru{link}')
# print(f'Новость № {k}: {img}')