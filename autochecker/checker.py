import os
from selenium import webdriver
from .driver import downloader
from .login_page import login
from .check_page import check_all

def parse():
    url = os.environ.get('SELF_CHECK_URL')

    driver = _load_driver()
    
    try:
        driver.get(url=url)
        
        print('I got it!')
        login(driver)
        check_all(driver)
        
        print('Done!')
    except Exception as e:
        print(e)
    finally:
        driver.quit()


## Driver
def _load_driver():
    downloader.download_driver()

    if(os.path.exists('./chromedriver.exe') == False):
        raise Exception('No chromedriver!')

    options = _get_options()

    driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
    return driver

def _get_options():
    options = webdriver.ChromeOptions()
    
    # options.add_argument('headless')
    # options.add_argument("no-sandbox")

    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    return options
