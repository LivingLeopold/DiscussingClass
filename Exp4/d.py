with open("data.txt", 'r') as f1:
    message = f1.read()

message = message.encode()
signature = qianming(message)
qianzheng(message, signature)