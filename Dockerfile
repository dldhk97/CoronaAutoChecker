FROM python:3.8

LABEL maintainer="dldhk97@naver.com"

COPY . /checker

WORKDIR /checker

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
ENV CHECK_EVERY_DAY_AT_HOUR HOUR
ENV CHECK_EVERY_DAY_AT_MINUTE MINUTE

CMD python -u main.py $USER_ID $USER_PASSWORD $CHECK_EVERY_DAY_AT_HOUR $CHECK_EVERY_DAY_AT_MINUTE
