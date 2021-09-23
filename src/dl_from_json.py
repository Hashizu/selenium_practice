import re
import json
import time
from tqdm import tqdm
import urllib
import urllib.request

JSON = "../out/posts_笑顔_1000.json"
OUT =  "../out/smile"

def download_file(url, dst_path):
    '''
    url : ダウンロードしたい画像/データのurl
    dst_path ： ダウンロードファイルの名前
    '''

    try:
        with urllib.request.urlopen(url) as web_file, open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())
    except urllib.error.URLError as e:
        print(e)


if __name__ == '__main__':

    with open(JSON, mode="r", encoding="utf8") as f:
        p = json.load(f)

    for i, im_key in enumerate(tqdm(p.keys())):
        download_file(p[im_key]["src"], "{}/image{}.jpg".format(OUT,i))
        time.sleep(1)
    