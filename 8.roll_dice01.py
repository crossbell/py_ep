'''
模拟掷骰子v1.0

'''
import random
def rool():
    '''
    返回骰子点数
    :return:
    '''
    return random.randint(1, 6)

def main():
    #掷骰子 次数
    times= 10000
    # 初始化骰子
    result_list = [0]*6
    print(result_list)
    for i in range(times):
        result = rool()
        result_list[result-1] += 1
    for i, x in enumerate(result_list):
        print("点数{}--次数{}--频率{}".format(i, x , x/times))


    print(result_list)
if __name__ == '__main__':
    main()