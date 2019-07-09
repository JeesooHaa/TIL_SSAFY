# ssafy.txt 파일을 읽어서
# 역순으로 reversed_ssafy.txt 파일로 저장
with open('ssafy.txt', 'r') as f:
    lines = f.readlines() # 각 라인을 item 으로 list 의 형태로 반환    
    
lines.reverse() # list 를 반대로 뒤집는다.

with open('reversed_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)
