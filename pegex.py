import re
s="this is python program portal"
match=re.search('portal',s)
print('start index:',match.start())
print('end index:',match.end())

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)
 
print(result)
