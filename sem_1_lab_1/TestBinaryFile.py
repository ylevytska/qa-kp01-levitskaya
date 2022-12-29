from BinaryFile import BinaryFile
from Directory import Directory
import pytest


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
