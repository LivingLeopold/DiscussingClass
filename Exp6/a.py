# coding=utf-8
from os.path import isdir, join, splitext, getsize
from os import remove, listdir
import sys

# 指定要删除的文件类型
filetypes = ['.tmp', '.log', '.obj', '.txt']

def delCertainFiles(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)
        elif splitext(temp)[1] in filetypes or getsize(temp)==0:
            # 删除指定类型的文件或大小为 0 的文件
            remove(temp)
            print(temp, ' deleted....')
directory = sys.argv[1]
delCertainFiles(directory)