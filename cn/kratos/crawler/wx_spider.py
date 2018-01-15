'''
    微信公众号spider
    作者：liangwang16@creditease.cn
'''
from cn.kratos.crawler import wx_html_outer
from cn.kratos.crawler import wx_html_parser
from cn.kratos.crawler import spider_manager

def main():
    weixin_account = '财富技术'
    url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8'.format(weixin_account)

    wx_spider = spider_manager.SpiderManager(wx_html_parser.WxHtmlParser(), wx_html_outer.WxHtmlOuter())
    wx_spider.craw(url)

if __name__ == '__main__':
    main()