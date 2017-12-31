#-*- coding: utf-8-*-
from flask import Flask, render_template, request, url_for, redirect, make_response

app = Flask(__name__)

# 뭔가 잘못되었을 때 에러메세지를 띄울 수 있도록 하는 함수.. message 변수를 전달하여 출력되는 에러메세지를 변경할 수 있음.
@app.route('/error')
def error():
    return render_template('error.html')

# 메인페이지를 렌더링해주는 함수
@app.route('/', defaults={'page' : 1})
@app.route('/<int:page>')
def homepage(page):
    return render_template('homepage.html')

if __name__ == "__main__":
    app.run()
