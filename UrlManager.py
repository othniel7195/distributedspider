# -*- encoding=utf-8 -*-

import types

class UrlManager(object):

    def __init__(self):
        self.new_urls = set()  # type: set
        self.old_urls = set()

    def has_new_url(self):
        """
        判断是否有未爬取得url
        :rtype :bool
        """
        return len(self.new_urls) != 0

    def add_new_urls(self, urls):
        """
        添加新的url
        :return: 
        """
        if urls is not None:
            if type(urls) is types.StringTypes:
                self.new_urls.add(urls)
            elif types(urls) is types.ListType:
                tmp_urls = urls  # type: list



