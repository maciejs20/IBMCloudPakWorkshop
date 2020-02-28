FROM ubuntu

RUN apt-get update && apt-get install -y python python-pip

RUN pip install flask

COPY app.py /usr/local

ENTRYPOINT FLASK_APP=/usr/local/app.py flask run --host=0.0.0.0

