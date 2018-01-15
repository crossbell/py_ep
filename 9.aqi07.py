"""
    空气质量计算7.0：
    1.爬虫BeautifulSoup获取空气aqi
    2.获取城市列表
    3.将结果数据保存在csv，json中
"""
from bs4 import BeautifulSoup as bs
import requests
import json
import csv

def get_city_list():
    '''
        获取城市列表
    '''
    url = 'http://pm25.in'
    req = requests.get(url, timeout=30)
    code = req.status_code
    city_list = []
    if code ==200:
        soup = bs(req.text, 'lxml')
        citys_bottm = soup.find_all('div', {'class': 'bottom'})[1]
        city_attr_list = citys_bottm.find_all('a')
        for city_attr in city_attr_list:
            city_name = city_attr.text
            city_letter = city_attr['href']
            city_list.append((city_letter[1:], city_name))
    return city_list

def get_url_html(city_letter):
    '''
        获取城市空气指数
    '''
    url = 'http://pm25.in/' + city_letter
    req = requests.get(url, timeout=30)
    code = req.status_code
    city_tuple = ()

    if code == 200:
        soup = bs(req.text, 'lxml')
        div_list = soup.find_all('div', {'class': 'span1'})
        pt_dict = {'city': city_letter}
        for i in range(8):
            div_content = div_list[i]
            caption = div_content.find('div', {'class': 'caption'}).text.strip()
            value = div_content.find('div', {'class': 'value'}).text.strip()
            pt_dict[caption] = value
        city_tuple = (city_letter, pt_dict)

    return city_tuple

def save_file(city_pt_list):
    with open('aqi/city_aqi.txt', 'w', encoding='utf-8') as f:
        f.write(str(city_pt_list))

def save_json_file(city_pt_list):
    with open('aqi/city_aqi.json', 'w', encoding='utf-8') as f:
        json.dump(city_pt_list, f, ensure_ascii=False)

def save_csv_file(city_pt_list):
    with open('aqi/city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        title_line = list(city_pt_list[0].keys())
        writer.writerow(title_line)
        for line in city_pt_list:
            writer.writerow(line.values())

def main():
    city_list = get_city_list()
    city_pt_list = []
    # count = 0
    for i, city in enumerate(city_list):
        if i % 20 == 0:
            print('正在处理第{}个城市，总技{}个'.format(i+1, len(city_list)))
        pt_tuple = get_url_html(city[0])
        dict_aqi = pt_tuple[1]
        dict_aqi['city'] = city[1]
        city_pt_list.append(dict_aqi)
        # count += 1
        # if count == 5:
        #     break

    save_file(city_pt_list)
    save_json_file(city_pt_list)
    save_csv_file(city_pt_list)

if __name__ == '__main__':
    main()