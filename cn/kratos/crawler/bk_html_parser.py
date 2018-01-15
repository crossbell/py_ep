'''
    html页面解析器
    作者：crossbell
'''
import re
from bs4 import BeautifulSoup as bs4
from urllib import parse

class BkHtmlParser:

    def __init__(self):
        pass

    def _get_new_urls(self, url, soup):
        """
            定向解析页面新URL
        """
        new_urls = set()
        links = soup.find_all('a', {'href': re.compile(r'item')})
        for link in links:
            new_url = 'https://baike.baidu.com' + link['href']
            # urlparse.urljoin(url, new_url)
            new_urls.add(parse.unquote(new_url))
        return new_urls

    def _get_new_data(self, url, soup):
        """
            定向解析百科页面内容
        """
        res_dict = {}
        title_node = soup.find('dd', {'class': "lemmaWgt-lemmaTitle-title"}).find('h1')
        summary_nodes = soup.find('div', {'class': "lemma-summary"}).find_all('div', {'class': 'para'})
        summary_str = ''
        for nodes in summary_nodes:
            summary_str += nodes.text

        res_dict['words'] = title_node.text
        res_dict['url'] = url
        res_dict['sumary'] = summary_str
        print('解析完页面结果:', res_dict)
        return res_dict

    def parser_html(self, url, html_context):
        '''
            返回：{title, url, summary}
        '''
        if url is None or html_context is None:
            return

        if re.search('baike.baidu.com/item', url) is not None:
            return None

        soup = bs4(html_context, 'html.parser', from_encoding='utf-8')

        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data
