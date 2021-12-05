from os import path
import winapps as apps
import os
path=""
for x in apps.search_installed('chrome'):
    lst=x.uninstall_string.split("'\'")[0].split("\\")
    print(lst)
for i in range(len(lst)-3):
        path +="".join(lst[i])
        path+="\\"
os.startfile(path+"chrome.exe")
print(path)