"""
BMR计算器，实现代谢计算2.0
1.用户输入参数，通过空格分离
2.str的分隔函数
"""
def calBmr(age,height,weigth,gender):
    bmr= 0
    if gender == '男':
        bmr = 13.7 * weigth + 5.0 * height - 6.8 * age + 66
    elif gender == '女':
        bmr = 9.6 * weigth + 1.8 * height - 4.7 * age + 655
    else:
        bmr = -1

    if bmr == -1:
        print("性别输入错误，请重新输入！")
    else:
        print("性别:{}，年龄:{},身高:{}，体重:{}，BRM={}".format(gender,age,height,weigth,bmr))

def main():
    str = input("请输入计算数据，退出请按Q，继续请按任意键")

    while str!='Q':
        try:
            inputstr = input("1.请输入年龄、身高(cm)、体重(kg)、性别，以空格分开：")
            strs = inputstr.split(' ')
            age = int(strs[0])
            height = float(strs[1])
            weigth = float(strs[2])
            gender = strs[3]
            calBmr(age, height, weigth, gender)
        except ValueError:
            print("输入数据类型错误")
        except IndexError:
            print("输入数据个数错误")
        except:
            print("输入数据格式错误")

        str=input("请输入计算数据，退出请按Q，继续请按任意键")


if __name__ == '__main__':
    main()

