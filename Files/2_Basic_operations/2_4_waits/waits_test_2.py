from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = 'http://suninjuly.github.io/wait2.html'
browser = webdriver.Chrome()
browser.get(link)

#implicit wait that waits till it can find element on the page
#browser.implicitly_wait(5)

#explicit wait. wait till button becomes clickable
button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, 'verify'))
)
button.c
#button = browser.find_element_by_css_selector('button.btn')
button.click()
text_message = browser.find_element_by_css_selector('#verify_message')

assert 'Verification was successful!' in text_message.text

time.sleep(5)
browser.quit()