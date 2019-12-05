from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #find text values of 2 headers
    number1_element = browser.find_element_by_css_selector('#num1')
    number2_element = browser.find_element_by_css_selector('#num2')

    number1_value = number1_element.text
    number2_value = number2_element.text
    sum = int(number1_value) + int(number2_value)
    print(sum)

    #find and click element from the list that equals the sum value
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum))

    #find submit button and click it
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    #copy value from alert
    alert = browser.switch_to_alert()
    print(alert.text)

finally:
    time.sleep(3)
    browser.quit()