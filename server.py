from flask import Flask, render_template

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

app.run(host="0.0.0.0", port=8000, debug=True)