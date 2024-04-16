from pathlib import Path
from pickle import dump

import openssh_key.private_key_list as pkl
import cryptography.hazmat.primitives.asymmetric.rsa as rsa

home = Path.home()

# pk_sk_pair = pkl.PrivateKeyList.from_string(open('test_id_ed25519').read(), passphrase='secret_passphrase')

# pk_sk_pair = pkl.PrivateKeyList.from_string(open(home/ '.ssh' / 'id_rsa').read())
                                                                                                  
# sk_list = pkl.PrivateKeyList.from_list([pk_sk_pair], cipher='aes256-ctr', kdf='bcrypt')                                                                                                  
# private_key = sk_list.convert_to(rsa.RSAPrivateKey)
# public_key = sk_list.convert_to(rsa.RSAPublicKey)

pk_sk_pair = pkl.PublicPrivateKeyPair.generate('ssh-rsa')
with open ('pair.pkl', 'wb') as f:
    dump(pk_sk_pair, f)

# private_key = pk_sk_pair.private.params.convert_to(rsa.RSAPrivateKey)
# print(pk_sk_pair.public.pack_public_string())

# message = b""

# ciphertext = public_key.encrypt(
#     message,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )
