from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #find all required text fields and button
    first_name = browser.find_element_by_css_selector('.first_block .first')
    last_name = browser.find_element_by_css_selector('.first_block .second')
    email = browser.find_element_by_css_selector('.first_block .third')
    button = browser.find_element_by_css_selector('button.btn')

    #fill fields with text and click button
    first_name.send_keys('test')
    last_name.send_keys('test')
    email.send_keys('test')
    button.click()

    #wait for next page to load
    time.sleep(1)

    #find success text
    success = browser.find_element_by_tag_name('h1')
    success_text = success.text

    #check text of success
    assert "Congratulations! You have successfully registered!" == success_text

finally:
    time.sleep(10)
    browser.quit()
