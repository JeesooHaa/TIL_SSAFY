from flask import Flask, render_template, request # 사용자의 요청을 확인할 수 있음
import requests
app = Flask(__name__)


@app.route('/') # / => root
def index():
    return 'Hello world'


@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'Hello {name}'
    return render_template('greeting.html', html_name=name)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'Pong! age: {age}' 
    # render_template('pong.html')


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')
    font = requests.get('http://artii.herokuapp.com/fonts_list')
    # Ascii Art API 를 활용해서 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    result = response.text
    return render_template('ascii_result.html', result=result)


#####
@app.route('/lotto_input')
def lotto_input():
    # 사용자가 입력할 수 있는 페이지만 전달
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split() # txt => list / str

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # Json 타입의 파일을 python dictionary 로 parsing 해줘 
    
    lotto_drw = [] # int 
    for i in range(1,7):
        lotto_drw.append(lotto_info[f'drwtNo{i}'])
        # lotto_drw.append(str(lotto_info[f'drwtNo{i}'])) 당첨번호를 str으로 받기 

    lotto_numbers = list(map(int, lotto_numbers))

    # # 번호 교집합 개수 찾기 
    # if len(lotto_numbers) == 6:         # 사용자를 믿으면 안됨 
    #     matched = 0
    #     for number in lotto_numbers:    # 사용자 숫자를 하나씩 확인하면서  
    #         if number in winner:        # 당첨번호에 있는지 체크해서
    #             matched += 1            # 당첨시 matched 를 1 씩 증가 시킨다.

    #     if matched == 6:
    #         result = '1등입니다!'
    #     elif matched == 5:
    #         if str(lotto_info['bnusNo']) in lotto_numbers:
    #             result = '2등입니다!'
    #         else:
    #             result = '3등입니다!'
    #     elif matched == 4:
    #         result = '4등입니다.'
    #     elif matched == 5:
    #         result = '5등입니다....'
    #     else:
    #         result = '꽝..'
    # else:
    #     result = '입력하신 숫자가 6개가 아닙니다.'

    # return render_template('lotto_result.html', result=result)

    count_win = 0 
    for i in lotto_numbers:
        cc = i in lotto_drw
        if cc == True:
            count_win += 1    

    lotto_bonus_num = lotto_info['bnusNo']
    bonus_win = lotto_bonus_num in lotto_numbers

    rank = 0
    if count_win == 6:
        rank = 1
    elif (count_win == 5) and (bonus_win == True):
        rank = 2
    elif count_win == 5:
        rank = 3
    elif count_win == 4:
        rank = 4
    elif count_win == 3:
        rank = 5 
    else:
        rank = '꽝'

    return f'{lotto_round}, {lotto_numbers}, {rank}'


if __name__ == '__main__':  
    app.run(debug=True)
