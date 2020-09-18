import os, fitz, re
from Folder import Folder

def selectFolder(imgdir):
    folder = Folder(imgdir)
    return os.listdir(imgdir)
    

def run(imgdir, name="output"):
    extensionsList = ['jpg','jpeg','png']
    folder = Folder(imgdir)
    doc = fitz.open()  # PDF with the pictures

    for position, f in folder.files:
        filename=[]
        filename = f.split(".")

        if filename[-1] in extensionsList:       
            img = fitz.open(os.path.join(imgdir, f))  # open pic as document
            rect = img[0].rect  # pic dimension
            pdfbytes = img.convertToPDF()  # make a PDF stream
            img.close()
            imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
            page = doc.newPage(width=rect.width, height=rect.height)  # page dimension
            page.showPDFpage(rect, imgPDF, 0)  # image fills the page

    doc.save(os.path.join(imgdir,"{}.pdf".format(name))) # Save the document
    print(name + ".pdf salvo com sucesso")

if __name__=="__main__":
    imgdir = input("Digite o caminho para a pasta onde estão as imagens: ") # Recieves the path to the folder
    while not os.path.isdir(imgdir):
        imgdir = input("Entada inválida. Por favor, digite novamente o caminho para a pasta onde estão as imagens ou 0 para sair: ")
        if imgdir == "0":
            print('Fechando o programa...')
            exit() 
            
    name = input("Digite o nome da saída: ") # Recieves the name of the output file
    run(imgdir, name)