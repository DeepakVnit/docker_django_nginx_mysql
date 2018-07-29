FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN mkdir /code
RUN mkdir /mystatic
ADD . /code/
WORKDIR /code
RUN pip install -r requirements.txt
RUN chmod +x start.sh
