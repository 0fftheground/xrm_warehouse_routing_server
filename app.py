from flask import Flask
from flask import request
from model import get_route_json
from utils import verify_md5_sign
import json
# import requests
import logging

app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

logging.basicConfig(filename='record.log', level=logging.WARNING, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def hello():
    return 'hello docker&flask'

@app.route('/test', methods=['POST'])
def return_route():
    request_data = request.get_data().decode('utf-8')
    # print(request_data)
    data = json.loads(request_data)
    if verify_md5_sign(data['deliveryNo'], data['sign']):
        try:
            result = get_route_json(data)
        except Exception as e:
            app.logger.error("calculation failed!")
            app.logger.error(e)
        # print(result)
        # requests.post(url, data=result)
        return result
    else:
        app.logger.warning("Sign verification failed!")
        return 'Sign verification failed!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
