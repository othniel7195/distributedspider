# encoding:utf-8

import Queue
from multiprocessing.managers import BaseManager
import UrlManager
import DataSave
import time
from multiprocessing.process import Process

class SpiderServer(object):

    def __init__(self):
        # url管理器把url给爬虫节点的通道
        self.urlQueue = Queue.Queue()
        # 爬虫节点把数据返回解析通道
        self.resultQueue = Queue.Queue()
        # 数据解析通道
        self.parseQueue = Queue.Queue()
        # 存储数据通道
        self.storeQueue = Queue.Queue()

    def start_server(self):
        """
        
        :rtype: BaseManager 
        """
        # 把 url 任务队列和结果队列在网络中暴露
        BaseManager.register('get_task_queue', callable=lambda: self.urlQueue)
        BaseManager.register('get_result_queue', callable=lambda: self.resultQueue)

        # 绑定端口 设置验证口令
        manager = BaseManager(address=('', 8001), authkey='ZF')
        return manager

    def url_manager_proc(self, root_url):
        url_manager = UrlManager.UrlManager()
        url_manager.add_new_urls(root_url)
        while True:
            while(url_manager.has_new_url()):
                new_url = url_manager.get_new_url()
                self.urlQueue.put(new_url)
                if url_manager.get_old_url_size() > 2000:
                    self.urlQueue.put('END')
                    return

            try:
                if not self.parseQueue.empty():
                    # 获取解析出来的新的urls
                    urls = self.parseQueue.get()
                    url_manager.add_new_urls(urls)
            except BaseException, e:
                time.sleep(0.1)


    def result_proc(self):
        while True:
            try:
                if not self.resultQueue.empty():
                    content = self.resultQueue.get(True)
                    print  "content: %s" % content
                    if content['new_urls'] == 'END':
                        print "接收到通知结束爬虫"
                        self.storeQueue.put("END")
                        return

                    self.parseQueue.put(content['new_urls'])
                    self.storeQueue.put(content['new_data'])
                else:
                    time.sleep(0.1)
            except BaseException, e:
                time.sleep(0.1)


    def store_proc(self):
        data_save = DataSave.DataSave()
        while True:
            try:
                if not self.storeQueue.empty():
                    data = self.storeQueue.get()
                    if data == "END":
                        print "存储进程结束"
                        data_save.output_data()

                        return
                    data_save.store_data(data)
                else:
                    time.sleep(0.1)
            except BaseException, e:
                time.sleep(0.1)



if __name__ == '__main__':
    server = SpiderServer()
    server_manager = server.start_server()
    url_manager_proc = Process(target=server.url_manager_proc, args=('http://e.pingan.com/pa18shoplife/category/list.jsp',))
    result_proc = Process(target=server.result_proc)
    store_proc = Process(target=server.store_proc)
    url_manager_proc.start()
    result_proc.start()
    store_proc.start()

    server_manager.get_server().serve_forever()



























