from unicodedata import name
from docx2pdf import convert
from tkinter.filedialog import askopenfilename
pth=askopenfilename()
lst=pth.split("/")
name=lst[-1].split(".")[0]
outpth=""
for i in range(len(lst)-1):
    outpth += lst[i] + "/"
try:
    convert(pth,outpth+f"/{name}.pdf")
    print("\nSuccessful!")
except Exception as ex:
    print(ex)
