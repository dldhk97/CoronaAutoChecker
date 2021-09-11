import requests
from bs4 import BeautifulSoup
import os
import platform
import wget
import zipfile

def download_driver():
    if(os.path.exists('./chromedriver.exe') == True):
        return
    print('chromedriver does not exists!')

    latest_version = _get_latest_version()
    base_url = os.environ.get('CHROME_DRIVER_URL') + latest_version + '/'
    file_name = _get_file_name_by_platform()
    download_url = base_url + file_name

    print('chromedriver download started!')
    latest_driver_zip = wget.download(download_url, file_name)
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(latest_driver_zip)
    print('chromedriver download complete!')

    

def _get_latest_version():
    url = os.environ.get('CHROME_DRIVER_URL') + 'LATEST_RELEASE'

    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)
        raise Exception('Failed to get latest chromedriver version')

def _get_file_name_by_platform():
    sys = platform.system()
    arch = 'Unknown'

    if sys == 'Windows':
        arch = 'win32'
    elif sys == 'Linux':
        arch = 'linux64'
    elif sys == 'Darwin':
        arch = 'mac64'
        if platform.processor == 'arm':
            arch += '_m1'
    else:
        raise Exception('Failed to download chromedriver. Unknown OS.')
    
    return 'chromedriver_' + arch + '.zip'