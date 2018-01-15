'''
    html内容输出器
    作者：crossbell
'''
from cn.kratos.crawler import mongo_util

class BkHtmlOuter:
    def __init__(self):
        self.data_dict = []

    def collect_data(self, data):
        '''
            数据采集
        '''
        if data is None:
            return
        self.data_dict.append(data)
        mu = mongo_util.MongoUtil()
        mu.add_datas('bk', self.data_dict)

    def output_data(self):
        '''
            输出html表格
        '''
        with open('out\\bk.html', mode='w', encoding='utf-8') as f:
            f.write('<html>')
            f.write('<body>')
            f.write('<table border=1')
            f.write('<td>序号</td>')
            f.write('<td width=50>词条</td>')
            f.write('<td width=100>地址</td>')
            f.write('<td>简介</td>')
            f.write('</tr>')
            for i, item in enumerate(self.data_dict):
                f.write('<tr><td>{}</td>'.format(i+1))
                f.write('<td>{}</td>'.format(item['words']))
                f.write('<td>{}</td>'.format(item['url']))
                f.write('<td>{}</td></tr>'.format(item['sumary']))
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
