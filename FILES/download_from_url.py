import requests
import os
import shutil
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# download and rename
downloaded_img_path = os.path.join(DOWNLOADS_DIR, "1.jpg")
url = 'https://www.expatica.com/app/uploads/sites/9/2017/07/cost-of-living-in-switzerland.jpg'

# for a smallish ite,
r = requests.get(url, stream=True)
r.raise_for_status() # 200
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)

# dl_filename = os.path.basename(url)
# new_dl_filename = os.path.join(DOWNLOADS_DIR, dl_filename)
# with requests.get(url, stream=True) as r:
#     with open(new_dl_filename, 'wb') as file_obj:
#         shutil.copyfileobj(r.raw, file_obj)


download_file(url, DOWNLOADS_DIR)