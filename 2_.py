import jwt

from common import something, secret

data_encoded = jwt.encode(something, secret)
print(data_encoded, jwt.decode(
    data_encoded,
    secret, 
    algorithms=['HS256']))
