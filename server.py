import random

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ukr")
def ukr_bimba():
    return "Это украинская бимба"

@app.route("/rus")
def rus_bimba():
    return "Это русска бимба"

@app.route("/dollar")
def dollar():
    price = random.randint(35, 120)
    # return "Сегодня курс доллара - {} рублей.".format(price)
    return render_template('dollar.html', price=price)

@app.route('/animals')
def animals():

    animal = request.args.get('type')

    return render_template('animals.html', animal=animal)

app.run(host="0.0.0.0", port=8000, debug=True)