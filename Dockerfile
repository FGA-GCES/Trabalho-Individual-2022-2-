
FROM python:3.9 


WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt


CMD ["python3", "src/main.py"]