from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_css_selector('#treasure')
    get_x = int(treasure.get_attribute('valuex'))
    
    result = calc(get_x)

    text_field = browser.find_element_by_css_selector('#answer')
    text_field.send_keys(str(result))

    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector('#robotsRule')
    robot_radio.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    
    alert = browser.switch_to_alert()
    print(alert.text)
    alert.accept()

finally:
    time.sleep(3)
    browser.quit()