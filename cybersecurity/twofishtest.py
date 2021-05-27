# %%
import binascii
from twofish import Twofish

# %%
T = Twofish(b'*ioboal*')
x = T.encrypt(b'DAMBIRANJINRIOIS')
key = binascii.unhexlify('8CACBE276491F6FF4B1EC0E9CFD52E76')
# t = Twofish(key)
# cipher_text = T.encrypt('deadbeaf12345678')
# plain_text = t.decrypt(cipher_text)

print(T)
print(x)
print(T.decrypt(x).decode())
print(Twofish(b'rafi').encrypt(b'RAFIAHMADGGMasUL'))
print(Twofish(b'rafi').decrypt(Twofish(b'rafi').encrypt(b'RAFIAHMADGGMasUL')).decode())