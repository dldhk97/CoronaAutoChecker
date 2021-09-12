# CoronaAutoChecker
코로나 자가진단 자동화 프로그램

## Requirements
Google Chrome, python3.8

## How to use
```
# install requirements
python3 -m pip install -r requirements.txt

# run
python3 main.py YOUR_USER_ID YOUR_USER_PASSWORD
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
```

### run
```
docker-compose up -d
```

## TODO
- [ ] 경량화(alpine 이미지 사용)
- [ ] 스케쥴(매일 몇시마다 실행, ENV로 받아서 설정가능)
- [ ] 잡다한 이미지 및 컨테이너 생성하지 않게(alpine 사용 시)
- [x] 시간 랜덤화
- [x] OS 상관없이 잘 작동하게
