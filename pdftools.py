from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import sys

command = sys.argv[1]

def extract_pages(pages,pdf_file_path):
    file_base_name = pdf_file_path.replace('.pdf', '')

    pdf = PdfFileReader(pdf_file_path)

    #pages = [0, 2, 4] # page 1, 3, 5
    pdfWriter = PdfFileWriter()

    for page_num in pages:
        pdfWriter.addPage(pdf.getPage(int(page_num)-1))

    with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
        pdfWriter.write(f)
        f.close()

if(command == "extract"):
    pages = sys.argv[3:]
    pdf_file_path = sys.argv[2]
    extract_pages(pages,pdf_file_path)

if(command =="append"):
    appender = PdfFileMerger()
    appender.append(sys.argv[2])
    appender.append(sys.argv[3])
    appender.write("appended.pdf")
