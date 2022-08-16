FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
RUN mkdir /backend/static
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev make \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]