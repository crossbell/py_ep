'''
    判断密码强弱v1.0
    1.密码需大于8位
    2.密码需包含数字
    3.密码需包含字母
    4.尝试次数不能超过5次
    5.将密码保存到文件中
    6.从文件中读取密码
    7.class
'''

class FileTools:
     def __init__(self, filepath):
         self.filepath = filepath

     def openFile(self):
         f = open(self.filepath, 'r')
         lines = f.readlines()
         f.close()
         return lines

     def writeFile(self, lines):
         f = open(self.filepath, 'a')
         f.write(lines)
         f.close()

class PasswordTools:
    def __init__(self, password_str):
        self.password_str = password_str
        self.strength_level = 0

    def is_has_char(self):
        '''
            判断函数是否包含字母
        '''
        is_has = False
        for cc in self.password_str:
            if cc.isalpha() :
                is_has = True
                break
        return is_has

    def is_has_num(self):
        '''
            判断函数是否包含数字
            :param password_str:
            :return is_has:
            '''
        is_has = False
        for cc in self.password_str:
            if cc.isnumeric():
                is_has = True
                break
        return is_has

    def check_str(self):
        if len(self.password_str) >= 8:
            self.strength_level += 1
        else:
            print("密码要求长度至少8位")

        if self.is_has_char():
            self.strength_level += 1
        else:
            print("密码要求必须包含字母")

        if self.is_has_num():
            self.strength_level += 1
        else:
            print("密码要求必须包含数字")

def main():
    times= 5
    while times > 0 :
        password_str = input("请输入密码：")

        # 调用密码检测工具类
        pt = PasswordTools(password_str)
        pt.check_str()
        level_dict = {0: '弱', 1: '较弱', 2: '中', 3: '强'}

        # 调用密码保存工具类
        file_tools = FileTools("words.txt")
        file_tools.writeFile("\n密码：{}，强度：{}".format(pt.password_str, level_dict[pt.strength_level]))

        print(file_tools.openFile())
        if pt.strength_level == 3:
            print("密码强度合格")
            break
        else:
            print("密码强度不合格")
            times -= 1
    if times <= 0:
        print('密码输入过多，超过5次')


if __name__ == '__main__':
    main()