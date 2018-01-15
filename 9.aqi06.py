"""
    空气质量计算6.0：
    1.爬虫BeautifulSoup获取空气aqi
"""
from bs4 import BeautifulSoup as bs
import requests

def get_url_html(city_name):
    url = 'http://pm25.in/' + city_name
    req = requests.get(url, timeout=30)
    code = req.status_code
    city_aqi = []
    if code == 200:
        soup = bs(req.text, 'lxml')
        div_list = soup.find_all('div', {'class': 'span1'})
        for pt in div_list:
            div_content = div_list[pt]
            print(div_content)
            value = pt.find('div', {'class': 'value'}).text.strip()
            caption = pt.find('div', {'class': 'caption'}).text.strip()
            city_aqi.append((caption, value))
        # for i in range(8):
        #     div_content = div_list[i]
        #     caption = div_content.find('div', {'class': 'caption'}).text.strip()
        #     value = div_content.find('div', {'class': 'value'}).text.strip()
        #     city_aqi.append((caption, value))
    return city_aqi

def main():
    # city_name = input("输入城市名拼音：")
    city_name = 'beijing'
    pt_list = get_url_html(city_name)
    print(pt_list)

if __name__ == '__main__':
    main()