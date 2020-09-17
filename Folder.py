import os, re, functools

class Folder:
    def __init__(self, path):
        self.path = path
        self.files = self.orderFiles()
        self.size = len(self.files) if self.files else 0

    def orderFiles(self):
        imglist = os.listdir(self.path)
        
        orderedImgs = list()
        for f in imglist:
            if re.findall(r'\d+',f):
                pos = functools.reduce(lambda x,y: x+y ,re.findall(r'\d+',f))
            else:
                pos =0
                
            fileTuple=(pos, f)
            orderedImgs.append(fileTuple)

        for img in range(len(orderedImgs)):
            orderedImgs[img] = self.getPosition(orderedImgs[img])
            
        orderedImgs.sort(key=lambda x: (x[0], x[1]))
        return orderedImgs


    def getPosition(self, imgTuple):
        aux = int(imgTuple[0])        
        return (aux, imgTuple[1])
