from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)


@app.route("/") # endpoint 
def hello(): # def 함수 만드는 법 
    # return "Hello!"
    return render_template('index.html') # 폴더 이름 templates / app.py 와 같은 위치 
    

@app.route('/ssafy')
def ssafy():
    return 'Hello SSAFY'


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 12, 9)
    td = b_day - today 
    return f'{td.days}일 남았습니다.' 


@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag1</h1>'


@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    ''' 


# Variable Routing 
@app.route('/greeting/<name>') # IU
def greeting(name): # name == IU
    return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:num>')
def cube(num):
    # return f'{num}의 3 제곱은 {num ** 3} 입니다.'
    return render_template('cube.html', num_1=num, num_2=num ** 3)


#실습
@app.route('/lunch/<int:people>')
def lunch(people):
    # 사람 수 만큼의 랜덤 아이템을 menu list 에서 뽑아서 보여주는 페이지!
    menu = ['짜장면', '만둣국', '볶음밥', '마파두부덮밥']
    order = random.sample(menu, people) # 비복원 추출 
    return str(order)


@app.route('/movie')
def movie():
    movies = ['트루먼쇼', '스파이더맨', '토이스토리4', '기생충', '알라딘']
    return render_template('movie.html', movies=movies)


if __name__ == '__main__': # 직접 호출할 때만 서버로 활용 
    app.run(debug=True) # 저장시 서버 재부팅 

# python **.py

# hello.py 
# message = hi
# import hello

# print(hello.message)
