from .selenium_utils import get_elem_by_id

def check_all(driver):
    click_element(driver, 'Form_문항1.radio1.m1')
    click_element(driver, 'Form_문항2.check2_1')
    click_element(driver, 'Form_문항3.radio3.m1')
    click_element(driver, 'Form_문항4.radio4.m1')
    click_element(driver, 'Form_문항5.radio5.m1')
    click_element(driver, 'Form8.pb1')                  # Submit button
    click_alert(driver)
    print("Checks submitted!")
    

def click_element(driver, elem_id):
    try:
        elem = get_elem_by_id(driver, elem_id)
        elem.click()
    except:
        raise Exception('Failed to click' + elem_id)

def click_alert(driver):
    alert = driver.switch_to_alert()
    alert.accept()