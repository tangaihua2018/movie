from flask import Flask

from service.haiwaikan import modify_ts_url

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/m3u8/<file_name>')
def process_request(file_name):
    uri_list = modify_ts_url(file_name)
    return uri_list


if __name__ == '__main__':
    app.run()
