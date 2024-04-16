import jwt

from common import something
from _3_ import private_key, public_key

data_encoded = jwt.encode(something, private_key, 'RS256')
print(data_encoded)
print(jwt.decode(data_encoded, public_key, ['RS256']))

