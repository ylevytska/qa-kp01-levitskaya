from BinaryFile import BinaryFile
from BufferFile import BufferFile
from LogTextFile import LogTextFile
from Directory import Directory
import pytest


class TestDirectory:

    def test_directory_creation(self):
        # GIVEN
        maxElements = 10
        dirName = 'dir'

        # WHEN
        directory = Directory(dirName=dirName, maxElements=maxElements)

        # THEN
        assert directory.dirName == dirName
        assert directory.dirMaxElem == maxElements
        assert directory.elementsCount == 0

    def test_directory_move(self):
        # GIVEN
        directory = Directory(dirName='dir')

        # WHEN
        parentDirectory = Directory('parentDir')
        directory.move(parentDirectory)

        # THEN
        assert directory.parent == parentDirectory

    def test_directory_deletion(self):
        # GIVEN
        directory = Directory(dirName='dir')

        # WHEN
        directory.delete()
        tryToGetDirName = directory.dirName
        print(tryToGetDirName)

        # THEN
        assert pytest.raises(Exception)

    def test_directory_list_elements(self):
        # GIVEN
        directory = Directory(dirName='dir', maxElements=10)

        binaryFile1 = BinaryFile(fileName="file1", content="1")
        binaryFile1.move(directory)

        binaryFile2 = BinaryFile(fileName="file2", content="2")
        binaryFile2.move(directory)

        binaryFile3 = BinaryFile(fileName="file3", content="3")
        binaryFile3.move(directory)

        # WHEN
        dirElements = directory.list_elements()

        # THEN
        assert dirElements[0] == binaryFile1
        assert dirElements[1] == binaryFile2
        assert dirElements[2] == binaryFile3

    def test_element_is_not_added_when_directory_is_full(self):
        # GIVEN
        maxElements = 0
        directory = Directory(dirName='dir', maxElements=maxElements)
        binaryFile1 = BinaryFile(fileName="file1", content="1")

        # WHEN
        binaryFile1.move(directory)

        # THEN
        assert pytest.raises(OverflowError)

    def test_directory_is_not_moved_when_target_dir_does_not_exist(self):
        # GIVEN
        directory = Directory(dirName='dir', maxElements=10)
        parentDirectory = None

        # WHEN
        # THEN
        with pytest.raises(Exception):
            directory.move(parentDirectory)


class TestBinaryFile:

    def test_binary_file_creation(self):
        # GIVEN
        fileName = "file1"
        content = "1"

        # WHEN
        binaryFile = BinaryFile(fileName=fileName, content=content)

        # THEN
        assert binaryFile.fileName == fileName
        assert binaryFile.content == content

    def test_binary_file_deletion(self):
        # GIVEN
        binaryFile = BinaryFile(fileName="file1", content="1")

        # WHEN
        binaryFile.delete()
        tryToGetFileName = binaryFile.fileName
        print(tryToGetFileName)

        # THEN
        assert pytest.raises(Exception)

    def test_binary_file_move(self):
        # GIVEN
        binaryFile = BinaryFile(fileName="file1", content="1")
        parentDir = Directory(dirName="dir", maxElements=10)

        # WHEN
        binaryFile.move(parentDir)

        # THEN
        assert binaryFile.parent == parentDir

    def test_binary_file_read(self):
        # GIVEN
        fileName = "file1"
        expected_content = "1"
        binaryFile = BinaryFile(fileName=fileName, content=expected_content)

        # WHEN
        actual_content = binaryFile.read()

        # THEN
        assert expected_content == actual_content

    def test_binary_file_is_not_moved_when_target_dir_does_not_exist(self):
        # GIVEN
        binaryFile = BinaryFile(fileName="file1", content="1")
        parentDirectory = None

        # WHEN
        # THEN
        with pytest.raises(Exception):
            binaryFile.move(parentDirectory)


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


class TestLogTextFile:
    def test_log_text_file_creation(self):
        # GIVEN
        fileName = "file1"

        # WHEN
        logTextFile = LogTextFile(fileName=fileName)

        # THEN
        assert logTextFile.fileName == fileName

    def test_log_text_file_deletion(self):
        # GIVEN
        fileName = "file1"
        logTextFile = LogTextFile(fileName=fileName)

        # WHEN
        logTextFile.delete()
        tryToGetDirName = logTextFile.fileName
        print(tryToGetDirName)

        # THEN
        assert pytest.raises(Exception)

    def test_log_text_file_move(self):
        # GIVEN
        fileName = "file1"
        logTextFile = LogTextFile(fileName=fileName)
        parentDir = Directory(dirName="dir", maxElements=10)

        # WHEN
        logTextFile.move(parentDir)

        # THEN
        assert logTextFile.parent == parentDir

    def test_log_text_file_read(self):
        # GIVEN
        fileName = "file1"
        newLine = "new line"
        expected_content = "new line new line new line "
        logTextFile = LogTextFile(fileName=fileName)

        # WHEN
        logTextFile.append_line(newLine)
        logTextFile.append_line(newLine)
        logTextFile.append_line(newLine)
        actual_content = logTextFile.read()

        # THEN
        assert expected_content == actual_content

    def test_log_text_file_is_not_moved_when_target_dir_does_not_exist(self):
        # GIVEN
        fileName = "file1"
        logTextFile = LogTextFile(fileName=fileName)
        parentDirectory = None

        # WHEN
        # THEN
        with pytest.raises(Exception):
            logTextFile.move(parentDirectory)
