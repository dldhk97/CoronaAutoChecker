from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_elem_by_id(driver, elem_id):
    return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, elem_id)))