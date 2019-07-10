import requests
import bs4
import csv 

# 1. Bithumb 페이지를 가지고 온다.
response = requests.get('https://www.bithumb.com/') # 요청을 보내 응답을 받는다.
html = response.text # 응답받은 객체에서 html 문서를 string 으로 가지고 옴 

# 2. Beautiful Soup 모듈을 이용하여 string type 의 html 을 파싱한다!
soup = bs4.BeautifulSoup(html, 'html.parser')

# 3. 각 코인의 정보 담겨있는 table row 데이터를 list 형태로 가져온다.
coins = soup.select(' .coin_list tr ')

# 띄어쓰기 접근 : 모두 / > 접근 : 바로 밑 

# 5. csv writer 를 이용해서 정보를 저장한다. 
with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)

    # 4. 각 코인을 순회하며 필요한 정보만 추출한다. 
    for coin in coins: # coin == tr 
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text # .replace('NEW', '')
        coin_name = coin_name.replace('NEW', '').strip() # 공백 삭제 
        coin_price = coin.select_one('td:nth-child(2) > strong').text
        # 6. 작성 
        data = (coin_name, coin_price)
        csv_writer.writerow(data)
