# encoding:utf-8

from bs4 import BeautifulSoup


class HtmlParse(object):

    def do_parser(self, html_cont):
        """
        解析html
        :param html_cont: 
        :rtype: (set, set)
        """
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_url(soup)
        new_data = self._get_new_data(soup)

        return new_urls, new_data

    def _get_new_url(self, soup):
        """
        获取 html的链接        
        :param soup: BeautifulSoup
        :return: 
        """
        pass

    def _get_new_data(self, soup):
        """
        获取html 中需要的数据
        :param soup: 
        :return: 
        """
        pass



