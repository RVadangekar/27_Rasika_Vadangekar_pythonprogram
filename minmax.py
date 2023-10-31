num=[5,10,24,12,18,29,16,35]
min=num[0]
max=num[0]
        
for i in num:
	if i<min:
		min=i
	if i>max:
		max=i	
		
print("Smallest element is: ",min)
print("largest element is: ",max)
