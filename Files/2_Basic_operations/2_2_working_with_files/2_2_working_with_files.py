from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #data values
    fn = 'Jack'
    ln = 'Crawlinger'
    em = 'test@mail.com'

    #find and fill First Name text field
    firstname = browser.find_element_by_css_selector('[name="firstname"]')
    firstname.send_keys(fn)

    #find and fill Last Name text field
    lastname = browser.find_element_by_css_selector('[name="lastname"]')
    lastname.send_keys(ln)

    #find and fill Email text field
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys(em)

    #finding a file on the system
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    #finding Upload element and upload the file
    upload_file = browser.find_element_by_css_selector('[name="file"]')
    upload_file.send_keys(file_path)

    #finding and clicking Submit button
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    #get value from an alert
    alert = browser.switch_to_alert()
    print(alert.text)

finally:
    time.sleep(5)
    browser.quit()

