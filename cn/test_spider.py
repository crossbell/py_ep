import  requests
from bs4 import BeautifulSoup as bs

def main():
    url = 'http://z.cn'
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }
    rep = requests.get(url, timeout=30, headers=headers, allow_redirects=True)
    print(rep.history[1].url)
    print(rep.headers)


if __name__ == '__main__':
    main()