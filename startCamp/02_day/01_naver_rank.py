import requests
import bs4

url = 'https://www.naver.com/'

response = requests.get(url)

html = response.text

print(html)

soup = bs4.BeautifulSoup(html, 'html.parser')
rank = soup.select('.ah_l .ah_item .ah_a .ah_k ')

for i in rank[:20]:
    print(i.text)
