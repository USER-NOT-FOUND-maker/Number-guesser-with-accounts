def IsSequencableStructure(i):
    if isinstance(i,list):
        return True
    if isinstance(i,tuple):
        return True
    if isinstance(i,set):
        return True
    return False

def FixBinSize(x,y):
    if is_bin(x) and is_bin(y):
        if len(x) != len(y):
            if len(x) > len(y):
                y = y.zfill(len(x))
                return x,y
            else:
                x = x.zfill(len(y))
                return x,y
        return x,y

def is_bin(n):
    for i in str(n):
        if str(i) != "1" and i != "0":
            return False
    return True

def fixbin(n):
    if is_bin(n):
        if n[0] != "1":
            for i in range(len(n)):
                if n[i] == "1":
                    start = i
                    n = n[start::]
                    break
        return n
    raise ValueError("not a binary number")

def int2bin(n):
    if n == 0:
        return "0"
    elif n  == 1:
        return "1"
    elif n == 2:
        return "10"
    else:
        BinaryString = ""
        BinaryDigits = []
        for i in range(n):
            if 2**i <= n:
                BinaryDigits.append(2**i)
                continue
            BinaryDigits.append(2**i)
            break
        BinaryDigits = BinaryDigits[::-1]
        
        CurrentNumber = 0

        
        for i in BinaryDigits:
            if (CurrentNumber + i) <= n:
                CurrentNumber += i
                BinaryString += "1"
            else:
                BinaryString += "0"
    return BinaryString[1::]

def bin2int(n):
    if not is_bin(n):
        raise ValueError("not a binary number")
    n = fixbin(n)
    nums = [2**i for i in range(len(n))][::-1]
    total = 0
    for i in range(len(n)):
        if n[i] == "1":
            total += nums[i]
    return total

def addbin(x,y):
    if not (is_bin(x) and is_bin(y)):
        raise ValueError("not a binary number")
    x = bin2int(x)
    y = bin2int(y)
    z = x+y
    z = int2bin(z)
    return z

def subbin(x,y):
    if not (is_bin(x) and is_bin(y)):
        raise ValueError("not a binary number")
    x = bin2int(x)
    y = bin2int(y)
    z = x-y
    z = int2bin(z)
    return z

def mulbin(x,y):
    if not (is_bin(x) and is_bin(y)):
        raise ValueError("not a binary number")
    x = bin2int(x)
    y = bin2int(y)
    z = x*y
    z = int2bin(z)
    return z

def divbin(x,y):
    if not (is_bin(x) and is_bin(y)):
        raise ValueError("not a binary number")
    x = bin2int(x)
    y = bin2int(y)
    z = x//y
    if x//y != x/y:
        print("WARNING! number has been rounded down!")
    z = int2bin(z)
    return z

def XorBin(x,y):
    new = []
    if not (is_bin(x) and is_bin(y)):
        raise ValueError("not a binary number")
    x,y = fixbin(x),fixbin(y)
    x,y = FixBinSize(x,y)
    for i in range(len(x)):
        new.append(str(int(x[i] != y[i])))
    return ''.join(new)

def OrBin(x,y):
    new = []
    if not (is_bin(x) and is_bin(y)):
        raise ValueError("not a binary number")
    x,y = fixbin(x),fixbin(y)
    x,y = FixBinSize(x,y)
    for i in range(len(x)):
        new.append(str(int(x[i]) | int(y[i])))
    return ''.join(new)

def AndBin(x,y):
    new = []
    if not (is_bin(x) and is_bin(y)):
        raise ValueError("not a binary number")
    x,y = fixbin(x),fixbin(y)
    x,y = FixBinSize(x,y)
    for i in range(len(x)):
        new.append(str(int(x[i]) & int(y[i])))
    return ''.join(new)

def PowerBin(x,y):
    if not (is_bin(x) and is_bin(y)):
        raise ValueError("not a binary number")
    x = bin2int(x)
    y = bin2int(y)
    z = x**y
    z = int2bin(z)
    return z

def chr2bin(s):
    return int2bin(ord(s))

def bin2chr(n):
    if not is_bin(n):
        raise ValueError("not a binary number")
    n = fixbin(n)
    return chr(bin2int(n))

def str2bin(s):
    result = [chr2bin(s[i]) for i in range(len(s))]
    return result

def bin2str(ls):
    if not IsSequencableStructure(ls):
        raise ValueError("entered value must be a sequencable structure: List, tuple or set")
    else:
        result = []
        for i in range(len(ls)):
            result.append(bin2chr(ls[i]))
    return ''.join(result)