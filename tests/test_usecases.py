from checker.usecases import compareTwoFiles, isFileStructureTheSame, isDirStructureTheSame

from pytest import mark

import os


@mark.usecases
class UsecasesTests:
    def test_compareTwoFiles_sameFiles(self):
        assert compareTwoFiles('./resources/textFile.txt', './resources/textFile.txt') == 100

    def test_compareTwoFiles_differentFiles(self):
        assert compareTwoFiles('./resources/textFile.txt', './resources/simpleFile.html') == 0

    def test_isFileStructureTheSame_expectTrue(self):
        assert isFileStructureTheSame('./resources/simpleStructure.txt', './resources/simpleFile.html') is True

    def test_isFileStructureTheSame_expectFalse(self):
        assert isFileStructureTheSame('./resources/complicatedStructure.txt', './resources/simpleFile.html') == (False, 0)

    def test_isDirStructureTheSame_expectTrue(self):
        assert isDirStructureTheSame('./resources/simpleStructure.txt', './resources') is True

    def test_isDirStructureTheSame_expectFalse(self):
        diffStructFile = open('./resources/wrongStruct.html', 'w')
        diffStructFile.write('<head>Head</head>')
        assert isDirStructureTheSame('./resources/simpleStructure.txt', './resources') == ['./resources/wrongStruct.html']

    def teardown_method(self):
        try:
            os.remove('./resources/wrongStruct.html')
        except FileNotFoundError:
            pass
