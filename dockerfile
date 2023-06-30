FROM python:3.9
WORKDIR /app

COPY main.py .
COPY data.json .

RUN pip install requests

RUN pip install bs4

CMD ["python", "./main.py"]