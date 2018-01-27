# encoding:utf-8

import codecs


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
        fout = codecs.open('data.html', mode='w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write("<td> %s <td>" % data[''])
            fout.write('<tr>')
        fout.write('<table>')
        fout.write('<body>')
        fout.write('<html>')
        fout.close()




