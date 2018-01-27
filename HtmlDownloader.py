# coding:utf-8

import requests
import json


class HtmlDownload(object):

    def __init__(self):
        self.header = {
            "Accept": "" "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome / 63.0.3239.84 Safari / 537.36"
        }

    def download_get(self, url, params=None):
        """
        下载html get 方式
        :param url: 
        :param params: 
        :rtype: str 
        """
        if url is not None:
            r = requests.get(url=url, params=params, header=self.header)  # type :requests.Response
            if r.status_code == 200:
                r.encoding = 'utf-8'
                return r.text
            else:
                return None

    def download_post(self, url, params):
        """
        下载html post 方式
        :param url: 
        :param params: 
        :rtype:  str
        """

        if url is not None:
            r = None
            if isinstance(params, dict):
                r = requests.post(url=url, data=params, header=self.header)
            elif isinstance(params, json):
                r = requests.post(url=url, json=params, header=self.header)

            if r.status_code == 200:
                r.encoding = 'utf-8'
                return r.text
            else:
                return None





