import array
def makeBitArray(bitSize, fill = 0):
    intSize = bitSize >> 5
    if (bitSize &31):
        intSize += 1
    if fill == 1:
        fill = 4294967295
    else:
        fill = 0


    bitArray = array.array('I')
    bitArray.extend((fill,) *intSize)
    return(bitArray)

def testBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    return(array_name[record] & mask)

def setBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] |= mask
    return(array_name[record])

def clearBit(array_name, bit_num):
    record= bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset 
    array_name[record] &= mask
    return(array_name[record])

def toggleBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] ^= mask
    return(array_name[record])

bits = 65536

ini = 1

myArray = makeBitArray(bits, ini)

print(bits, len(myArray), (len(myArray) * 32) - bits, bin(myArray[0]))
