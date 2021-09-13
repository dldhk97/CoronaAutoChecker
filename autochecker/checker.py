import os
from .driver.driver_utils import load_driver
from .page.login_page import login
from .page.check_page import check_all

def parse():
    try:
        _check_env()

        user_id = os.environ.get('USER_ID')
        user_password = os.environ.get('USER_PASSWORD')
        url = os.environ.get('SELF_CHECK_URL')

        driver = load_driver()
        driver.get(url=url)
        
        print('Page open succeed!')
        login(driver, user_id, user_password)
        check_all(driver)
        print('Done!')
        
    except Exception as e:
        print(e)
    
    try:
        driver.quit()
    except:
        pass

def _check_env():
    if os.path.exists('./.env') == False:
        raise Exception('No .env file! Please create .env file!')