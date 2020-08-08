import os
import docx2pdf
from docx2pdf import convert
folderpath=r"C:\Users\sivacatering\Desktop\folder"
for files in os.listdir(folderpath):
    if ".docx" not in files:
	    continue
    convert(folderpath+"\\"+files,folderpath+"\\"+files.split('.')[0]+".pdf")
