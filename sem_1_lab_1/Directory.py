class Directory:
    def __init__(self, dirName, maxElements=0, parent=None):
        self.dirMaxElem = maxElements
        self.parent = parent
        self.dirName = dirName
        self.elementsCount = 0
        self.fileList = []
        return

    def delete(self):
        return

    def list_elements(self):
        return

    def move(self, path):
        return
