from selenium import webdriver
import time
import math
from selenium.webdriver.common.action_chains import ActionChains

link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    actions = ActionChains(browser)
#open the URL
    browser.get(link)
#find and click the link
    button = browser.find_element_by_link_text("224592")
    button.click()
#wait till next page is loaded
#    time.sleep(1)
#find all text fields and button of the form
    first_name = browser.find_element_by_name("first_name")
    last_name = browser.find_element_by_name("last_name")
    city = browser.find_element_by_class_name("city")
    country = browser.find_element_by_id("country")
    button = browser.find_element_by_css_selector('button.btn')

#filling the form
    first_name.send_keys('Ivan')
    last_name.send_keys('Petrov')
    city.send_keys('Smolensk')
    country.send_keys('Russia')
#scroll to and click button 
    actions.move_to_element(browser.find_element_by_css_selector('button.btn')).perform()
    button.click()
finally:
    time.sleep(30)
    browser.quit()
