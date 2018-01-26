# -*- encoding=utf-8 -*-


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
            if isinstance(urls, str):
                self.new_urls.add(urls)
            elif isinstance(urls, list):
                for url in urls:
                    self.new_urls.add(url)
            elif isinstance(urls, set):
                self.new_urls.union(urls)
            else:
                pass

    def get_new_url(self):
        """
        获取一个新的url
        :rtype: str 
        """
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def get_new_url_size(self):
        """
        获取未爬取的大小
        :return: 
        """
        return len(self.new_urls)

    def get_old_url_size(self):
        """
        获取已经爬取的大小
        :return: 
        """
        return len(self.old_urls)





