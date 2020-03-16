# coding=utf-8
# 加密文件
def jiamiText(path):
    path = Path(path)  # 此处为密钥路径
    jiamipath = input("请输入加密文件路径：")
    jiemipath = input("请输入加密后文件路径：")
    # 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。
    with open(path, 'wt', encoding='utf-8') as fp0, \
            open(jiamipath, 'rt', encoding='utf-8') as fp1, \
            open(jiemipath, 'wt', encoding='utf-8') as fp2:
        # 读取加密文件内容
        jiamitxt = jiami(fp1.read())

        # 返回加密后的密文，密钥,并写入文件中
        miwen1, miyao1 = jiamitxt['miwen'], jiamitxt['miyao']
        json.dump(miyao1, fp0)
        json.dump(miwen1, fp2)


# 解密文件
def jiemiText():
    miyao_path = input("请输入密钥路径：")
    miwen_path = input("请输入待解密文件路径：")
    jiemi_path = input("请输入解密后文件路径：")
    with open(miwen_path, 'rt', encoding='utf-8') as fp1, \
            open(miyao_path, 'rt', encoding='utf-8') as fp2, \
            open(jiemi_path, 'wt', encoding='utf-8') as fp3:
        # 解密操作
        jiemitxt = jiemi(json.load(fp2), json.load(fp1))
        fp3.write(jiemitxt)


path = input("要写入的密钥路径：")
jiamiText(path)
jiemiText()
