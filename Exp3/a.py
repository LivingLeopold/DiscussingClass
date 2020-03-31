import random
import string
import re
import zipfile
import os

def rand_generator( L ):
    s = ''
    for _ in range(L):
        s += random.choice(string.ascii_letters + string.digits)
        print(s)
    return s

def examiner( P ):
    pattern = "^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{8,}$"
    if re.match(pattern,P) == None:
        return False
    else:
        return True

def unzip(path , pwd ):
    try:
        zipFile = zipfile.ZipFile(path)
        zipFile.extractall("/Users/living/PycharmProjects/DiscussingClass/",pwd=pwd)
    except Exception :
        return False
    else:
        return True

unzip("/Users/living/PycharmProjects/DiscussingClass/Exp3/a.py.zip","123456")


