from checker.usecases import compare2Files, isFileStructureTheSame


def test_compare2Files_sameFiles():
    assert compare2Files('./tests/resources/textFile.txt', './tests/resources/textFile.txt') == 100


def test_compare2Files_differentFiles():
    assert compare2Files('./tests/resources/textFile.txt', './tests/resources/simpleFile.html') == 0


def test_isFileStructureTheSame_expectTrue():
    assert isFileStructureTheSame('./tests/resources/simpleStructure.txt', './tests/resources/simpleFile.html')


def test_isFileStructureTheSame_expectFalse():
    assert isFileStructureTheSame('./tests/resources/complicatedStructure.txt', './tests/resources/simpleFile.html') == False
