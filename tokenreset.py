from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer('*36@#y4vchbhchbh',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
