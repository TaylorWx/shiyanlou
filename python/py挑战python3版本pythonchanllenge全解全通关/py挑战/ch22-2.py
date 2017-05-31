#coding=gbk
import zlib,bz2
data=open(r'package.pack','rb').read()
result=""
while True:
    if data.startswith(b'x\x9c'):
        data = zlib.decompress(data)
        result += ' '
    elif data.startswith(b'BZh'):
        data = bz2.decompress(data)
        result += '#'
    elif data.endswith(b'\x9cx'):
        data = data[::-1]
        result += '\n'
    else:
        break
print(result)
