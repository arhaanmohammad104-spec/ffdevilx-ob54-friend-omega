from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

da='f2212101'
dec=[f"{i:02x}" for i in range(0x80,0x100)]
x=['1']+[f"{i:02x}" for i in range(1,0x80)]
K1=bytes([101,116,33,120,72,83,97,119,82,94,37,56,74,50,83,53])
IV1=bytes([84,76,82,118,120,100,114,114,117,51,37,80,85,113,65,54])
K2=bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
IV2=bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
def encrypt_packet(t):
    c=AES.new(K1,AES.MODE_CBC,IV1)
    return c.encrypt(pad(bytes.fromhex(t),AES.block_size)).hex()
def decrypt_packet(p):
    c=AES.new(K1,AES.MODE_CBC,IV1)
    return unpad(c.decrypt(bytes.fromhex(p)),AES.block_size).hex()
def encrypt_api(t):
    c=AES.new(K2,AES.MODE_CBC,IV2)
    return c.encrypt(pad(bytes.fromhex(t),AES.block_size)).hex()
def decrypt_api(t):
    c=AES.new(K2,AES.MODE_CBC,IV2)
    return unpad(c.decrypt(bytes.fromhex(t)),AES.block_size).hex()
def Decrypt_ID(d):
    if d and len(d) in(10,8):
        w=128
        for _ in range(int(str(len(d)/2-1)[0])-1):w*=128
        p=[d[i:i+2] for i in range(0,len(d),2)]
        if len(d)==10:
            return str(w*x.index(p[4])+(dec.index(p[1])*128)+dec.index(p[0])+(dec.index(p[2])*128**2)+(dec.index(p[3])*128**3))
        return str(w*x.index(p[3])+(dec.index(p[1])*128)+dec.index(p[0])+(dec.index(p[2])*128**2))
    return None
def Encrypt_ID(n):
    n=int(n);xxx=x;d=dec
    n/=128
    if n>128:
        n/=128
        if n>128:
            n/=128
            if n>128:
                n/=128
                a=int(n);b=(n-a)*128;c=(b-int(b))*128;d1=(c-int(c))*128;e=(d1-int(d1))*128
                return d[int(e)]+d[int(d1)]+d[int(c)]+d[int(b)]+xxx[int(n)]
            a=int(n);b=(n-a)*128;c=(b-int(b))*128;d1=(c-int(c))*128
            return d[int(d1)]+d[int(c)]+d[int(b)]+xxx[int(n)]
def Encrypt(n):
    n=int(n);xxx=x;d=dec
    n/=128
    if n>128:
        n/=128
        if n>128:
            n/=128
            if n>128:
                n/=128
                a=int(n);b=(n-a)*128;c=(b-int(b))*128;d1=(c-int(c))*128;e=(d1-int(d1))*128
                return d[int(e)]+d[int(d1)]+d[int(c)]+d[int(b)]+xxx[int(n)]
            a=int(n);b=(n-a)*128;c=(b-int(b))*128;d1=(c-int(c))*128
            return d[int(d1)]+d[int(c)]+d[int(b)]+xxx[int(n)]
        a=int(n);b=(n-a)*128;c=(b-int(b))*128
        return d[int(c)]+d[int(b)]+xxx[int(n)]
    a=int(n)
    if a==0:
        return xxx[int((n-a)*128)]
    return d[int((n-a)*128)]+xxx[int(n)]