import os, fitz, re, argparse
from Folder import Folder

argparser = argparse.ArgumentParser()
argparser.add_argument('-d', '--directory', type=str, metavar='', help='Caminho para a pasta onde estão as imagens')
argparser.add_argument('-o', '--output', type=str, metavar='', help='Nome do arquivo que será salvo')
args = argparser.parse_args()


def selectFolder(imgdir):
    return os.listdir(imgdir)


def pdf_stream_from_image(imgdir, filename):
    img = fitz.open(os.path.join(imgdir, filename))  # open pic as document
    dimension = img[0].rect
    pdf_stream = img.convertToPDF()  # make a PDF stream
    img.close()
    return dimension, pdf_stream


def make_pdf(imgdir, name="output"):
    extensionsList = ["jpg", "jpeg", "png"]
    folder = Folder(imgdir)
    doc = fitz.open()  # PDF with the pictures

    for position, f in folder.files:
        filename = []
        filename = f.split(".")

        if filename[-1] in extensionsList:
            rect, pdfbytes = pdf_stream_from_image(imgdir, f)
            imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
            page = doc.newPage(width=rect.width, height=rect.height)
            page.showPDFpage(rect, imgPDF, 0)  # image fills the page

    doc.save(os.path.join(imgdir, "{}.pdf".format(name)))
    print(name + ".pdf salvo com sucesso na pasta {}.".format(imgdir))
    return True


if __name__ == "__main__":
    if not args.directory and not args.output:
        imgdir = input("Digite o caminho para a pasta onde estão as imagens: ")
        name = input("Digite o nome da saída: ")

    elif args.output and not args.directory:
        imgdir = input("Digite o caminho para a pasta onde estão as imagens: ")
        name = args.output
    else:
        imgdir = args.directory
        name = args.output
    while not os.path.isdir(imgdir):
        imgdir = input(
            "Entada inválida. Por favor, digite novamente o caminho para a pasta onde estão as imagens ou 0 para sair: "
        )
        if imgdir == "0":
            print("Fechando o programa...")
            exit()

    
    make_pdf(imgdir, name)
