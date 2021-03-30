import hashlib

def sha1sum(filename):
    h=hashlib.sha1()
    with open (filename,'rb') as file:
        chunk  = 0
        while chunk != b'':
            chunk = file.read(2048)
            h.update(chunk)
    return h.hexdigest()

def sha256sum(filename):
    h=hashlib.sha256()
    with open (filename,'rb') as file:
        chunk  = 0
        while chunk != b'':
            chunk = file.read(2048)
            h.update(chunk)
    return h.hexdigest()

def md5sum(filename):
    h=hashlib.md5()
    with open (filename,'rb') as file:
        chunk  = 0
        while chunk != b'':
            chunk = file.read(2048)
            h.update(chunk)
    return h.hexdigest()

def sha224sum(filename):
    h=hashlib.sha224()
    with open (filename,'rb') as file:
        chunk  = 0
        while chunk != b'':
            chunk = file.read(2048)
            h.update(chunk)
    return h.hexdigest()

def sha384sum(filename):
    h=hashlib.sha384()
    with open (filename,'rb') as file:
        chunk  = 0
        while chunk != b'':
            chunk = file.read(2048)
            h.update(chunk)
    return h.hexdigest()
