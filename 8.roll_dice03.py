'''
模拟掷骰子v3.0
    1.模拟两个骰子
    2.数据可视化:输出直方图
'''
import random
import matplotlib.pyplot as plt

#中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

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
    result_list = []
    for i in range(times):
        result_list.append( rool())
    print(result_list)
    # 数据可视化输出
    plt.hist(result_list, bins=range(2, 14), edgecolor='black',normed=1, linewidth=0.3, color='red')
    plt.title('柱状图')
    plt.xlabel('点数')
    plt.ylabel('次数频率')
    plt.show()

if __name__ == '__main__':
    main()