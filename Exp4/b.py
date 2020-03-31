# coding=utf-8
from Crypto.PublicKey import RSA

def qianming(message):
    with open('master-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        # 哈希加密
        digest = SHA.new()
        # 此处进行数字签名
        digest.update(message)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)

    with open('signature.pem', 'wb') as fp1:
        fp1.write(signature)
        fp1.close()
    print(signature)
    print("signature已成功写入signature.pem文件")
    return signature

