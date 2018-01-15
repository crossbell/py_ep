'''
    爬虫调度器
    作者：liangwang16@creditease.cn
'''
from cn.kratos.crawler import url_download
from cn.kratos.crawler import url_manager
import time
class SpiderManager:

    def __init__(self, parser, outer):
        self.urls = url_manager.URLManager()
        self.downloader = url_download.URLDownload()
        self.parser = parser
        self.outer = outer

    def craw(self, url):
        count = 0
        self.urls.add_url(url)
        while self.urls.has_url():
            time.sleep(2)
            # 获取一待爬取URL
            new_url = self.urls.get_url()
            print(new_url)
            # try:
                # 获取网页内容
            html_context = self.downloader.download(new_url)
            print(html_context)
                # 解析网页内容，返回网页中的URL, 及需要的网页文本
            new_urls, new_data = self.parser.parser_html(new_url, html_context)
            self.urls.add_urls(new_urls)
            self.outer.collect_data(new_data)
            count += 1
            if count == 1000:
                break
            # except :
                # print('解析网页：{}异常:'.format(new_url))
                # self.urls.add_bad_url(new_url)
        self.outer.output_data()
