from inspect import trace
from PyPDF2 import PdfFileWriter,PdfFileReader
import os
from tkinter.filedialog import *
try:
    path=askopenfilename()
    list=path.split("/")
    outpath=""
    for i in range(len(list)-1):
        outpath += list[i]+"/"
    name=list[-1].split(".")[0]
    p=os.path.join(outpath,name)
    os.mkdir(p)
    outpath = outpath+name
    input=PdfFileReader(open(path,"rb"))
    for page in range(input.numPages):
        output=PdfFileWriter()
        output.addPage(input.getPage(page))
        with open(outpath+f"/{name}[{page+1}].pdf","wb") as outPut:
            output.write(outPut)
    print("Successful!")
except Exception as ex:
    pass