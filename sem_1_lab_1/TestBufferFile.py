from BufferFile import BufferFile
from Directory import Directory
import pytest


class TestBufferFile:

    def test_buffer_file_creation(self):
        # GIVEN
        fileName = "file1"
        maxSize = 10

        # WHEN
        bufferFile = BufferFile(fileName=fileName, maxSize=maxSize)

        # THEN
        assert bufferFile.fileName == fileName
        assert bufferFile.maxSize == maxSize

    def test_buffer_file_deletion(self):
        # GIVEN
        bufferFile = BufferFile(fileName="file1", maxSize=10)

        # WHEN
        bufferFile.delete()
        tryToGetFileName = bufferFile.fileName
        print(tryToGetFileName)

        # THEN
        assert pytest.raises(Exception)

    def test_buffer_file_move(self):
        # GIVEN
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        parentDir = Directory(dirName="dir", maxElements=10)

        # WHEN
        bufferFile.move(parentDir)

        # THEN
        assert bufferFile.parent == parentDir

    def test_buffer_file_push(self):
        # GIVEN
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        pushedElement = 1

        # WHEN
        bufferFile.push(pushedElement)

        # THEN
        assert bufferFile.content[0] == pushedElement

    def test_element_is_not_pushed_when_buffer_file_is_full(self):
        # GIVEN
        bufferFile = BufferFile(fileName="file1", maxSize=0)
        pushedElement = 1

        # WHEN
        # THEN
        with pytest.raises(OverflowError):
            bufferFile.push(pushedElement)

    def test_buffer_file_consume(self):
        # GIVEN
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        pushedElement = 1

        # WHEN
        bufferFile.push(pushedElement)

        # THEN
        assert bufferFile.consume() == pushedElement

    def test_buffer_file_is_not_moved_when_target_dir_does_not_exist(self):
        # GIVEN
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        parentDirectory = None

        # WHEN
        # THEN
        with pytest.raises(Exception):
            bufferFile.move(parentDirectory)
