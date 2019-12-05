from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #find people radio button and verify default checked state
    people_radio = browser.find_element_by_id('peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('people_checked value is: ', people_checked)
    assert people_checked is not None, 'People radio button is NOT checked'

    #find robots radio button and verify default checked state
    robots_radio = browser.find_element_by_id('robotsRule')
    robots_not_checked = robots_radio.get_attribute('checked')
    print('robots_not_checked value is: ', robots_not_checked)
    assert robots_not_checked is None, 'People radio button is checked'

    #find submit button state after 10 secconds have passed
    time.sleep(10)
    button = browser.find_element_by_css_selector('button.btn')
    button_state = button.get_attribute('disabled')
    print('submit button value is: ', button_state)
    assert button_state is not None, 'Submit button is disabled'

finally:
    time.sleep(2)
    browser.quit()
