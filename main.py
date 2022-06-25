import requests
import bs4
from fake_headers import Headers


def check_article(article, preview):
    count = 0
    for word in keywords:
        if word in preview.text.split():
            count += 1
            break
    if count >= 1:
        date = article.find(class_='tm-article-snippet__datetime-published').text
        header = article.find(class_='tm-article-snippet__title-link').text
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        print(f'<{date}> - <{header}> - <{base_url}{href}>')


keywords = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/all/'
headers = Headers(os="windows", headers=True).generate()
base_url = 'https://habr.com'

response = requests.get(url, headers=headers).text
soup = bs4.BeautifulSoup(response, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    preview = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
    if preview != None:
        check_article(article, preview)
    else:
        preview = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        check_article(article, preview)
