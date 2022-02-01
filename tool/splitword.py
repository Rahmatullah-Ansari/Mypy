import aspose.words as aw
from tkinter.filedialog import *
path=askopenfilename()
print(path)
doc=aw.Document(path)
count=doc.page_count
name=path.split("/")[-1].split(".")[0]
for page in range(0,count):
    extractPage=doc.extract_pages(page,1)
    extractPage.save(f"{name}[{page+1}].docx")
