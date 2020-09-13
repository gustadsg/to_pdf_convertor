import os, fitz

print(os.getcwd())

imgdir= input("digite o caminho para a pasta onde estão as imagens: ")
# imgdir = os.path.join(os.getcwd(),"images")  # where the pics are
name=input("digite o nome da saída: ")


imglist = os.listdir(imgdir)  # list of them
imgcount = len(imglist)  # pic count

doc = fitz.open()  # PDF with the pictures

for i, f in enumerate(imglist):
    img = fitz.open(os.path.join(imgdir, f))  # open pic as document
    rect = img[0].rect  # pic dimension
    pdfbytes = img.convertToPDF()  # make a PDF stream
    img.close()  # no longer needed
    imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
    page = doc.newPage(width = rect.width,  # new page with ...
                       height = rect.height)  # pic dimension
    page.showPDFpage(rect, imgPDF, 0)  # image fills the page
    

doc.save("{}.pdf".format(name))