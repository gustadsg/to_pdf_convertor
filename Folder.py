import os, re

class Folder:
    def __init__(self, path):
        self.path = path
        self.files = self.orderFiles()
        self.size = len(self.files) if self.files else 0

    def orderFiles(self):
        imglist = os.listdir(self.path)
        
        orderedImgs = list()
        for f in imglist:
            pos = re.findall(r'\d+', f)
            fileTuple=(pos, f)
            orderedImgs.append(fileTuple)

        for img in range(len(orderedImgs)):
            orderedImgs[img] = self.getPosition(orderedImgs[img])
            
        orderedImgs.sort(key=lambda x: x[0])
        return orderedImgs


    def getPosition(self, imgTuple):
        aux = imgTuple[0]
        aux = list(map(int, aux))
        if aux:
            aux=aux[0]
        else:
            aux=0
        return (aux, imgTuple[1])
