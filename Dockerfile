from python:3.7-slim-stretch


WORKDIR /stacked_bar_chart

ADD . /stacked_bar_chart

RUN pip install -r requirements.txt


