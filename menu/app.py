from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "menu 시작 page에요"


@app.route('/menu')
def menu():
    return "menu backend입니다."


if __name__ == "__main__":
    app.run(host="0.0.0.0")
