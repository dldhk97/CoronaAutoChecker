import os, sys
from selenium import webdriver
from .driver import downloader
from .login_page import login
from .check_page import check_all

def parse():
    try:
        _check_env()
        url = os.environ.get('SELF_CHECK_URL')

        driver = _load_driver()

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

## Driver
def _load_driver():
    downloader.download_driver()

    if (os.path.exists('./chromedriver.exe') == False) and (os.path.exists('./chromedriver') == False):
        raise Exception('No chromedriver!')

    options = _get_options()
    
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.abspath(os.path.join(absolute_path, os.pardir))
    driver_path = root_path + '/chromedriver'
    print('chrome_driver_path=' + driver_path)

    try:
       os.chmod(driver_path, 0o0777)
    except Exception as e:
       print('Failed to chmod driver')
       print(e)

    return webdriver.Chrome(executable_path=driver_path, chrome_options=options)

def _get_options():
    options = webdriver.ChromeOptions()
    
    options.add_argument('headless')
    options.add_argument("no-sandbox")

    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    return options
