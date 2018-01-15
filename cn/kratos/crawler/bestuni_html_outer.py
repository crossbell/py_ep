'''
    html内容输出器
    作者：liangwang16@creditease.cn
'''
from cn.kratos.crawler import mongo_util
class BestUniHtmlOuter:
    def __init__(self):
        self.data_list = []

    def collect_data(self, data):
        '''
            数据采集
        '''
        if data is None:
            return
        self.data_list = data
        mu = mongo_util.MongoUtil()
        mu.add_datas('bestuni', self.data_list)

    def output_data(self):
        '''
            输出html表格
        '''
        with open('out/bestuni.html', mode='w', encoding='utf-8') as f:
            f.write('<html>')
            f.write('<body>')
            f.write('<table border=1>')
            f.write('<td>序号</td>')
            f.write('<td width=50>大学</td>')
            f.write('<td width=100>省市</td>')
            f.write('</tr>')
            tplt = "{0:^10}\t{1:^10}\t{2:^10}"
            print(tplt.format('排名', '大学', '得分', chr(12288)))
            for i, item in enumerate(self.data_list):
                f.write('<td>{:^10}</td>'.format(item['xh']))
                f.write('<td>{:^15}</td>'.format(item['name']))
                f.write('<td>{:^10}</td></tr>'.format(item['score']))
                print(tplt.format(item['xh'], item['name'], item['score'], chr(12288)))
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')