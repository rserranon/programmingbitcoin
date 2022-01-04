n = 255
myOtherBytes = bytes([2,3])
myBytes = b'0x4' + n.to_bytes(2,'big')
print(myOtherBytes)
print(myBytes)
