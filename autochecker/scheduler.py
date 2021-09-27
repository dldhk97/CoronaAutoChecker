import os, time, random
import schedule
from .checker import parse
from .log.logger import print_log

def reserve():
    _check_env()
    
    print_log('Reservation started.')

    input_hour = os.environ.get('CHECK_EVERY_DAY_AT_HOUR')
    input_minute = os.environ.get('CHECK_EVERY_DAY_AT_MINUTE')
    input_time = input_hour + ':' + input_minute

    print_log('Input time = ' + input_time)

    check_everyday_time = _normalize_time_str(input_time)

    if not _is_time_format(check_everyday_time):
        raise Exception('Invalid time format! Please input valid format like 21 30')

    schedule.every().day.at(check_everyday_time).do(job)
    print_log('Reservation completed! Now it runs at ' + str(check_everyday_time) + ' every day.')

    while True:
        schedule.run_pending()
        time.sleep(1)

def job():
    if os.environ.get('RANDOM_SLEEP') == 'True':
        _random_sleep()

    parse()

def _normalize_time_str(input):
    return input.replace('"', '')

def _is_time_format(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except:
        return False

def _check_env():
    if os.path.exists('./.env') == False:
        raise Exception('No .env file! Please create .env file!')

def _random_sleep():
    sleep_time = 60 * random.randrange(1, 10)                       # 0m ~ 10m
    print_log('Now sleep for ' + str(round(sleep_time / 60)) + ' minute')
    time.sleep(sleep_time)
    print_log('Now awaked')