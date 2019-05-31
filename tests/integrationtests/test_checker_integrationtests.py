from checker.main import calculateResult
from pytest import mark


@mark.integration
class IntegrationTests:
    def test_cmpFile2Dir_expectOneSimilarFile(self):
        assert calculateResult(['--usecase', 'cmpFile2Dir', '--file1', './resources/copyOfSimpleFile.html', '--dir', './resources']) == ['./resources/simpleFile.html']

    def test_cmpFile2Dir_expectNoSimilarFiles(self):
        assert calculateResult(['--usecase', 'cmpFile2Dir', '--file1', './pytest.ini', '--dir', './resources']) == []

    def test_cmpTwoFiles_expect100Similarity(self):
        assert calculateResult(['--usecase', 'cmpTwoFiles', '--file1', './resources/copyOfSimpleFile.html', '--file2', './resources/simpleFile.html']) == 100

    def test_cmpTwoFiles_expect0Similarity(self):
        assert calculateResult(['--usecase', 'cmpTwoFiles', '--file1', './resources/copyOfSimpleFile.html', '--file2', './resources/textFile.txt']) == 0

    def test_checkStructure_expectTrue(self):
        assert calculateResult(['--usecase', 'checkStructure', '--file1', './resources/simpleFile.html', '--structureFile', './resources/simpleStructure.txt'])

    def test_checkStructure_expectFalse(self):
        assert calculateResult(['--usecase', 'checkStructure', '--file1', './resources/simpleFile.html', '--structureFile', './resources/complicatedStructure.txt']) == (False, 0)

    def test_checkStructureDir_expectTrue(self):
        assert calculateResult(['--usecase', 'checkStructureDir', '--dir', './resources', '--structureFile', './resources/simpleStructure.txt'])

    def test_checkStructureDir_expectTwoFIlesToNotConformTheStructure(self):
        assert calculateResult(['--usecase', 'checkStructureDir', '--dir', './resources', '--structureFile', './resources/complicatedStructure.txt']) == ['./resources/simpleFile.html', './resources/copyOfSimpleFile.html']

    def test_cmpFilesInDir_expectTwoFIlesSame(self):
        assert calculateResult(['--usecase', 'cmpFilesInDir', '--dir', './resources']) == {'./resources/simpleFile.html': [('./resources/copyOfSimpleFile.html', 100)]}
