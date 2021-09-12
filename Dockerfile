FROM python:3.8

LABEL maintainer="dldhk97@naver.com"

COPY . /checker

WORKDIR /checker

# set timezone
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# set display port to avoid crash
ENV DISPLAY=:99

# install requirements
RUN pip3 install -r requirements.txt

ENV USER_ID ID
ENV USER_PASSWORD PASSWORD

ENV RUN_EVERY_DAY True
ENV CHECK_EVERY_DAY_AT_HOUR HOUR
ENV CHECK_EVERY_DAY_AT_MINUTE MINUTE

RUN sed -i '/^USER_ID=/c\USER_ID=$USER_ID' .env
RUN sed -i '/^USER_PASSWORD=/c\USER_PASSWORD=$USER_PASSWORD' .env

RUN sed -i '/^RUN_EVERY_DAY=/c\RUN_EVERY_DAY=$RUN_EVERY_DAY' .env
RUN sed -i '/^CHECK_EVERY_DAY_AT_HOUR=/c\CHECK_EVERY_DAY_AT_HOUR=$CHECK_EVERY_DAY_AT_HOUR' .env
RUN sed -i '/^CHECK_EVERY_DAY_AT_MINUTE=/c\CHECK_EVERY_DAY_AT_MINUTE=$CHECK_EVERY_DAY_AT_MINUTE' .env

CMD python -u main.py
