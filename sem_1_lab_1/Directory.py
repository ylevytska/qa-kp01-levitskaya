class Directory:
    def __init__(self, dirName, maxElements=0, parent=None):
        self.DIR_MAX_ELEMS = maxElements
        self.parent = parent
        self.name = dirName
        self.elementsCount = 0
        self.fileList = []
        return

    def delete_dir(self):
        return

    def list_elements(self):
        return

    def move_element(self, path):
        return
