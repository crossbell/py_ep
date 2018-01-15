'''
    百度百科spider
    作者：crossbell
'''
from cn.kratos.crawler import bk_html_outer
from cn.kratos.crawler import bk_html_parser
from cn.kratos.crawler import spider_manager

def main():
    url = 'https://baike.baidu.com/item/宜信'
    bk_spider = spider_manager.SpiderManager(bk_html_parser.BkHtmlParser(), bk_html_outer.BkHtmlOuter())
    bk_spider.craw(url)

if __name__ == '__main__':
    main()