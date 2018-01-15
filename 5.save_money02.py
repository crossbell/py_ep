"""
52周存钱计划2.0
1.增加用户输入日期，判断是一年中第几周，然后输出
"""
import  math
from datetime import datetime

save_moneys =0
def cal_weeks_money(weeks,base_week_amt,inc_week_amt):
    global  save_moneys
    # 每周存钱记录
    week_money_list = []
    # 每周累计存钱记录
    save_money_list = []
    week_money = base_week_amt
    for i in range(weeks):
        week_money_list.append(week_money)
        save_moneys = math.fsum(week_money_list)
        save_money_list.append(save_moneys)
        print("第{}周存入{}元，累计存入{}元".format(i+1, week_money, save_moneys))
        week_money += inc_week_amt

    return week_money_list, save_money_list
def main():

    str = input("请输入计算数据，退出请按Q，继续请按任意键")
    while str != 'Q':
        params = input("请您输入存钱周数、每周存钱基数、每周递增数，以空格分隔：").split(' ')
        str_param_date = input("请您输入日期[yyyy-mm-dd]：")
        param_date = datetime.strptime(str_param_date, '%Y-%m-%d')

        try:
            weeks = int(params[0])
            base_week_amt = float(params[1])
            inc_week_amt = float(params[2])
            i = param_date.isocalendar()[1]
            #调用每周存钱方法
            week_money_list, save_money_list = cal_weeks_money(weeks, base_week_amt, inc_week_amt)
            print('-------------------------------------')
            print('第{}周存钱{}元，累计存钱{}元'.format(i, week_money_list[i-1], save_money_list[i-1]))
        except:
            print("输入数据错误，请重新输入")
        str = input("请输入计算数据，退出请按Q，继续请按任意键")

if __name__ == '__main__':
    main()