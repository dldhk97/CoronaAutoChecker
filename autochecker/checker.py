import os
from .driver.driver_utils import load_driver
from .page.login_page import login
from .page.check_page import check_all
from .log.logger import print_log

def parse():
    try:
        _check_env()

        user_id = os.environ.get('USER_ID')
        user_password = os.environ.get('USER_PASSWORD')
        url = os.environ.get('SELF_CHECK_URL')
        driver = load_driver()

        _open_page(driver, url)
        print_log('Page open succeed!')
        
        login(driver, user_id, user_password)

        check_all(driver)
        print_log('Checks submitted!')

        print_log('Done!')
        
    except Exception as e:
        print_log(e)
    try:
        driver.quit()
    except:
        pass

def _check_env():
    if os.path.exists('./.env') == False:
        raise Exception('No .env file! Please create .env file!')

def _open_page(driver, url):
    driver.get(url=url)