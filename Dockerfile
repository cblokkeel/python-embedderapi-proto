# FROM python:3.9.4-slim-buster
# EXPOSE 8080
# WORKDIR /app
# COPY requirements.txt requirements.txt
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN pip install -r requirements.txt
# COPY . .

# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]

FROM python:3.10.12-slim-buster

WORKDIR /app
RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential
RUN apt-get -y install git
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .

EXPOSE 8080
ENV OPENAI_API_KEY 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
ENV DESIRED_API_KEY 75e4aae4-aaed-48d9-91b1-6bc08c85ca76

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
