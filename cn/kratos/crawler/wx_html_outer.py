'''
    html内容输出器
    作者：liangwang16@creditease.cn
'''
from cn.kratos.crawler import mongo_util

class WxHtmlOuter:
    def __init__(self):
        self.data_list = []

    def collect_data(self, data):
        '''
            数据采集
        '''
        if data is None:
            return
        self.data_list += data
        mu = mongo_util.MongoUtil()
        mu.add_datas('wx', self.data_list)

    def output_data(self):
        '''
            输出html表格
        '''
        with open('out/wx_account.html', mode='w', encoding='utf-8') as f:
            f.write('<html>')
            f.write('<body>')
            f.write('<table border=1>')
            f.write('<td>序号</td>')
            f.write('<td width=10>公众号</td>')
            f.write('<td width=10>账户</td>')
            f.write('<td width=10>头像</td>')
            f.write('<td width=10>认证</td>')
            f.write('<td width=10>功能</td>')
            f.write('<td width=10>最新文章</td>')
            f.write('</tr>')
            for i, item in enumerate(self.data_list):
                print(item)
                f.write('<tr>')
                f.write('<td>{}</td>'.format(i+1))
                f.write('<td><a href="{}">{}</a></td>'.format(item['wx_href'], item['wx_name']))
                f.write('<td>{}</td>'.format(item['wx_account']))
                f.write('<td><img src="{}"/></td>'.format(item['wx_account_img'][4:]))
                f.write('<td>{}</td>'.format(item['wx_authname']))
                f.write('<td>{}</td>'.format(item['wx_summary']))
                # f.write('<td>{}</td>'.format(item['wx_article']))
                f.write('<td><a href={}>{}</a></td>'.format(item['wx_article_href'], item['wx_article']))
                f.write('</tr>')
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')