import requests
from requests_html import HTML


url = 'https://www.amazon.co.uk/Mo%C3%ABt-Chandon-Ros%C3%A9-Imp%C3%A9rial-Gift/dp/B008U7SWXC/ref=redir_mobile_desktop?ie=UTF8&aaxitk=vEani3XHgUute4jc1LufSA&hsa_cr_id=3093126030502&pd_rd_r=0e2e200a-ff2e-48da-9cb6-0f60ac493dc5&pd_rd_w=LaWGK&pd_rd_wg=jSDk6&ref_=sbx_be_s_sparkle_mcd_asin_1_img'
title_lookup = '#productTitle'
price_lookup = '#unqualifiedBuyBox'

r = requests.get(url)
html_str = r.text

print(html_str)
