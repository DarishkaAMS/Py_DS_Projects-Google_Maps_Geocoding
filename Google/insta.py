# import getpass
#
# my_password = getpass.getpass('What is your password?\n')
# print(my_password)
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver
import time

browser = webdriver.Chrome()
url = 'https://www.instagram.com'
browser.get(url)

time.sleep(2)
username_el = browser.find_element_by_name('username')
username_el.send_keys(INSTA_USERNAME)
password_el = browser.find_element_by_name('password')
password_el.send_keys(INSTA_PASSWORD)

submit_btl_el = browser.find_element_by_css_selector('button[type="submit"]')
submit_btl_el.click()

body_el = browser.find_element_by_css_selector('body')
html_text = body_el.get_attribute('innerHTML')

print(html_text)