from selenium import webdriver
import time
import math

#calculate formula
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#find and click the Submit button
def click_submit():
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

#accept to alert
def accept_alert():
    alert = browser.switch_to_alert()
    alert.accept()

#copy value from alert to Terminal and accept
def copy_from_alert():
    alert = browser.switch_to_alert()
    print(alert.text)
    alert.accept()

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #find and click the Submit button
    click_submit()

    #switch to alert and click confirm
    accept_alert()

    #find X element and get the value
    x_element = browser.find_element_by_css_selector('#input_value')
    x_value = int(x_element.text)

    #calculate the formula with X value
    result = calc(x_value)

    #find text field and fill the answer
    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(str(result))

    #find and click the Submit button
    click_submit()
    
    #short delay to follow up
    time.sleep(1)

    #copy from and accept alert
    copy_from_alert()

finally:
    time.sleep(5)
    browser.quit()
    