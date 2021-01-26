FROM python:3.8.1-slim-buster

WORKDIR /parser
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV MONGODB_HOST=mongo
ENV USE_PROXY 1
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "run_parser.py"]
