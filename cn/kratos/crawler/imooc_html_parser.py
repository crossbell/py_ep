'''
    html页面解析器
    作者：liangwang16@creditease
'''
import re
from bs4 import BeautifulSoup as bs
import bs4

class BestUniHtmlParser:

    def __init__(self):
        pass

    def _get_new_urls(self, url, soup):
        return None

    def _get_new_data(self, url, soup):
        """
            定向解析百科页面内容
            <table class="table table-small-font table-bordered table-striped">
        """

        res_list = []
        # table_node = soup.find('table', {'class': "table table-small-font table-bordered table-striped"})
        tr_nodes = soup.find('tbody', {'class': "hidden_zhpm"}).children
        # print(tr_nodes)
        for i, tr_node in enumerate(tr_nodes):
            if not isinstance(tr_node, bs4.element.Tag):
                continue

            tds_nodes = tr_node('td')
            # print(tr_node.prettify())
            res_dict = {}
            res_dict['xh'] = i
            res_dict['name'] = tds_nodes[1].string
            res_dict['score'] = tds_nodes[3].string
            res_list.append(res_dict)
        # print('解析完页面结果:', res_dict)
        return res_list

    def parser_html(self, url, html_context):
        '''
            返回：{title, url, summary}
        '''
        if url is None or html_context is None:
            return
        soup = bs(html_context, 'lxml', from_encoding='utf-8')

        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data