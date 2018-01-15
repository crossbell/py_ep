"""
    空气质量计算5.0：
    1.爬虫requests获取空气aqi
"""
import requests

def get_url_html(url):
    req = requests.get(url, timeout=30)
    code = req.status_code
    context = ''
    if code == 200:
        context = req.text
    return context

def main():
    city_name = input("输入城市名拼音：")
    url = 'http://pm25.in/' + city_name
    context = get_url_html(url)
    find_str = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = context.find(find_str) + len(find_str)
    aqi_val = context[index:index+2]
    print("{}空气质量AQI{}".format(city_name,aqi_val))

if __name__ == '__main__':
    main()