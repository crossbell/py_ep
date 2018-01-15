#汇率换算，支持人民币及美元互换
cur_str = input("请输入换算的金额：")
print(cur_str)
#单位
unit = cur_str[-3:]
#金额
cur_amt = float(cur_str[:-3])
#汇率
RATE = 6.67
change_amt = 0
if(unit=='RMB'):
    change_amt = cur_amt/RATE
    print("换算后金额：", change_amt)
elif(unit=='USD'):
    change_amt = cur_amt * RATE
    print("换算后金额：", change_amt)
else:
    print("不支持该币种换算")
