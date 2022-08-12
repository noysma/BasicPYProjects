import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()
source_dir = os.getcwd()

for file in os.listdir(source_dir):
    if file.endswith("pdf"):
        merger.append(file)

merger.write("Combined.pdf")
merger.close()