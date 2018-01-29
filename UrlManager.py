# -*- encoding=utf-8 -*-


class UrlManager(object):

    def __init__(self):
        self.newUrls = set()  # type: set
        self.oldUrls = set()

    def has_new_url(self):
        """
        判断是否有未爬取得url
        :rtype :bool
        """
        return len(self.newUrls) != 0

    def add_new_urls(self, urls):
        """
        添加新的url
        :return: 
        """
        if urls is not None:
            if isinstance(urls, str):
                self.newUrls.add(urls)
            elif isinstance(urls, list):
                for url in urls:
                    self.newUrls.add(url)
            elif isinstance(urls, set):
                self.newUrls = self.newUrls.union(urls)

            else:
                pass

    def get_new_url(self):
        """
        获取一个新的url
        :rtype: str 
        """
        url = self.newUrls.pop()
        self.oldUrls.add(url)
        return url

    def get_new_url_size(self):
        """
        获取未爬取的大小
        :return: 
        """
        return len(self.newUrls)

    def get_old_url_size(self):
        """
        获取已经爬取的大小
        :return: 
        """
        return len(self.oldUrls)





