import re
s="this is python programming laboratory"
match=re.search('portal',s)
print('start index', match.start())
print('end index', match.end())
