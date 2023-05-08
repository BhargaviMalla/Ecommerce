from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def admintoken(email,seconds):
    s=Serializer('*36@#y4vchbhchbh',seconds)
    return s.dumps({'admin':email}).decode('utf-8')
