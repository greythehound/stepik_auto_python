from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #find text of the 'x' element
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    #calculate the X accoding to the formula
    y = calc(x)

    #find text field and fill the answer
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    #find robot checkbox and check it
    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robot_checkbox.click()

    #find people and robot radio button checked
    people_radio_button = browser.find_element_by_id('peopleRule')
    robot_radio_button = browser.find_element_by_css_selector('#robotsRule')

    #verify that people radio button is selected by default
    people_checked = people_radio_button.get_attribute('checked')
    print('people_checked value is: ', people_checked)
    assert people_checked is not None, 'People radio button is not selected by default'

    #verify that robots radio button is NOT selected by default
    robots_not_checked = robot_radio_button.get_attribute('checked')
    print('robots_not_checked value is: ', robots_not_checked)
    assert robots_not_checked is None, 'Robots radio button is selected by default'

    #select robot radio button
    robot_radio_button.click()
    #find and click the Submit button
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    #copy value from the alert
    alert = browser.switch_to_alert()
    print(alert.text)

finally:
    time.sleep(10)
    browser.quit()