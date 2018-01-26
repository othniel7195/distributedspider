# encoding:utf-8

class DataSave(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):

        if data is not None:
            self.datas.append(data)

    def output_data(self):
        """
        输出数据
        :return: 
        """
        pass