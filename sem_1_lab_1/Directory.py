class Directory:
    def __init__(self, dirName, maxElements=0, parent=None):
        self.dirMaxElem = maxElements
        self.parent = parent
        self.dirName = dirName
        self.elementsCount = 0
        self.fileList = []
        return

    def delete(self):
        del self
        return

    def list_elements(self):
        return self.fileList

    def move(self, path):
        if(path == None):
            raise Exception("Target directory doesn't exist")

        if (path.elementsCount >= path.dirMaxElem + 1):
            print('Target directory is full')
            return

        if self.parent != None:
            self.parent.elementsCount -= 1
            self.parent.fileList.pop(self.parent.fileList.index(self))

        self.parent = path
        self.parent.fileList.append(self)
        self.parent.elementsCount += 1
        return
