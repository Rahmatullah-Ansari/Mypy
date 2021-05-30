import img2pdf
from tkinter.filedialog import askdirectory
import os
with open("output1.pdf","wb") as f:
	f.write(img2pdf.convert((int(i) for i in os.listdir(askdirectory()))))