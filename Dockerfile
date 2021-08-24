FROM python:3.8

WORKDIR /cardsol

COPY requirements.txt .

RUN python3 -m venv env

CMD ["source", "./env/bin/activate"]

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./tests/main.py"]