import requests
import bs4 # Beautiful Soup 

url = 'https://finance.naver.com/sise/'

response = requests.get(url)
print(response)
print(response.status_code)

html = response.text

soup = bs4.BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text

print(kospi)
