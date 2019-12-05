from selenium import webdriver
import time

link = 'http://suninjuly.github.io/wait1.html'
browser = webdriver.Chrome()

browser.implicitly_wait(5)
browser.get(link)

button = browser.find_element_by_css_selector('button.btn')
button.click()
text_message = browser.find_element_by_css_selector('#verify_message')

assert 'Verification was successful!' in text_message.text

time.sleep(5)
browser.quit()