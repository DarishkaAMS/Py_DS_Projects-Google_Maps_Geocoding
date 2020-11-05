# import getpass
#
# my_password = getpass.getpass('What is your password?\n')
# print(my_password)
from urllib.parse import urlparse
import os
import time
import requests
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver


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
# print(html_text)

'''
<button class="_5f5mN       jIbKX  _6VtSN     yZn4P   ">Follow</button>
'''

# browser.find_elements_by_css_selector('button')

# Using xpath
# my_button_xpath = '//button'
# browser.find_elements_by_css_selector(my_button_xpath)


def click_to_follow(browser):
    # my_follow_btn_xpath = "//a[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    # my_follow_btn_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    follow_btn_elments = browser.find_elements_by_xpath(my_follow_btn_xpath)
    for btn in follow_btn_elments:
        time.sleep(2)  # self-throttle
        try:
            btn.click()
        except:
            pass

#
# new_user_url = 'https://www.instagram.com/ted/'
# browser.get(new_user_url)
# click_to_follow(browser)


time.sleep(2)
the_VCP_url = 'https://www.instagram.com/veuveclicquot/'
browser.get(the_VCP_url)

post_url_pattern = 'https://www.instagram.com/p/<post-slug-id>'
post_xpath_str = '//a[contains(@href, "/p/")]'
post_links = browser.find_elements_by_xpath(post_xpath_str)
post_link_el = None

if len(post_links) > 0:
    post_link_el = post_links[0]

if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)


video_els = browser.find_elements_by_xpath("//video")
images_els = browser.find_elements_by_xpath("//img")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "INSTA images")
os.makedirs(IMG_DIR, exist_ok=True)


def scrape_and_save(elements):
    for el in elements:
        # print(img.get_attribute('src'))
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        # print(base_url)
        filename = os.path.basename(base_url)
        filepath = os.path.join(IMG_DIR, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)


scrape_and_save(video_els)
scrape_and_save(images_els)