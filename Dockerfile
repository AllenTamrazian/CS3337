FROM python:alpine

EXPOSE 8000
WORKDIR /app

RUN pip3 install Django django-widget-tweaks

COPY . /app
ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
