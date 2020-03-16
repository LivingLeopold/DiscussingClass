# -*- coding:utf-8 -*-
def jiami(s):
    #字符串编码为字节串
    s=s.encode()
    length=len(s)
    #转换为整数
    zhengshu=int.from_bytes(s, byteorder='big',signed='true')
    #整数与密钥进行异或运算生成密文
    miyao=generateIntM(length)
    miwen=miyao^zhengshu
    return {'miyao': miyao,'miwen': miwen}
