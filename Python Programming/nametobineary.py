def string2bits(s=""):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bit2strings(b=None):
    return''.join([chr(int(x,2)) for x in b])

s="Prince"
b= string2bits(s)

convertedback=bit2strings(b)
print(convertedback)
