'''
模拟掷骰子v4.0
    1.模拟两个骰子
    2.科学计数
'''
import numpy as np
import matplotlib.pyplot as plt

#中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    #掷骰子 次数
    times= 10000
    # 初始化2次骰子结果：区间2-12
    rall1_result = np.random.randint(1, 7, size=times)
    rall2_result = np.random.randint(1, 7, size=times)
    rall_list = rall1_result + rall2_result

    hist, bins = np.histogram(rall_list, bins=range(2, 14), normed=1)
    result_dict = dict(zip(bins,hist))
    print(result_dict)
    tick_lables = ['2点', '3点', '4点', '5点', '6点',
                   '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_lables)

    plt.hist(rall_list, bins=range(2, 14), edgecolor='black',normed=1, linewidth=0.3, color='blue',rwidth=0.8)
    plt.title('柱状图')
    plt.xlabel('点数')
    plt.ylabel('次数频率')
    plt.show()

if __name__ == '__main__':
    main()