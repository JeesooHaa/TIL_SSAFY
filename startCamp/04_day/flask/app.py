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
    lotto_numbers = request.args.get('numbers').split() # txt => list

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # Json 타입의 파일을 python dictionary 로 parsing 해줘 
    
    lotto_drw = []
    for i in range(1,7):
        lotto_drw.append(lotto_info[f'drwtNo{i}'])

    lotto_true = []
    for i in lotto_numbers:
        lotto_true.append(i in lotto_drw)

    aa = 0 
    for i in lotto_true:
        if i == True:
            aa += 1

    lotto_bonus_num = lotto_info['bnusNo']

    bb = 0 
    if lotto_bonus_num in lotto_numbers:
        bb = 2
    else:
        bb = 1 

    rank = 0
    if aa == 6:
        rank = 1
    elif (aa == 5) and (bb == 2):
        rank = 2

    return f'{lotto_round}, {lotto_numbers}, {rank}'


if __name__ == '__main__':  
    app.run(debug=True)
