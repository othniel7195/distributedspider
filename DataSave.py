# encoding:utf-8


class DataSave(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):

        if data is not None:
            self.datas += data

    def output_data(self):
        """
        输出数据
        :return: 
        """
        for data in self.datas:
            time = data['time']
            cation = data['cation']
            money = data['money']
            desc = data['describe']
            print "%s\n%s\n%s\n%s\n\n\n" %(time, cation, money, desc)






