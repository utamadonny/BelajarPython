import hashlib

def hash_file(filename):
    h=hashlib.sha1()
    with open (filename,'rb') as file:
        chunk  = 0
        while chunk != b'':
            chunk = file.read(2048)
            h.update(chunk)
    return h.hexdigest()

message = hash_file("cybersecurity/halo.txt")
print("sha1:", message)

message2= "cybersecurity/halo.txt".encode()
print("sha1:", hashlib.sha1(message2).hexdigest())

message3= "cybersecurity/halo.txt".encode()
print("sha1:", hashlib.sha1(message3).hexdigest())

message4 = "print(\"ha1\", hashlib.sha1(message2).hexdigest())".encode()
print("md5:", hashlib.md5(message4).hexdigest())

message5 = "print(\"ha1\", hashlib.sha1(message2).hexdigest())".encode()
print("md5:", hashlib.md5(message5).hexdigest())

message6 = "Hai nama saya Epic Gilgameshs".encode()
print("sha1:", hashlib.sha1(message6).hexdigest())