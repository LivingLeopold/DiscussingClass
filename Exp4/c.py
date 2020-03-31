# coding=utf-8
#验证签名过程
from Crypto.PublicKey import RSA
def qianzheng(message,signature):
       with open('master-public.pem') as f:
              key = f.read()
              rsakey = RSA.importKey(key)
              verifier = Signature_pkcs1_v1_5.new(rsakey)
              digest = SHA.new()
              # Assumes the data is base64 encoded to begin with
              digest.update(message)
              is_verify = verifier.verify(digest, base64.b64decode(signature))

       print(is_verify)
