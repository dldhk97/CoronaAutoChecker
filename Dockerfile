FROM dldhk97/python-chrome-kor-docker:3.8_amd64

LABEL maintainer="dldhk97@naver.com"

COPY . /checker

WORKDIR /checker

# install requirements
RUN pip3 install -r requirements.txt

ENV USER_ID ID
ENV USER_PASSWORD PASSWORD
ENV RUN_EVERY_DAY True
ENV CHECK_EVERY_DAY_AT_HOUR HOUR
ENV CHECK_EVERY_DAY_AT_MINUTE MINUTE
ENV RANDOM_SLEEP True

CMD (sed -i '/^USER_ID=/c\USER_ID=$USER_ID' .env) && \
(sed -i '/^USER_PASSWORD=/c\USER_PASSWORD=$USER_PASSWORD' .env) && \
(sed -i '/^RUN_EVERY_DAY=/c\RUN_EVERY_DAY=$RUN_EVERY_DAY' .env) && \
(sed -i '/^CHECK_EVERY_DAY_AT_HOUR=/c\CHECK_EVERY_DAY_AT_HOUR=$CHECK_EVERY_DAY_AT_HOUR' .env) && \
(sed -i '/^CHECK_EVERY_DAY_AT_MINUTE=/c\CHECK_EVERY_DAY_AT_MINUTE=$CHECK_EVERY_DAY_AT_MINUTE' .env) && \
(sed -i '/^RANDOM_SLEEP=/c\RANDOM_SLEEP=$RANDOM_SLEEP' .env)

ENTRYPOINT [ "python", "-u", "main.py" ]