FROM python:3.11.2

WORKDIR /app

ADD . /app

# install requirements
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir --compile -r requirements.txt

RUN [ "python3", "-c", "import nltk; nltk.download('punkt', download_dir='/usr/local/nltk_data')" ]

CMD exec uvicorn --host 0.0.0.0 --port $PORT main:app