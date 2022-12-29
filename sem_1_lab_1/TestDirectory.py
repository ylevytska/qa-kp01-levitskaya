from Directory import Directory
from BinaryFile import BinaryFile
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

        # THEN
        assert directory == None

    def test_directory_list_elements(self):
        # GIVEN
        directory = Directory(dirName='dir')

        binaryFile1 = BinaryFile(fileName="file1", content="1")
        binaryFile1.move(directory.dirName)

        binaryFile2 = BinaryFile(fileName="file2", content="2")
        binaryFile2.move(directory.dirName)

        binaryFile3 = BinaryFile(fileName="file3", content="3")
        binaryFile3.move(directory.dirName)

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
        binaryFile1.move(directory.dirName)

        # THEN
        assert pytest.raises(OverflowError)

    def test_directory_is_not_moved_when_target_dir_does_not_exist(self):
        # GIVEN
        directory = Directory(dirName='dir', maxElements=10)
        parentDirectory = None

        # WHEN
        directory.move(parentDirectory)

        # THEN
        assert pytest.raises(Exception)
