l=["first",1,2.0]
for i in l:
    print(i)

print("\nin continue")
for l in "dypcet":
    if l=='e' or l=='p':
        continue
    print("letter: ",l)
    
print("\nin break")
for l in "dypcet":
    if l=='e' or l=='p':
        break
    print("letter: ",l)

for l in "dyp123":
    pass
print("letter is: ",l)
    
