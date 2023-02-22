from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "account 시작 page에요"


@app.route('/account')
def account():
    return "account backend입니다."


if __name__ == "__main__":
    app.run(host="0.0.0.0")
