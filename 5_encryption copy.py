from pathlib import Path
from pickle import load

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import openssh_key.private_key_list as pkl
import cryptography.hazmat.primitives.asymmetric.rsa as rsa

home = Path.home()

# pk_sk_pair = pkl.PrivateKeyList.from_string(open('test_id_ed25519').read(), passphrase='secret_passphrase')

# pk_sk_pair = pkl.PrivateKeyList.from_string(open(home/ '.ssh' / 'id_rsa').read())
                                                                                                  
# sk_list = pkl.PrivateKeyList.from_list([pk_sk_pair], cipher='aes256-ctr', kdf='bcrypt')                                                                                                  
# private_key = sk_list.convert_to(rsa.RSAPrivateKey)
# public_key = sk_list.convert_to(rsa.RSAPublicKey)

with open('pair.pkl', 'rb') as f:
    pk_sk_pair = load(f)
private_key = pk_sk_pair.private.params.convert_to(rsa.RSAPrivateKey)
# print(pk_sk_pair.public.pack_public_string())

correspondent_pubkey = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC5PP2r7e4BYgPbqk9wWTCEfh4oe4/h7NoLiQws9zMkkVvXoejLTHXBW4u9gliKn1Gd7l6FNoL6dzILoiUZ/URb+CzAeTBsPvgGtpcTuXRJ0RpGkTlJcHeN6OELMtLMMXsi68FcpISPBKUZ/zfK+PC6vJzZ18TW08D5cZSP5tdVhDjjFqwJMRZc7C72LZ6Wgn8AAIn26DPBTPAw6QtZVHjQvhnDWClvbIxcnuyGucQ4wt1whtam/vnYPbr+eoR7q5h40xltrhXTHYjR96+hXeMDVMESTjNc2cBGk99QFPONBp5mQlr5XgTrPLddnbVfv0tTnhF8DHbQJQzuTOP9/e3YzGKnxWyvmozQxw0jFa3guCke37OY/Uth1KudZDHw6fBgVFhg6d39sD+SUwBnzdwxeJsV5OMDyL/Uemj4TPETLWwUSlv2JHpiYV4dzTZqGHbUkooTgZ/f+qXxUO/sv5amCoj+wC3pepzLAInnQLcx+trxZAQXrLImqZrXDliOFW7ggKIbffEuaSZceIv0snPB/O8qc5uXAtlEJLmFjDEEvoive9lnIvbY2rD6fbcG+IDXXFkp6+nuNaJLQtKO4l15RNiiZf2rhMMVcMXLzvVUtrwgeh96rWYzjHqdIpwAPMiwspBuZDohUzx5NjXF59rw0vLJgKN/99qxgmMdGBPkBQ=='
public_key = pkl.PublicKey.from_string(correspondent_pubkey).params.convert_to(rsa.RSAPublicKey)

message = b"Something goes wrong..."

ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
# print(ciphertext)

message_encrypted = b'h\xf3\x8ef\x12\x8b\x9e\xd5\xe0\xa2[\x00\xd5H\xc0\xc4]9\xa7Y\x85\xd0H\xe5>\xffI\xb6\x81E\xf8:\xa9j^\x18\x14Y0\x11\x03J\xb3b\x9db\xb1\xb4\xda>\xf6\xaf/\x83\x87\xc5\xe6\x9eu\x9c\xda\x06${\x02\x18\xbf2\xf1\xd2\xcf}\xee-\xfeV\x88\xd7\xc2\x05\xd6\x14-u\xa8u\xb7Q\xdc\x94<\xc70\xa9\x99lYX\x8f.5~\x8ek\xec\x99\x15\x0f\xa1\x94\xf4>%\x17\xb2`\xeb\xea\x81[\xf1\x10\xd6/\x0et\xc9N\xbf\xae~\xef\xb0P+\xf5\xc1\xaf\xc0\x94\xe4\xa0\x98\xf7\xa4*\xf5\x95\xfd\xa7+\x83x\xf4Qt\x11\x02"\xa3\xcd<\x011\xad\xb1\xa9\xa4\x8c\x10\n\x05\xa0k~6\xf9\x047\xb9\xd3\x82\xa0?3\xae\xd1yR\xc6^\xfc B[\xfc\x15?\xd1\x0b\xed\xaf\xeb\xf8\xe8\x94\xfa\xd3f\x1fm\xb92l\xf9\xe6#MY\x1e\xe7\xf3\xbd\xa06\xe9Y\xc1\xe3\xb7\xdeV\x88Y\xc4b\x99\xeb\xac\x93\xbf\xc5\xae\x18yG,\xe3Kt{!\xf5V,D\xfe\xb5@J\xe0\x84m\xbb\x18\xc8vC\xb8*\x15\x8c\x17[\x80x\xd9\xd0P\x13\xd3X.5&1\n\t\xe4\n\x15\x82[\x0e\x06x\x02\xbc]\xbd\x02}U\x02\xca\x1b#X\xa5\xe4\x1f\xd9W\x17\xd2\xbe\x8f\xa1b7\xac\xa5\xcc\x9ebi\x81q\xc6\xea\x10/\x96=\x1a\xed\x89/:\x03m\xc8)}\x98\x80\xd5h\xce\xc8\x19kL\xd3*Sm\xa2\xa4$\xd4\xa2\xba:h\xccE\xc3"\xe2O\xb1\x8f\x03R\x00\xa0\x95\x80\xeb\x0c\xda\xdd\xb6\x86\xd8_\x0e\xa4t\xaeuH\xee!\xc8\xed\xcb\x10\x95\x98\xd7\xdd7\xeeX\xba\xd7\xc5\x88|2\xdc\xb3Aw(\xb61\xc8\xb4_W\xa6\xad\xd5\x187\x10\x9dV;I\x8b Q\xcf\x80\xa5!\xbfbY\x02L\x99;nJ{8??\x96\xe0\xae7*>g\xae\xe5\xe7\xd4\xd7\x8d\x94\x8c30\xe2C\x89\xa0\xfc\xac\x0b\xb913[N<~\x1f\xa1\xc7C\x05~\x91\xda\xf3E\xb6 \x02\xfa\xe7 \x80%\x9e\x82\x94\xf0E;\xa8\xff\xb0\xbb'

print(private_key.decrypt(
    message_encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
))