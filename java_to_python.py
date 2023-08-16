import re

def removeDuplicate(s):
    index = 0
    c = list(s)
    for i in range(len(s)):
        for j in range(i):
            if c[i] == c[j]:
                break
        if i == j:
            c[index] = c[i]
            index += 1
    s = ''.join(c[:index])
    return s

def removeWhiteSpace(ch, key):
    c = list(key)
    for i in range(len(c)):
        for j in range(len(ch)):
            if c[i] == ch[j]:
                c[i] = ' '
    key = ''.join(c)
    key = re.sub(' ', '', key)
    return key

def makePair(pt):
    s = ""
    c = 'a'
    for i in range(len(pt)):
        if pt[i] == ' ':
            continue
        else:
            c = pt[i]
            s += pt[i]
        if i < len(pt) - 1:
            if pt[i] == pt[i + 1]:
                s += "x"
    if len(s) % 2 != 0:
        s += "x"
    print(s, end="")
