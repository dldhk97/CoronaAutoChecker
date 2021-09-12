import sys, time
import schedule

def reserve(job):
    if not is_reservation_arg_exists:
        raise Exception('Invalid ags! If you want reservation, please input valid args (USER_ID, USER_PASSWORD, CHECK_EVERY_DAY_AT')
    
    check_everyday_time = sys.argv[3]
    if not _is_time_format(check_everyday_time):
        raise Exception('Invalid time format! Please input valid format like 21:30')

    schedule.every().day.at(check_everyday_time).do(job)
    print('Reserve completed! Now it runs at ' + str(check_everyday_time) + ' every day.')

    while True:
        schedule.run_pending()
        time.sleep(1)

def is_reservation_arg_exists():
    return len(sys.argv) > 3

def _is_time_format(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except:
        return False