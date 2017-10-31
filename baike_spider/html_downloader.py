# coding:utf-8
import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:  # 判断是否请求成功
            return None
        return response.read()