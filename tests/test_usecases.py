from checker.usecases import compareTwoFiles, isFileStructureTheSame, isDirStructureTheSame

import os


class UsecasesTests:
    def test_compareTwoFiles_sameFiles(self):
        assert compareTwoFiles('./tests/resources/textFile.txt', './tests/resources/textFile.txt') == 100

    def test_compareTwoFiles_differentFiles(self):
        assert compareTwoFiles('./tests/resources/textFile.txt', './tests/resources/simpleFile.html') == 0

    def test_isFileStructureTheSame_expectTrue(self):
        assert isFileStructureTheSame('./tests/resources/simpleStructure.txt', './tests/resources/simpleFile.html') is True

    def test_isFileStructureTheSame_expectFalse(self):
        assert isFileStructureTheSame('./tests/resources/complicatedStructure.txt', './tests/resources/simpleFile.html') is False

    def test_isDirStructureTheSame_expectTrue(self):
        assert isDirStructureTheSame('./tests/resources/simpleStructure.txt', './tests/resources') is True

    def test_isDirStructureTheSame_expectFalse(self):
        diffStructFile = open('./tests/resources/wrongStruct.html', 'w')
        diffStructFile.write('<head>Head</head>')
        assert isDirStructureTheSame('./tests/resources/simpleStructure.txt', './tests/resources') == ['./tests/resources/wrongStruct.html']

    def teardown_method(self):
        try:
            os.remove('./tests/resources/wrongStruct.html')
        except FileNotFoundError:
            pass
