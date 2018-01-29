# encoding:utf-8

import Queue
from multiprocessing.managers import BaseManager

class SpiderServer(object):

    def __init__(self):
        self.url_queue = Queue.Queue()
        self.result_queue = Queue.Queue()









