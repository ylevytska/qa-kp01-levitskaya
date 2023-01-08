class BinaryFile:
    def __init__(self, fileName, content, parent=None):
        self.fileName = fileName
        self.content = content
        self.parent = parent
        self.deleted = False

    def delete(self):
         if self.deleted is False:
            self.deleted = True
            del self
            return {'message': self.fileName +'file deleted'}
         else: 
            return {'error': 'File is already deleted'}

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

    def read(self):
        return self.content
