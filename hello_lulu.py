from flask import Flask

app_lulu = Flask(__name__)


@app_lulu.route('/hello_page_lulu')
def hello_world_lulu():
    return 'Hello World!'


if __name__ == '__main__':
    app_lulu.run(debug=True)
