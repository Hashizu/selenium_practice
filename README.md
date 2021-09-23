# seleniume practice

## 概要
seleniumの練習がしたい。
動くけどpoetry無視して構築してしまった。

Instagramから指定のタグ（KEYWORDとしてハードコーディング）の画像を一定数ダウンロードする。

## 前準備
正しいバージョンのchrome driver-binaryを導入する必要がある。

*pip環境で入れるとpylanceが対応しなかった…？ので後のことを考えてcodndaでchromedriverを導入。

*chrome > ヘルプ > chromeについて からバージョンを確認

```
conda config --append channels conda-forge
> conda forgeのレポジトリを獲得

conda search -f cromedriver
> 対応するchromedriverのバージョンを確認（自分のchromeに近いやつ。）

conda install python-chromedriver-binary=<version>
```

## usage

```
$ poetry install

$ python3 resoruce.py

$ python3 dl_from_json.py

```


