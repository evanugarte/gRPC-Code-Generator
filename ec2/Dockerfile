FROM python:3.8.4-slim-buster

WORKDIR /app

RUN apt-get update

RUN yes | apt-get install curl

COPY . .

RUN ["/bin/bash", "./setup"]

EXPOSE 5000

CMD ["python3", "server.py"]
