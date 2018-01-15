'''
    日期处理，判断一年第几天 3.0
    1.判断闰年函数
    2.使用set集合
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

    days = day
    # 31天的月份
    _31_days_p_month_set = {1, 3, 5, 7, 8, 10, 12}
    # 30天的月份
    _30_days_p_month_set = {4, 6, 9, 11}
    for i in range(1, month):
        if i in _31_days_p_month_set:
            days += 31
        elif i in _30_days_p_month_set:
            days += 30
        else:
            days += 28
    if (is_leap_year(year) and (month > 2 ) ):
        days += 1

    print("输入日期{}，是一年的第{}天".format(input_date, days))

if __name__ == '__main__':
    main()