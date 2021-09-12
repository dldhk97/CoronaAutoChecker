import os, sys, time, random
from .driver.driver_utils import load_driver
from .page.login_page import login
from .page.check_page import check_all

def parse():
    try:
        _random_sleep()
        _check_env()
        url = os.environ.get('SELF_CHECK_URL')

        driver = load_driver()
        driver.get(url=url)
        
        print('I got it!')

        login(driver)
        check_all(driver)
        
        print('Done!')
    except Exception as e:
        print(e)
    
    try:
        driver.quit()
    except:
        pass

## env
def _check_env():
    if os.path.exists('./.env') == False:
        raise Exception('No .env file! Please create .env file using .env_example')
    if len(sys.argv) < 3:
        raise Exception('Invalid args! Please run with args (USER_ID, USER_PASSWORD)')

def _random_sleep():
    sleep_time = random.randrange(0, 5)
    print('Now sleep for ' + str(sleep_time) + 's')
    time.sleep(sleep_time)
    print('Now awaked')