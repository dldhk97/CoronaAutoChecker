FROM python:3.8-alpine

LABEL maintainer="dldhk97@naver.com"

COPY . /checker

WORKDIR /checker

RUN pip3 install -r requirements.txt

ENV USER_ID ID
ENV USER_PASSWORD PASSWORD

CMD ["main.py"]

ENTRYPOINT ["python3", USER_ID, USER_PASSWORD]