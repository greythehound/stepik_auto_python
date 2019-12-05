from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def click_submit():
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

def alert_switch_copy():
    alert = browser.switch_to_alert()
    print(alert.text)
    alert.accept()


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #delay to follow up
    time.sleep(1)

    #find a button and click it
    click_submit()

    #switch to another tab
    new_tab = browser.window_handles[1]
    browser.switch_to_window(new_tab)

    #find X element and it's value
    x_element = browser.find_element_by_css_selector('#input_value')
    x_value = int(x_element.text)

    #calculate the formula with X value
    result = calc(x_value)

    #find answer text field and fill it with calculated value
    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(str(result))

    #find submit button and click it
    click_submit()

    #delay to follow up
    time.sleep(2)

    #switch to alert and copy value to Terminal
    alert_switch_copy()

finally:
    time.sleep(3)
    browser.quit()