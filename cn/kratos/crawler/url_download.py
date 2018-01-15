'''
    URL下载器
    作者：crossbell
'''
import requests

class URLDownload:
    def __init__(self):
        pass

    def download(self, url):
        """
            下载URL返回网页内容
        """
        print('正在爬取:{} 内容'.format(url))
        if url is None:
            return

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Cookie": "IPLOC=CN1100; SUID=B8A6FE652E08990A0000000059688C91; SUV=00BC555A65FEA6B859688C92E218A537; LSTMV=266%2C24; LCLKINT=6162; ABTEST=5|1515585250|v1; SNUID=4E510993F6F2959D4788F69AF7E86727; weixinIndexVisited=1; JSESSIONID=aaaheWU0tJ9CW-UC2Ladw; sct=9",
            "Host": "weixin.sogou.com",
            "Referer": "http://weixin.sogou.com/weixin?query=%E5%AE%9C%E4%BF%A1&_sug_type_=&s_from=input&_sug_=n&type=1&page=7&ie=utf8",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
        }

        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'ABTEST=0|1515670136|v1; PHPSESSID=dc74qi8hv8ct4pou0mpnmqrkc0; JSESSIONID=aaaMyWvDgTkSl9OVXAKdw; SUV=0059271B65FEA6B85A00599A9BE8A622; CXID=DF1BE1D3B75357C9CD2747AE281325CB; SUID=B8A6FE651810990A00000000596586FA; IPLOC=CN1100; SUIR=B15C125933316A25B55CDC75344FE6D6; SNUID=3E2178E38782E5F9F3190EC487A84F45; sct=3; usid=hs176lQ2fgLthuXw',
            'Referer':'http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E5%AE%9C%E4%BF%A1&ie=utf8&_sug_=n&_sug_type_='
        }

        resp = requests.request('get', url, timeout=30, headers=headers, allow_redirects=True)
        resp.encoding = 'utf-8'
        html = resp.text
        # print(html)
        if resp.status_code != 200:
            return
        return html
