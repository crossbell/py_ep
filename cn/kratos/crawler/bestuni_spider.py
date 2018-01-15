'''
    最好大学spider
    作者：crossbell
'''
from cn.kratos.crawler import bestuni_html_outer
from cn.kratos.crawler import bestuni_html_parser
from cn.kratos.crawler import spider_manager


def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    bestuni_spider = spider_manager.SpiderManager(bestuni_html_parser.BestUniHtmlParser(), bestuni_html_outer.BestUniHtmlOuter())
    bestuni_spider.craw(url)

if __name__ == '__main__':
    main()