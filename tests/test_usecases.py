from checker.usecases import compareTwoFiles, isFileStructureTheSame, isDirStructureTheSame, compareFilesInDir

from pytest import mark, raises

import os


@mark.usecases
class UsecasesTests:
    def test_compareTwoFiles_sameFiles(self):
        assert compareTwoFiles('./resources/textFile.txt', './resources/textFile.txt') == 100

    def test_compareTwoFiles_differentFiles(self):
        assert compareTwoFiles('./resources/textFile.txt', './resources/simpleFile.html') == 0

    def test_compareTwoFiles_expectPermissionError(self):
        restrictedFile = open('./resources/tempFile.html', 'w')
        restrictedFile.close()
        os.chmod('./resources/tempFile.html', 100)
        with raises(PermissionError):
            assert compareTwoFiles('./resources/tempFile.html', './resources/simpleFile.html')

    def test_compareTwoFiles_nonExistent_expectIOError(self):
        with raises(IOError):
            assert compareTwoFiles('./resources/nonExistant.html', './resources/simpleFile.html')

    def test_isFileStructureTheSame_expectTrue(self):
        assert isFileStructureTheSame('./resources/simpleStructure.txt', './resources/simpleFile.html') == (True, 100)

    def test_isFileStructureTheSame_expectFalse(self):
        assert isFileStructureTheSame('./resources/complicatedStructure.txt', './resources/simpleFile.html') == (False, 0)

    def test_isFileStructureTheSame_noHtmlExtension_expectException(self):
        with raises(TypeError):
            assert isFileStructureTheSame('./resources/simpleStructure.txt', './resources/simpleStructure.txt')

    def test_isFileStructureTheSame_noValidHtml_expectException(self):
        with raises(TypeError):
            assert isFileStructureTheSame('./resources/simpleStructure.txt', './resources/toTestNoValidHtml/noValidHtml.html')

    def test_isDirStructureTheSame_expectTrue(self):
        assert isDirStructureTheSame('./resources/simpleStructure.txt', './resources/toTestDirStructureTheSame') == (True, 100)

    def test_isDirStructureTheSame_expectFalse(self):
        result = isDirStructureTheSame('./resources/complicatedStructure.txt', './resources/toTestDirStructureTheSame')
        assert 'simpleFile.html' in result

    def test_compareFilesInDir_expectTwoFIlesSame(self):
        result = compareFilesInDir('./resources')
        expectedFile = '/simpleFile.html'
        expectedFile2 = '/copyOfSimpleFile.html'
        assert expectedFile in result or expectedFile2 in result

    def test_compareFilesInDir_expectMDFilesNotConsidered(self):
        result = compareFilesInDir('./resources')
        assert 'test1.md' not in result and 'test2.md' not in result

    def test_compareFilesInDir_expectNoSameFiles(self):
        result = compareFilesInDir('./resources/toTestRestrictedFiles')
        assert result == {}

    def test_compareFilesInDir_expectNoSameFilesInDirWithHiddenFiles(self):
        result = compareFilesInDir('./resources/toTestHiddenFiles')
        assert result == {}

    def teardown_method(self):
        try:
            os.remove('./resources/tempFile.html')
        except FileNotFoundError:
            pass
