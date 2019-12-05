from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #find X value and calculate the formula
    x_element = browser.find_element_by_css_selector('#input_value')
    x_value = int(x_element.text)
    result = calc(x_value)

    #find text field, scroll it to top of the page and fill calculated value
    text_field = browser.find_element_by_css_selector('#answer')
    #scroll field to the top
    browser.execute_script("arguments[0].scrollIntoView(true);", text_field)
    text_field.send_keys(str(result))

    #find robot checkbox and check it
    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    #browser.execute_script("arguments[0].scrollIntoView(true);", text_field)
    robot_checkbox.click()

    #find robot radiobutton and select it
    robot_radiobutton = browser.find_element_by_css_selector('#robotsRule')
    #browser.execute_script("arguments[0].scrollIntoView(true);", text_field)
    robot_radiobutton.click()

    #find submit button and click it
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    #print alert to terminal
    alert = browser.switch_to_alert()
    print(alert.text)

finally:
    time.sleep(5)
    browser.quit()