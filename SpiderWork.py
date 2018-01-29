# encoding:utf-8

from multiprocessing.managers import BaseManager

class SpiderWork(object):

    def __init__(self):

        BaseManager.register()
