from matplotlib import pyplot as plt
names=['rasika','pratiksha','shweta']
marks=[80,87,85]
plt.subplot(1,3,1)
plt.bar(names,marks)
plt.subplot(1,3,2)
plt.scatter(names,marks)
plt.suptitle("subplot graph")
plt.show()
