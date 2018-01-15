'''
    html页面解析器
    作者：crossbell
'''
import re
from bs4 import BeautifulSoup as bs
import bs4
import requests

class WxHtmlParser:

    def __init__(self):
        pass

    def _get_new_urls(self, url, soup):

        if url is None or re.search('&page=', url) is not None:
            return None
        # <div class="p-fy" id="pagebar_container">
        a_nodes = soup.find('div', {'class': 'p-fy'})('a')
        new_urls = []
        for node in a_nodes:
            print('正在爬取第{}页'.format(node.string))
            new_urls.append(url + '&page={}'.format(node.string))
        print(new_urls)

        return new_urls

    def _get_new_data(self, url, soup):
        """
            解析公众号地址
        """
        res_list = []
        li_nodes = soup.find('ul', {'class': "news-list2"}).children
        for i, li_node in enumerate(li_nodes):
            if not isinstance(li_node, bs4.element.Tag):
                continue

            div_node = li_node('div', {'class': 'txt-box'})[0]
            # print(div_node)
            wx_account_img = li_node.find('img', {'src': re.compile(r'http://img01.sogoucdn.com')})
            # print(wx_account_img['src'])
            wx_account = div_node('p', {'class': 'info'})[0]('label')[0].string
            filename = "out/" + wx_account + ".jpg"

            self.save_img(wx_account_img['src'], filename)
            res_dict = {}
            res_dict['xh'] = i
            res_dict['wx_name'] = div_node.find('p', {'class': 'tit'}).find('a').text
            res_dict['wx_account'] = wx_account
            res_dict['wx_account_img'] = filename
            res_dict['wx_href'] = div_node.find('p', {'class': 'tit'}).find('a')['href']

            wx_summary = ''
            wx_authname = ''
            wx_article = ''
            wx_article_href = ''
            for j in range(len(li_node('dl'))):
                print(li_node('dl')[j].dt.text)
                if '功能介绍' in li_node('dl')[j].dt.text:
                    wx_summary = li_node('dl')[j]('dd')[0].text
                elif '认证' in li_node('dl')[j].dt.text:
                    wx_authname = li_node('dl')[j]('dd')[0].text
                elif '最近文章' in li_node('dl')[j].dt.text:
                    wx_article = li_node('dl')[j]('a')[0].text
                    wx_article_href = li_node('dl')[j]('a')[0]['href']

            res_dict['wx_summary'] = wx_summary
            res_dict['wx_authname'] = wx_authname
            res_dict['wx_article'] = wx_article
            res_dict['wx_article_href'] = wx_article_href

            res_list.append(res_dict)
            print('解析完页面结果:', res_dict)
        return res_list

    def parser_html(self, url, html_context):
        '''
            返回：{title, url, summary}
        '''
        if url is None or html_context is None:
            return

        if re.search('weixin.sogou.com', url) is None:
            return None

        soup = bs(html_context, 'lxml', from_encoding='utf-8')

        # print(soup.prettify())
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def save_img(self, url, filename):
        if url is None:
            return

        with open(filename, 'wb') as f:
            r = requests.get(url)
            f.write(r.content)

def main():
    html_context = """
    <ul class="news-list2"><li id="sogou_vr_11002301_box_0" d="oIWsFt7S3hG1ciw--28_x5V-IpLI">
<div class="gzh-box2">
<div class="img-box">
<a target="_blank" uigs="account_image_0" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1515675387&amp;ver=1&amp;signature=2xy4EKe1nd0p*BB5skxTXv*lyuhUa4184zLkyK-FfNexAF5tA1dzPGlNEbVzzV2XbcrsWs2V-vNX47vFTY0aow=="><span></span><img src="http://img01.sogoucdn.com/app/a/100520090/oIWsFt7S3hG1ciw--28_x5V-IpLI" onload="resizeImage(this,58,58)" onerror="errorHeadImage(this)" style="width: 58px; height: auto; margin-top: 0px;"></a>
</div>
<div class="txt-box">
<p class="tit">
<a target="_blank" uigs="account_name_0" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1515675387&amp;ver=1&amp;signature=2xy4EKe1nd0p*BB5skxTXv*lyuhUa4184zLkyK-FfNexAF5tA1dzPGlNEbVzzV2XbcrsWs2V-vNX47vFTY0aow=="><em><!--red_beg-->宜信<!--red_end--></em></a><i></i>
</p>
<p class="info">微信号：<label name="em_weixinhao">CreditEase2006</label>
<span class="line-s"></span>月发文&nbsp;35&nbsp;篇</p>
</div>
<div class="ew-pop">
<a class="code" href="javascript:void(0)"><img height="24" width="24" src="/new/pc/images/ico_ewm.png"></a><span style="display:none;" class="pop"><i></i>微信扫一扫关注<br>
<img height="104" width="104" src="http://mp.weixin.qq.com/rr?src=3&amp;timestamp=1515675387&amp;ver=1&amp;signature=E3RxIuzhKZPrAfbrDQ44Z9e-wIbQcEFAPTn9PzB1qW1AZ5XOzHMFTT3d9tSp15AksbdTIZ5QBECnY*nhyo1HfswnXr3pRwkc9rnAJMiVREs=" data-id="oIWsFt7S3hG1ciw--28_x5V-IpLI" onerror="qrcodeShowError('http://mp.weixin.qq.com/rr?src=3&amp;timestamp=1515675387&amp;ver=1&amp;signature=E3RxIuzhKZPrAfbrDQ44Z9e-wIbQcEFAPTn9PzB1qW1AZ5XOzHMFTT3d9tSp15AksbdTIZ5QBECnY*nhyo1HfswnXr3pRwkc9rnAJMiVREs=',4,'oIWsFt7S3hG1ciw--28_x5V-IpLI')"><img height="32" width="32" class="shot-img" src="http://img01.sogoucdn.com/app/a/100520090/oIWsFt7S3hG1ciw--28_x5V-IpLI" onerror="errorHeadImage(this)"></span>
</div>
</div>
<dl>
<dt>功能介绍：</dt>
<dd><em><!--red_beg-->宜信<!--red_end--></em>公司官方账号</dd>
</dl>

</li></ul>
    """
    url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&page=3'.format('宜信')
    wx_parser = WxHtmlParser()
    new_urls, new_data = wx_parser.parser_html(url, html_context)
    print(new_urls)
if __name__ == '__main__':
    main()