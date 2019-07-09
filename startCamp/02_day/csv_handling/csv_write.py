dinner = {
    '양자강': '02-557-4211', # 차돌짬뽕
    '김밥카페': '02-553-3181', # 라돈
    '순남시래기': '02-508-0887', # 보쌈정식
}

# 1. String formatting
with open('dinner.csv', 'w', encoding='utf-8') as f:
    # [['양자강', '02-557-4221'], ['김밥카페', '02-553-3181'], ...]
    for item in dinner.items():
        f.write(f'{item[0]},{item[1]}\n') # 양자강,02-557-4221

# 2. csv writer 
import csv
with open('dinner.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f) # f 라는 파일에 csv 를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item)
