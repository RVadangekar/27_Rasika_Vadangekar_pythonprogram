import re
s="this is python program portal"
match=re.search('portal',s)
print('start index:',match.start())
print('end index:',match.end())

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)
 
print(result)

string = "Hello World!"
pattern = r"World!$"
 
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")


string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"
 
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")


p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
 
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
