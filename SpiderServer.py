# encoding:utf-8
# multiprocessing.Queue 是跨进程通信队列
# Queue.Queue 进程内非阻塞队列,各自私有 无法跨进程通信
from multiprocessing import queues
from multiprocessing.managers import BaseManager
import UrlManager
import DataSave
import time
from multiprocessing.process import Process

class SpiderServer(object):

    def __init__(self):

        print "spider server init"

    def start_server(self, urlQueue, resultQueue):
        """
        
        :rtype: BaseManager 
        """
        # 把 url 任务队列和结果队列在网络中暴露
        BaseManager.register('get_task_queue', callable=lambda: urlQueue)
        BaseManager.register('get_result_queue', callable=lambda: resultQueue)

        # 绑定端口 设置验证口令
        manager = BaseManager(address=('', 8101), authkey='ZF')
        return manager

    def url_manager_proc(self, root_url, urlQueue, parseQueue):
        url_manager = UrlManager.UrlManager()
        url_manager.add_new_urls(root_url)
        while True:
            if(url_manager.has_new_url()):
                new_url = url_manager.get_new_url()
                urlQueue.put(new_url)
            else:
                urlQueue.put('END')


            try:
                if not parseQueue.empty():
                    # 获取解析出来的新的urls
                    urls = parseQueue.get()
                    url_manager.add_new_urls(urls)
                else:
                    time.sleep(0.1)
            except BaseException, e:
                time.sleep(0.1)


    def result_proc(self, resultQueue, storeQueue):
        while True:
            print "result_proc %s" % resultQueue.empty()
            try:
                if not resultQueue.empty():
                    content = resultQueue.get(True)
                    print  "content: %s" % content
                    if content['new_urls'] == 'END':
                        print "接收到通知结束爬虫"
                        storeQueue.put("END")
                        return

                    parseQueue.put(content['new_urls'])
                    storeQueue.put(content['new_data'])
                else:
                    time.sleep(0.1)
            except BaseException, e:
                time.sleep(0.1)


    def store_proc(self, storeQueue):
        data_save = DataSave.DataSave()
        while True:
            print "store_proc %s" % storeQueue.empty()
            try:
                if not storeQueue.empty():
                    data = storeQueue.get()
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
    # url管理器把url给爬虫节点的通道
    urlQueue = queues.Queue()
    #print urlQueue
    # 爬虫节点把数据返回解析通道
    resultQueue = queues.Queue()
    # 数据解析通道
    parseQueue = queues.Queue()
    # 存储数据通道
    storeQueue = queues.Queue()
    server = SpiderServer()
    server_manager = server.start_server(urlQueue, resultQueue)
    url_manager_proc = Process(target=server.url_manager_proc, args=('http://e.pingan.com/pa18shoplife/category/list.jsp', urlQueue, parseQueue))
    #print urlQueue
    result_proc = Process(target=server.result_proc, args=(resultQueue, storeQueue))
    store_proc = Process(target=server.store_proc, args=(storeQueue,))
    url_manager_proc.start()
    result_proc.start()
    store_proc.start()

    server_manager.get_server().serve_forever()





























