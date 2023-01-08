class BufferFile:
    def __init__(self, fileName, maxSize=0, parent=None):
        self.maxSize = maxSize
        self.fileName = fileName
        self.parent = parent
        self.content = []
        self.currentPop_Index = -1
        self.deleted = False

    def delete(self):
        if self.deleted is False:
            self.deleted = True
            del self
            return {'message': self.fileName + 'file deleted'}
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

    def push(self, elem):
        if len(self.content) >= self.maxSize:
            raise OverflowError

        self.content.append(elem)
        self.currentPop_Index += 1
        return {'content': self.content}

    def consume(self):
        if self.currentPop_Index >= 0:
            temp = self.content.pop(self.currentPop_Index)
            self.currentPop_Index -= 1
            return temp
        return None
