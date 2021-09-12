from .selenium_utils import get_elem_by_id

def login(driver, user_id, user_password):
    print('USER_ID=' + user_id)

    _fill_input_box(driver, user_id, 'Form_아이디.아이디_my_inputBox')
    _fill_input_box(driver, user_password, 'Form_비밀번호.비밀번호')

    _click_login_button(driver)
    _check_loggined(driver)
    

def _fill_input_box(driver, value, elem_id):
    try:
        inputbox = get_elem_by_id(driver, elem_id)
        inputbox.send_keys(value)
    except:
        raise Exception('Failed to fill ID')

def _click_login_button(driver):
    try:
        login_button = get_elem_by_id(driver, 'Form_로그인.send')
        login_button.click()
    except:
        raise Exception('Failed to login')

def _check_loggined(driver):
    alert = driver.switch_to_alert()
    print('Login page says :' + alert.text)
    
    if '일치하지 않습니다' in alert.text:
        raise Exception('Incorrect ID, password!')
    if '이미 제출하셨습니다' in alert.text:
        raise Exception("You've already submitted it!")
