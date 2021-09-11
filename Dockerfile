FROM python:3.8-alpine

LABEL maintainer="dldhk97@naver.com"

COPY . /checker

WORKDIR /checker

RUN pip3 install -r requirements.txt

ENV USER_ID ID
ENV USER_PASSWORD PASSWORD

CMD echo "USER_ID=$USER_ID"

ENTRYPOINT python main.py $USER_ID $USER_PASSWORD
