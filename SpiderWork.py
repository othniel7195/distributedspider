# encoding:utf-8

from multiprocessing.managers import BaseManager
from HtmlDownloader import HtmlDownload
from HtmlParse import HtmlParse

class SpiderWork(object):

    def __init__(self):

        BaseManager.register("get_task_queue")
        BaseManager.register("get_result_queue")

        server_addr = '127.0.0.1'
        self.manager = BaseManager(address=(server_addr, 8001), authkey='ZF')
        self.manager.connect()

        self.task = self.manager.get_task_queue()
        self.result = self.manager.get_result_queue()
        self.downloader = HtmlDownload()
        self.parser = HtmlParse()


    def crawl(self):
        pass


if __name__ == '__main__':
    pass









