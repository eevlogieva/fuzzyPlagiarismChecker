from pytest import mark


@mark.argParser
class ArgParserTests:
    def test_getUsecase(self, argParser):
        args = ['--usecase', 'cmpFile2Dir', '--file1', './resources/file1.html', '--dir', './resources']
        assert argParser(args).getUsecase() == 'cmpFile2Dir'

    def test_getFile1(self, argParser):
        args = ['--usecase', 'cmpFile2Dir', '--file1', './resources/file1.html', '--dir', './resources']
        assert argParser(args).getFile1() == './resources/file1.html'

    def test_getFile2(self, argParser):
        args = ['--usecase', 'cmpTwoFiles', '--file1', './resources/file1.html', '--file2', './resources/file2.html']
        assert argParser(args).getFile2() == './resources/file2.html'

    def test_getStructureFile(self, argParser):
        args = ['--usecase', 'checkStructure', '--file1', './resources/copyOfSimpleFile.html', '--structureFile', './resources/struct.txt']
        assert argParser(args).getStructureFile() == './resources/struct.txt'

    def test_getDir(self, argParser):
        args = ['--usecase', 'cmpFile2Dir', '--file1', './resources/file1.html', '--dir', './resources']
        assert argParser(args).getDir() == './resources'

    def test_getDir_notPassed(self, argParser):
        args = ['--usecase', 'cmpFile2Dir', '--file1', './resources/file1.html']
        assert argParser(args).getDir() is None

    def test_getUsecase_notPassed(self, argParser):
        args = ['--file1', './resources/file1.html', '--dir', './resources']
        assert argParser(args).getUsecase() is None

    def test_getFile1_notPassed(self, argParser):
        args = ['--usecase', 'cmpFile2Dir', '--dir', './resources']
        assert argParser(args).getFile1() is None

    def test_getFile2_notPassed(self, argParser):
        args = ['--usecase', 'cmpTwoFiles', '--file1', './resources/file1.html']
        assert argParser(args).getFile2() is None

    def test_getStructureFile_notPassed(self, argParser):
        args = ['--usecase', 'checkStructure', '--file1', './resources/copyOfSimpleFile.html']
        assert argParser(args).getStructureFile() is None
