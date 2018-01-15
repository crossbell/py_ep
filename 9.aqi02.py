"""
    空气质量计算2.0：
    1.JSON文件操作
    2.排序
"""
import json

def process_json(filePath):
    """
        计算传入污染物aqi数值
    """
    f = open(filePath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    # 排序，取前五条记录
    city_list.sort(key=lambda x: x['aqi'])
    top5_list =city_list[:5]
    f.close()
    # 写入文件
    wf = open("aqi/top5_aqi.json", mode='w', encoding='utf-8')
    json.dump(top5_list, wf, ensure_ascii=False)
    wf.close()

def main():
    filePath = "aqi/shanghai_aqi.json"
    process_json(filePath)


if __name__ == '__main__':
    main()