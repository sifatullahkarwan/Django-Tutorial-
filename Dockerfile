FROM python:3.10-alpine
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev

RUN apk del .tmp


RUN mkdir /app

WORKDIR  /app 

COPY requirements.txt  /app



RUN pip install  --no-cache-dir -r requirements.txt 

COPY .   /app/

EXPOSE 9000

CMD [ "python3","manage.py","runserver","0.0.0.0:9000" ]