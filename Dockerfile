FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
copy requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/