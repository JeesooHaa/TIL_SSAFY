# 열기모드
# r: 읽기, w: 쓰기(write - 오버라이트), a: 추가(append)
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'this is line {i + 1} \n')
f.close()

with open('with_ssafy.txt', 'w') as f: # 컨텍스트 매니저
    for i in range(10):
        f.write(f'this is line {i + 1}\n')
            
with open('ssafy.txt', 'w', encoding='utf-8') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])
