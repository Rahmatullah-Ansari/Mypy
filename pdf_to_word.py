__author__="Rahmatullah Ansari"
__credits__="Rahmatullah Ansari"
__email__="rahmatullahansari38@gmail.com"

import win32com.client
import os

word=win32com.client.Dispatch("word.Application")
word.visible=0

doc_pdf="E:\\others\\Age_Declaration_Form.pdf"
input_file=os.path.abspath(doc_pdf)

wb=word.Documents.open(input_file)
output_file=os.path.abspath(doc_pdf[0:-4]+"docx".format())
wb.SaveAs2(output_file,FileFormat=16)
print("successfully!")
wb.Close()
word.Quit()