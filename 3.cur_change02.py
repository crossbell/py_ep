"""
汇率转换
"""
def getRate(unit):
    rate = 6.67
    if unit == 'CYN':
        rate = 1/6.67
    elif unit == 'USD':
        rate = 6.67
    else:
        rate = -1
    return rate

def change_cur(cur_amt,rate):
    return  cur_amt * rate

def main():
    cur_str = input("请输入换算金额及单位（退出请输Q）:")
    count = 0
    while (cur_str!='Q'):
        # 单位
        unit = cur_str[-3:]
        # 金额
        cur_amt = eval(cur_str[:-3])
        # 获取汇率
        rate = getRate(unit)
        if rate == -1:
            print("输入币种暂不支持换算，请重新输入")
        else:
            # cur_val = change_cur(cur_amt,rate)
            change_cur_lmd = lambda x: x * rate
            cur_val = change_cur_lmd(cur_amt)
            print("转换后金额：", cur_val)
        count += 1
        print("-------------------------------------------")
        cur_str = input("请输入换算金额及单位（退出请输Q）:")

if __name__ == '__main__':
    main()