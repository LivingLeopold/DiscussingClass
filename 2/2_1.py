# -*- coding:utf-8 -*-
import  secrets

def generateM(L):
    bys=secrets.token_bytes(L)  #返回包含nbytes个字节的字节字符串。
    # 转化成整数M
    # 只能用这个函数，用decode编码处理不了
    M=int.from_bytes(bys,byteorder='little',signed='true')
    return  M

print(generateM(10))
