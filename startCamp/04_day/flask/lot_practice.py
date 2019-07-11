import requests

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
response = requests.get(url)
lotto_info = response.json() # Json 타입의 파일을 python dictionary 로 parsing 해줘 


lotto_drw =[]

lotto_numbers = ['39', '34', '37', '12', '9', '15'] # type error 
lotto_numbers22 = [39, 34, 12, 37, 9, 15]

for i in range(1,7):
    lotto_drw.append(lotto_info[f'drwtNo{i}'])

lotto_true = []
for i in lotto_numbers:
    lotto_true.append(i in lotto_drw)

print(lotto_true)

aa = 0 
for i in lotto_true:
    if i == True:
        aa += 1

lotto_bonus_num = lotto_info['bnusNo']

print(type(lotto_bonus_num))

print(lotto_bonus_num == '12')

# lotto_bonus = False
# for i in lotto_numbers:
#     if i == lotto_bonus_num:
#         lotto_bouns = True

bb = 0 
if lotto_bonus_num in lotto_numbers22:
    bb = 5
else:
    bb = 4 



if aa == 6:
    rank = '1등'
elif (aa == 5) and (bb == 5):
    rank = '2등'

print(rank)


