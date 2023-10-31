import os


print("string format",os.getcwd())
print("string format",os.getcwdb())


print("Current directory :", os.getcwd())

print("Current directory :", os.getcwd())
print("files in current directory",os.listdir(os.getcwd()))
print("directory contents are",os.listdir('new_dir'))
os.rmdir('new_dir')
dir_list=os.listdir('new_dir')
if len(dir_list)==0:
    print("directory is empty")
print(os.path.isdir('new_dir'))
         
