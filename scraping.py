from selenium import webdriver
import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse
import re
import json

def get_search_value(ptn, str):
      
    result = re.search(ptn, str)
      
    if result:
        return result.group(1)
    else:
        return None

KEYWORD = "カメラ"

# url
url = "https://www.instagram.com/explore/tags/" + urllib.parse.quote(KEYWORD) + "/"

#　ヘッドレスモードでブラウザを起動
options = Options()
options.add_argument('--headless')
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    #"user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36"
)

# ブラウザーを起動
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
print(url)
driver.get(url)

driver.implicitly_wait(10)  # 見つからないときは、10秒まで待つ

html = driver.page_source
# print(html)
# json_str = get_search_value("window._sharedData = (.*);<\/script>", html)
# dict = json.loads(json_str)

# print(dict)

with open("./out/camera.html", mode="w", encoding="utf8") as f:
    f.write(html)