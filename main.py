import os, fitz


imgdir = input("Digite o caminho para a pasta onde estão as imagens: ") # Recieves the path to the folder
name = input("Digite o nome da saída: ") # Recieves the name of the output file

imglist = os.listdir(imgdir)  # list of them
imgcount = len(imglist)  # pic count

doc = fitz.open()  # PDF with the pictures

for i, f in enumerate(imglist):
    img = fitz.open(os.path.join(imgdir, f))  # open pic as document
    rect = img[0].rect  # pic dimension
    pdfbytes = img.convertToPDF()  # make a PDF stream
    img.close()
    imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
    page = doc.newPage(
        width=rect.width, height=rect.height
    )  # page dimension
    page.showPDFpage(rect, imgPDF, 0)  # image fills the page

doc.save("{}.pdf".format(name)) # Save the document
