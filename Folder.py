import os, re, functools


class Folder:
    def __init__(self, path):
        self.path = path
        self.files = self.__orderFiles()
        self.size = len(self.files) if self.files else 0

    def __treatFilenames(self, filename):
        clean_name = re.sub("[0-9]", "", filename)
        clean_name = clean_name.lower()
        clean_name = clean_name.replace("(", "").replace(")", "")
        clean_name = clean_name.replace(" ", "")
        return clean_name

    def __orderFiles(self):
        imglist = os.listdir(self.path)

        orderedImgs = list()
        for f in imglist:
            if re.findall(r"\d+", f):
                pos = int(functools.reduce(lambda x, y: x + y, re.findall(r"\d+", f)))
            else:
                pos = 0

            fileTuple = (pos, f)
            orderedImgs.append(fileTuple)

        orderedImgs.sort(key=lambda x: (self.__treatFilenames(x[1]), x[0]))
        return orderedImgs
