# encoding:utf-8

from bs4 import BeautifulSoup


class HtmlParse(object):

    def do_parser(self, url, html_cont):
        """
        解析html
        :param html_cont: 
        :rtype: (set, list)
        """
        new_urls = set()
        new_data = []
        soup = BeautifulSoup(html_cont, 'html.parser')
        tag1 = soup.find_all(id='itemContainer')
        for tag2 in tag1[0].find_all('a'):
            new_url = self._get_new_url(tag2)
            if new_url is not None:
                new_urls.add(new_url)
            n_data = self._get_new_data(tag2)
            if n_data is not None and len(n_data) > 0:
                new_data.append(n_data)

        return new_urls, new_data

    def _get_new_url(self, soup):
        """
        获取 html的链接        
        :type :param soup: BeautifulSoup
        :rtype: str 
        """
        tmp = '/pa18shoplife/details'
        href = soup['href']
        if tmp in href:
            return href

    def _get_new_data(self, soup):
        """
        获取html 中需要的数据
        :param soup: 
        :rtype: dict 
        """

        data_dict = {}
        dl_tags = soup.find_all("dl")
        for dl_tag in dl_tags:
            time_class = dl_tag.find("dd", {"class": "time"})
            time = time_class.find(text=True)
            cation_class = dl_tag.find("dd", {"class": "cation"})
            cation = cation_class.find(text=True)
            money_class = dl_tag.find("dd", {"class": "money"})
            money = "%s%s" % (money_class.find_next(text=True), money_class.find_next(text=True).find_next(text=True))
            describe_array = dl_tag.find_all('dd')[-4:]
            describe = u"%s,%s,%s,%s。" % (describe_array[0].find(text=True),
                                                 describe_array[1].find(text=True),
                                                 describe_array[2].find(text=True),
                                                 describe_array[3].find(text=True))

            data_dict[u'time'] = time
            data_dict[u'cation'] = cation
            data_dict[u'money'] = money
            data_dict[u'describe'] = describe

        return data_dict















