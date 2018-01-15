'''
    URL管理器

    作者：crossbell
'''
from cn.kratos.crawler import mongo_util

class URLManager:

    def __init__(self):
        self.new_urls = []
        self.old_urls = set()
        self.bad_urls = set()
        self.mu = mongo_util.MongoUtil()

    def add_url(self, url):
        '''
            添加url
        '''
        if url is None:
            return
        if url not in set(self.new_urls) and url not in self.old_urls:
            self.new_urls.append(url)
        url_dict = {}
        url_dict["url"] = url
        self.mu.add_data('urls_new', url_dict)

    def add_urls(self, urls):
        '''
            批量添加urls
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_url(url)
        print('当前URL数量:{} '.format(len(self.new_urls)))

    def has_url(self):
        """判断是否还有待爬取URL"""
        return len(self.new_urls) != 0

    def get_url(self):
        '''
            取出一url
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        record = self.mu.find_data('urls_new', None)
        print(record["url"])
        self.mu.add_data('urls_old', record["url"])
        self.mu.del_data('urls_new', record["url"])

        return new_url

    def add_bad_url(self, bad_url):
        '''
            添加爬取失败的url
        '''
        if bad_url is None:
            return
        if bad_url not in self.new_urls and bad_url not in self.old_urls:
            self.bad_urls.add(bad_url)
        url_dict = {}
        url_dict["url"] = bad_url
        self.mu.add_data('urls_bad', url_dict)