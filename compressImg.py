import PIL
from PIL import Image
from tkinter.filedialog import *
path=askopenfilename()
img=PIL.Image.open(path)
height,width=img.size
img=img.resize((height,width),PIL.Image.ANTIALIAS)
pth=asksaveasfilename(defaultextension="jpg")
img.save(pth)
