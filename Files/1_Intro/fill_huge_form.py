from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name ("input")
    for element in elements:
        element.send_keys('My answer')
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    alert = browser.switch_to_alert()
    print(alert.text)
    time.sleep(3)
    browser.quit()
 
