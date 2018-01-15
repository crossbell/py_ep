"""
    空气质量计算1.0：
    1.跟进污染物指数计算空气指数
    IAQ = (IAQh-IAQl)*(Cp-BPl)/(BPh-BPl) - IAQl
"""
iaq_index_list = [0, 50, 100, 150, 200, 300, 400, 500]
pt_index_dict = {"PM25": [0, 35, 75, 115, 150, 250, 350, 500],
                 "O3_1": [0, 160, 200, 300, 400, 800, 1000, 1200],
                 "CO_1": [0, 5, 10, 35, 60, 90, 120, 150],
                 "PM10": [0, 50, 150, 250, 350, 420, 500, 600],
                 "NO2_24": [0, 40, 80, 180, 280, 565, 750, 940],
                 "SO2_1": [0, 150, 500, 650, 800, -1, -1, -1],
                 "SO2_24": [0, 50, 150, 475, 800, 1600, 2100, 2620],
                 "NO2_1": [0, 100, 200, 700, 1200, 2340, 3090, 3840],
                 "CO_24": [0, 2, 4, 14, 24, 36, 48, 60],
                 "O3_8": [0, 100, 160, 215, 265, 800, -1, -1]
                 }
def cal_line(IAQh, IAQl, BPh, BPl, Cp):
    """
        线性函数
    """
    return  (float(IAQh)-float(IAQl))*(Cp-float(BPl))/(float(BPh)-float(BPl)) - float(IAQl)

def cal_pt_aqi(pt_name, pt_value):
    """
       计算单个污染物aqi
    """
    global pt_index_dict
    global iaq_index_list
    aqi = -1
    pt_f = float(pt_value)
    # 查找污染物指数区间
    bins_list = pt_index_dict[pt_name]
    for i, bins_value in enumerate(bins_list):
        if i == len(bins_list)-1:
            # 已经超出最大值，不知怎么计算，记为异常点
            aqi = -1
        elif bins_value <= pt_f < bins_list[i+1] :
            # 该污染物指数区间对应 iaq值
            aqi = cal_line(iaq_index_list[i+1], iaq_index_list[i], bins_list[i+1], bins_value, pt_f)
            break
    print('计算{}指数值，输入数值:{}, AQI:{}。'.format(pt_name, pt_value, aqi))
    return aqi

def cal_aqi(pt_list):
    """
        计算传入污染物aqi数值
    """
    global pt_index_dict
    pt_name_list = list(pt_index_dict.keys())
    aqi_list = []
    for i , pt_value in enumerate(pt_list) :
        aqi_list.append(cal_pt_aqi(pt_name_list[i], pt_value))
    return max(aqi_list)



def main():

    print("请输入以下信息，以空格分开")
    # pt_strs = input("(1)PM25,(2)O3_1,(3)CO_1,(4)PM10,(5)NO2_24,(6)SO2_1,(7)SO2_24,(8)NO2_1,(9)CO_24,(10)O3_8:")
    pt_strs = "45 21 32 42 53 12 31 31 10 32"
    pt_list = pt_strs.split(" ")
    aqi = cal_aqi(pt_list)
    print(aqi)

if __name__ == '__main__':
    main()