# encoding:utf-8

import UrlManager
import HtmlDownloader
import DataSave
import HtmlParse



class SpiderManager(object):

    def __init__(self):

        self.urlManager = UrlManager.UrlManager()
        self.htmlParse = HtmlParse.HtmlParse()
        self.htmlDownload = HtmlDownloader.HtmlDownload()
        self.dataSave = DataSave.DataSave()

    def crawl(self, root_url):
        self.urlManager.add_new_urls(root_url)

        while(self.urlManager.has_new_url()
              and self.urlManager.get_old_url_size() < 10):
            """
            暂时只下载10个url
            """
            try:
                new_url = self.urlManager.get_new_url()
                cont = self.htmlDownload.download_get(new_url)
                new_urls, new_data = self.htmlParse.do_parser(new_url, cont)
                self.urlManager.add_new_urls(new_urls)
                self.dataSave.store_data(new_data)

                print "已经抓取%s个链接" % self.urlManager.get_old_url_size()
            except Exception, e:
                print "crawl fail %s" % e

        self.dataSave.output_data()


if __name__ == '__main__':
    spiderManger = SpiderManager()
    spiderManger.crawl("http://e.pingan.com/pa18shoplife/category/list.jsp")










