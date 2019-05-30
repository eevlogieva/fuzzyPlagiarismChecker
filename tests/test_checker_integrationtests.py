from checker.main import calculateResult


def test_cmpFile2Dir_expectOneSimilarFile():
    assert calculateResult(['--usecase', 'cmpFile2Dir', '--file1', './tests/resources/copyOfSimpleFile.html', '--dir', './tests/resources']) == ['./tests/resources/simpleFile.html']


def test_cmpFile2Dir_expectNoSimilarFiles():
    assert calculateResult(['--usecase', 'cmpFile2Dir', '--file1', './tests/pytest.ini', '--dir', './tests/resources']) == []
