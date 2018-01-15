'''
    日期处理，判断一年第几天
    1.判断闰年函数
    2.使用元组tuple
    3.
'''
from datetime import datetime

def is_leap_year(year):
    is_leap_yaar = False
    if (year % 400 == 0 ) or (year % 100 !=0  and year % 4 ==0) :
        is_leap_yaar =  True
    return is_leap_yaar

def main():
    input_str = input("请输入日期（yyyy-mm-dd）:")
    input_date = datetime.strptime(input_str,'%Y-%m-%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day
    print(input_date)
    # 每月天数
    days_p_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # 求和
    days =sum(days_p_month_tup[:month]) + day
    if (is_leap_year(year) and (month > 2 ) ):
        days += 1
    print("输入日期{}，是一年的第{}天".format(input_date, days))

if __name__ == '__main__':
    main()