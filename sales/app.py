from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "sales 시작 page에요"


@app.route('/sales')
def sales():
    return "sales backend입니다."


if __name__ == "__main__":
    app.run(host="0.0.0.0")
