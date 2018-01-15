'''
    日期处理，判断一年第几天 5.0
    使用datetime函数
'''
from datetime import datetime

def main():
    input_str = input("请输入日期（yyyy-mm-dd）:")
    input_date = datetime.strptime(input_str, '%Y-%m-%d')

    days = input_date.strftime('%j')

    print("输入日期{}，是一年的第{}天".format(input_date, days))

if __name__ == '__main__':
    main()