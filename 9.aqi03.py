"""
    空气质量计算3.0：
    1.JSON文件操作
    2.排序
    3.csv文件操作：top5存储为csv
"""
import json
import csv

def process_file(filepath):

    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    # 排序，取前五条记录
    city_list.sort(key=lambda x: x['aqi'])
    top5_list =city_list[:5]
    f.close()

    # 写入json文件
    wf = open("aqi/top5_aqi.json", mode='w', encoding='utf-8')
    json.dump(top5_list, wf, ensure_ascii=False)
    wf.close()

    # 写入csv文件
    cf = open('aqi/top5_aqi.csv', mode='w', encoding='utf-8', newline='')
    writer = csv.writer(cf)

    writer.writerow(list(top5_list[0].keys()))
    for line in top5_list:
        writer.writerow(list(line.values()))

def main():
    filepath = "aqi/shanghai_aqi.json"
    process_file(filepath)


if __name__ == '__main__':
    main()