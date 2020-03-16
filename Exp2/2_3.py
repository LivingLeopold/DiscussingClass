# coding=utf-8
def jiemi(miwen,miyao):
    afterJiemi=miwen^miyao
    #计算密文的长度，注意这里的+7/8
    length=int((afterJiemi.bit_length()+7)/8)
    #转化成字节流
    afterJiemi=int.to_bytes(afterJiemi,length,byteorder='big',signed='true')
    #解码成字符串
    afterJiemi=afterJiemi.decode()
    return  afterJiemi
