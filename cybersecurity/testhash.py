import hashfile as hs
import hashlib

message = hs.md5sum("cybersecurity/halo.txt")
print("md5:", message)

message2= hs.sha256sum("cybersecurity/halo.txt")
print("sha256:", message2)

message3= hs.sha1sum("cybersecurity/halo.txt")
print("sha1:", message3)

message4 = "Hai nama saya Epic Gilgameshs".encode()
print("md5:", hashlib.md5(message4).hexdigest())

message5 = "Hai nama saya Epic Gilgameshs".encode()
print("sha256:", hashlib.sha256(message5).hexdigest())

message6 = "Hai nama saya Epic Gilgameshs".encode()
print("sha1:", hashlib.sha1(message6).hexdigest())