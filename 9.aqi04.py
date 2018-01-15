"""
    空气质量计算4.0：
    1.自动判断文件类型
    2.使用with语句自动关闭文件
    3.csv文件操作：top5存储为csv
    4.自动判断文件扩展名
"""
import json
import csv
import os

def process_csv_file(filepath):

    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))


def process_json_file(filepath):

    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
        print(city_list)

def main():
    filepath = input("输入文件名：")
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        process_json_file(filepath)
    elif file_ext == '.csv':
        process_csv_file(filepath)
    else:
        print("不支持{}扩展名".format(file_ext))

if __name__ == '__main__':
    main()