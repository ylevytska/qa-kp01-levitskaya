class BufferFile:
    def __init__(self, fileName, maxSize=0, parent=None):
        self.MAX_BUF_FILE_SIZE = maxSize
        self.fileName = fileName
        self.parent = parent
        self.content = []

    def delete(self):
        return

    def move(self, path):
        return

    def push(self, elem):
        return

    def consume(self):
        return
