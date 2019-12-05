from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #wait till price dropps to 100
    wait_for_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,'price'), '$100')
    )
    #click Book button
    if wait_for_price == True:
        button = browser.find_element_by_css_selector("#book")
        button.click()

    #find X element
    x_element = browser.find_element_by_css_selector('#input_value')
    x_text = int(x_element.text)

    #calculate the formula
    result = calc(x_text)

    #fill text field with the X value
    text_field = browser.find_element_by_css_selector('#answer')
    text_field.send_keys(str(result))


    #click submit button
    submit_button = browser.find_element_by_css_selector('#solve')
    #scroll to the button
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    #switch to alert and print the value
    alert = browser.switch_to_alert()
    print(alert.text)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
