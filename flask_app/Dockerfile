FROM python:3.6

WORKDIR usr/src/flask_app
COPY requirements.txt .
RUN pip install requests
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

#CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]