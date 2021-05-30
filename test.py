# # Python program to rename all file 
# # names in your directory 
import os 
from tkinter.filedialog import askdirectory
# os.chdir(askdirectory()) 
# # print(os.getcwd()) 
# COUNT = 1

# # Function to increment count 
# # to make the files sorted. 
# def increment(): 
# 	global COUNT 
# 	COUNT = COUNT + 1


# for f in os.listdir(): 
# 	f_name, f_ext = os.path.splitext(f) 
# 	f_name = "geek" + str(COUNT) 
# 	increment() 

# 	new_name = '{} {}'.format(f_name, f_ext) 
# 	os.rename(f, new_name)
lst = []
os.chdir(askdirectory())
for f in os.listdir():
    name ,ext = os.path.splitext(f)
    name = "i3"+str(f)
    new_name = "{} {}".format(name,ext)
    lst.append(os.rename(f,new_name))
print(os.listdir())

