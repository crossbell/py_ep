'''
模拟掷骰子v2.0
    1.模拟两个骰子
    2.数据可视化:输出散点图
'''
import random
import matplotlib.pyplot as plt

def rool():
    '''
    返回骰子点数
    :return:
    '''
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    #掷骰子 次数
    times= 10000
    # 初始化2次骰子结果：区间2-12
    result_list = [0]*11
    # 筛子数
    dice_list = range(2, 13)
    # 合并打包
    result_dict = dict(zip(dice_list, result_list))


    for i in range(times):
        result = rool()
        result_dict[result] += 1

    print(result_dict)
    rate_list=[]
    for i, x in result_dict.items():
        print("点数{}--次数{}--频率{}".format(i, x, x/times))
        rate_list.append(10**6*3.14*x/times**2)
    # 数据可视化输出
    plt.scatter(result_dict.keys(), result_dict.values(), s=rate_list, c='blue', alpha=0.5)
    plt.show()

if __name__ == '__main__':
    main()