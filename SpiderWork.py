# encoding:utf-8

from multiprocessing.managers import BaseManager
from HtmlDownloader import HtmlDownload
from HtmlParse import HtmlParse


class SpiderWork(object):

    def __init__(self):
        print "spider work init start"

        BaseManager.register("get_task_queue")
        BaseManager.register("get_result_queue")

        server_addr = '127.0.0.1'
        self.manager = BaseManager(address=(server_addr, 8101), authkey='ZF')
        try:
            self.manager.connect()
        except BaseException, e:
            print e



        self.task = self.manager.get_task_queue()  # type: Queue

        print self.task, self.task.empty()

        self.result = self.manager.get_result_queue() # type: Queue
        self.downloader = HtmlDownload()
        self.parser = HtmlParse()
        print "spider work init finish"


    def crawl(self):
        while True:
            try:
                if not self.task.empty():
                    new_url = self.task.get()

                    if new_url == "END":
                        self.result.put({'new_urls':"END","new_data":"END"})
                        return
                    cont = self.downloader.download_get(new_url)
                    new_urls, new_data = self.parser.do_parser(new_url, cont)
                    self.result.put({'new_urls':new_urls,'new_data':new_data})
            except EOFError, e:
                print "连接工作节点失败"
                return
            except Exception, e:
                print e
                print 'Crawl fail work'


if __name__ == '__main__':
    spider_work = SpiderWork()
    spider_work.crawl()









