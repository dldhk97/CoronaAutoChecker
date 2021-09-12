# CoronaAutoChecker
코로나 자가진단 자동화 프로그램

## Requirements
Google Chrome, python3.8

## How to use
```
# install requirements
python3 -m pip install -r requirements.txt

# run
python3 main.py YOUR_USER_ID YOUR_USER_PASSWORD HOUR MINUTE

# example
python3 main.py 20991234 p4ssw0rd 08 30
```

## How to use with docker-compose

### build docker image
```
docker build -t dldhk97/corona_auto_checker:0.1 .
```

### create docker-compose.yml
```
version: "3"
services:
  corona_auto_checker:
    image: dldhk97/corona_auto_checker:0.1
    container_name: corona_auto_checker
    environment:
      - USER_ID=YOUR_USER_ID
      - USER_PASSWORD=YOUR_USER_PASSWORD
      - RUN_EVERY_DAY=True
      - CHECK_EVERY_DAY_AT_HOUR=08
      - CHECK_EVERY_DAY_AT_MINUTE=30
```

### run
```
docker-compose up -d
```

## TODO
- [ ] 경량화(alpine 이미지 + Chronium 사용)
