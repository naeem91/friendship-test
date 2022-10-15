FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080  

VOLUME /app

CMD python manage.py runserver 8080
