# coding=utf-8

string1 = "路漫漫其修远兮，吾将上下而求索。"
string2 = "Never put off until tomorrow what may be done today."
#加密
JAM=jiami(string1)
print(JAM)
#解密
JEM=jiemi(JAM['miwen'],JAM['miyao'])
print(JEM)

#字符串2
JAM2=jiami(string2)
print(JAM2)
JEM2=jiemi(JAM2['miwen'],JAM2['miyao'])
print(JEM2)
