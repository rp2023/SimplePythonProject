FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 5000

ENV FLASK_APP=simple_time_service.py

CMD ["python", "simple_time_service.py"]
