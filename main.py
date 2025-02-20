import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index0():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    s = '''<html>
        Человечество вырастает из детства.<br>
        Человечеству мала одна планета.<br>
        Мы сделаем обитаемыми безжизненные пока планеты.<br>
        И начнем с Марса!<br>
        Присоединяйся!<br>
        </html>'''
    return s


@app.route('/image_mars')
def image_mars():
    return f'''<title>Привет, Марс!</title><h1>Жди нас, Марс!</h1><img src="{flask.url_for('static', filename='images/MARS.png')}"> 
           <div class="p-3 mb-2 bg-primary text-white">.Человечество вырастает из детства.</div>
            <div class="p-3 mb-2 bg-secondary text-white">.Человечеству мала одна планета.</div>
            <div class="p-3 mb-2 bg-success text-white">.Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="p-3 mb-2 bg-danger text-white">.И начнем с Марса!</div>
            <div class="p-3 mb-2 bg-warning text-dark">.Присоединяйся!</div>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<title>Привет, Марс!</title><h1>Жди нас, Марс!</h1><
    
    img src="{flask.url_for('static', filename='images/MARS.png')}"> 
           <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
           <div class="p-3 mb-2 bg-primary text-white">.Человечество вырастает из детства.</div>
            <div class="p-3 mb-2 bg-secondary text-white">.Человечеству мала одна планета.</div>
            <div class="p-3 mb-2 bg-success text-white">.Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="p-3 mb-2 bg-danger text-white">.И начнем с Марса!</div>
            <div class="p-3 mb-2 bg-warning text-dark">.Присоединяйся!</div>'''

@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{flask.url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
