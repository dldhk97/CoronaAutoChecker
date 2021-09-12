import sys, time, os
import schedule

def reserve(job):
    _check_env()
    
    input_hour = os.environ.get('CHECK_EVERY_DAY_AT_HOUR')
    input_minute = os.environ.get('CHECK_EVERY_DAY_AT_MINUTE')
    input_time = input_hour + ':' + input_minute
    print(input_time)
    check_everyday_time = _normalize_time_str(input_time)

    if not _is_time_format(check_everyday_time):
        raise Exception('Invalid time format! Please input valid format like 21 30')

    schedule.every().day.at(check_everyday_time).do(job)
    print('Reservation completed! Now it runs at ' + str(check_everyday_time) + ' every day.')

    while True:
        schedule.run_pending()
        time.sleep(1)

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