import time
from selenium import webdriver

browser = webdriver.Chrome()
url = "https://google.com"
browser.get(url)
# browser.get('https://github.com/DarishkaAMS')

"""
<input type ='text' class'' id='' name='??' />
<textarea name='??'><textarea>

<input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both" 
aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" 
spellcheck="false" title="Пошук" value="" aria-label="Пошук" data-ved="0ahUKEwjVg-fsxejsAhVvDWMBHRfqBkkQ39UDCAQ">
"""

time.sleep(2)
name = 'q'
search_el = browser.find_element_by_name('q')
# search_el = browser.find_element_by_css_selector('h1')
# print(search_el)

search_el.send_keys('I love you')

"""
<input type='submit'/>
<button type='submit'/>
<form></form>

<input class="gNO89b" value="Пошук Google" aria-label="Пошук Google" name="btnK" type="submit" ' \
'data-ved="0ahUKEwjVg-fsxejsAhVvDWMBHRfqBkkQ4dUDCAs">
"""

submit_btn_el = browser.find_element_by_css_selector('input[type="submit"]')
print(submit_btn_el.get_attribute('name'))