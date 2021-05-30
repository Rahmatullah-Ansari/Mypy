import os
from PIL import Image
from fpdf import FPDF
from tkinter.filedialog import askdirectory
# p = FPDF()
# sdir = "C:\\Users\\rahma\\OneDrive\\Pictures\\Screenshots"
# width,height=0.0
# for i in range(1,6):
#     fname=sdir+"img%.d.jpg"%i
#     if os.path.exists(fname):
#         if i==1:
#             p=FPDF(unit='pt',format=[width,height])
#         image=fname
#         p.add_page()
#         p.image(image,0,0,width,height)
#     else:
#         print("File Not Found",fname)
#     print("Processed %d"%i)
# p.output("Converted.pdf","F")
# print("Successful")
lst = []
os.chdir(askdirectory())
# for f in os.listdir():
#     name ,ext = os.path.splitext(f)
#     name = "image_"+str(f)
#     new_name = "{} {}".format(name,ext)
#     lst.append(os.rename(f,new_name))
p=FPDF()
for i in os.listdir():
    if i.endswith(".ini"):
        pass
    else:
        p=FPDF(unit='pt',format=[0,0])
        image=i
        p.add_page()
        p.image(image,0,0,0,0)
        print(f"Processed:- {i}")
# print(os.listdir)
p.output("Out1.pdf","F")
print("successful")
