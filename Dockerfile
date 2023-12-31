# Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install Flask

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]