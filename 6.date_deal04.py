'''
    日期处理，判断一年第几天 4.0
    1.判断闰年函数
    2.使用dict字典
'''
from datetime import datetime

def is_leap_year(year):
    '''
    判断是否闰年
    '''
    is_leap_yaar = False
    if (year % 400 == 0) or (year % 100 !=0  and year % 4 ==0) :
        is_leap_yaar = True
    return is_leap_yaar

def main():
    input_str = input("请输入日期（yyyy-mm-dd）:")
    input_date = datetime.strptime(input_str, '%Y-%m-%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day
    print(input_date)

    days  = day
    days2 = day
    # 31天的月份
    days_month_dict = {1: 31,
         2: 28,
         3: 31,
         4: 30,
         5: 31,
         6: 30,
         7: 31,
         8: 31,
         9: 30,
         10: 31,
         11: 30,
         12: 31}
    for i in range(1, month):
        days += days_month_dict[i]

    days_month_dicts = {31: [1, 3, 5, 7, 8, 10, 12],
                       30: [4, 6, 9, 11],
                       28: [2]}

    for i in range(1, month):
        if i in days_month_dicts[31]:
            days2 += 31
        elif i in days_month_dicts[30]:
            days2 += 30
        else:
            days2 += 28
    if (is_leap_year(year) and (month > 2 ) ):
        days += 1
        days2 += 1

    print("输入日期{}，是一年的第{}天".format(input_date, days2))

if __name__ == '__main__':
    main()