FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install poetry
RUN poetry install

COPY . .

CMD ["python", "src/main.py"]