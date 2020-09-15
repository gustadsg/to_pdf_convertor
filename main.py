import os, fitz, re


def getPosition(imgTuple):
    aux = imgTuple[0]
    aux = list(map(int, aux))
    if aux:
        aux=aux[0]
    else:
        aux=0
    return (aux, imgTuple[1])


extensionsList = ['jpg','jpeg','png']

imgdir = input("Digite o caminho para a pasta onde estão as imagens: ") # Recieves the path to the folder
name = input("Digite o nome da saída: ") # Recieves the name of the output file

imglist = os.listdir(imgdir)  # list of the images
orderedImgs = list()

# ordering the images by name
for f in imglist:
    pos = re.findall(r'\d+', f)
    fileTuple=(pos, f)
    orderedImgs.append(fileTuple)

for img in range(len(orderedImgs)):
    orderedImgs[img] = getPosition(orderedImgs[img])

orderedImgs.sort(key=lambda x: x[0])

imgcount = len(imglist)  # pic count

doc = fitz.open()  # PDF with the pictures

for position, f in orderedImgs:
    filename, extension = f.split(".")

    if extension in extensionsList:       
        img = fitz.open(os.path.join(imgdir, f))  # open pic as document
        rect = img[0].rect  # pic dimension
        pdfbytes = img.convertToPDF()  # make a PDF stream
        img.close()
        imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
        page = doc.newPage(width=rect.width, height=rect.height)  # page dimension
        page.showPDFpage(rect, imgPDF, 0)  # image fills the page

doc.save(os.path.join(imgdir,"{}.pdf".format(name))) # Save the document
print(name + ".pdf salvo com sucesso")