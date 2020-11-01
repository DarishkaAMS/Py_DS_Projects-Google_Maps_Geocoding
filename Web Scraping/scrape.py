import datetime
import requests

now = datetime.datetime.now()
year = now.year


def url_to_txt(url, filename='world.html', save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        html_text = html_text.encode('utf-8').decode('ascii', 'ignore') # to en/decode
        # if save:
        with open(f"world-{year}.html", 'w') as f:
            f.write(html_text)
        return html_text
    return ""


url = "https://www.boxofficemojo.com/year/world/"
# url = "https://www.facebook.com/"

url_to_txt(url)
#html_text =


