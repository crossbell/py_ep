#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'模块的文档注释'
__author__ = 'crossbell'

def is_palindrome(n):
    i = len(str(n))//2
    if str(n)[:i] ==str(n)[-i:]:
        return n
def main():

    n = 123456789
    i = len(str(n))//2
    print(i)
    print(str(n)[:i])
    print(str(n)[-i:])
    output = filter(lambda x: str(x)[:(len(str(x))//2)] ==str(x)[-(len(str(x))//2):], range(1, 5000))
    print(list(output))

    output = filter(is_palindrome, range(1, 1000))
    print(list(output))
    # for n in primes():
    #     if n > 50:
    #         break
    #     print(n)

    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=lambda x:x[1]))
    f1,f2,f3=count()
    print(f1(),f2(),f3())

    while_test(5)



def _odd_iter():
    n =1
    while True:
        n += 2
        yield n

def _not_div(n):
    return lambda x: x % n >0

def primes():
    yield 2
    it = _odd_iter()

    while True:
        n = next(it)
        yield n
        it = filter(_not_div(n),it)

def count():
    # 不会立即执行，只有调用f()函数时才会执行。此时i=3,返回9
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

# def cont2():
#     [i * i for i in range(1, 4)]
#     lambda  x : i * i for i in range(1, 4)

def log(function):
    def wrapper(*args, **kw):
        print('call {}():'.format(function.__name__))
        return function(*args, **kw)
    return wrapper

def while_test(num):
    l = [x * (-1) ** x for x in range(2, num) ]
    result = ''
    for i, x in enumerate(l):
        if i>0 and x>0:
            result += "+"
        result += str(x)
    print(result, '=', sum(l))

if __name__ == '__main__':
    main()
