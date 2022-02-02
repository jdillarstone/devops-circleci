# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt update
RUN apt install pandoc texlive -y

COPY . .
RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]