FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt && apk add make

EXPOSE 8080  

CMD python manage.py runserver 8080
