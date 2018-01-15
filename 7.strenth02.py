'''
    判断密码强弱v1.0
    1.密码需大于8位
    2.密码需包含数字
    3.密码需包含字母
    4.尝试次数不能超过5次
    5.将密码保存到文件中
    6.从文件中读取密码
'''


def is_has_char(password_str):
    '''
        判断函数是否包含字母
    '''
    is_has = False
    for cc in password_str:
        if cc.isalpha() :
            is_has = True
            break
    return is_has

def is_has_num(password_str):
    '''
        判断函数是否包含数字
        :param password_str:
        :return is_has:
        '''
    is_has = False
    for cc in password_str:
        if cc.isnumeric():
            is_has = True
            break
    return is_has

def main():
    # times= 5
    # while times >0 :
    #     password_str = input("请输入密码：")
    #     strength_level = 0
    #     if len(password_str) >= 8:
    #         strength_level += 1
    #     else:
    #         print("密码要求长度至少8位")
    #
    #     if is_has_char(password_str):
    #         strength_level += 1
    #     else:
    #         print("密码要求必须包含字母")
    #
    #     if is_has_num(password_str):
    #         strength_level += 1
    #     else:
    #         print("密码要求必须包含数字")
    #
    #     if strength_level == 3:
    #         print("密码强度合格")
    #     else:
    #         print("密码强度不合格")
    #         times -= 1
    #     level_dict = {0: '弱', 1 : '较弱', 2: '中', 3: '强'}
    #     f = open("password.txt", 'a')
    #     f.write("\n密码：{}，强度：{}".format(password_str, level_dict[strength_level]))
    #     f.close()
    # print('密码输入过多，超过5次')
    f = open('password.txt', 'r')
    # print(f.read())
    # print('------------------')
    # print(f.readline())
    # print('------------------')
    print(f.readlines())
    # print('------------------')
    for line in f:
        print(line)
if __name__ == '__main__':
    main()