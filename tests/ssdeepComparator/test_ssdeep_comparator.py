from pytest import mark
from checker.ssdeepComparator.ssdeep_comparator import Comparator


@mark.comparator
class ComparatorTests():
    def test_compare(self, comparator):
        assert comparator.compare('./resources/textFile.txt', './resources/textFile.txt') == 100

    def test_compareStrings_expectSame(self, comparator):
        assert comparator.compareStrings('This is a string', 'This is a string') == 100

    def test_compareStrings_expectDiff(self, comparator):
        assert comparator.compareStrings('This is a string', 'This is a different string') == 0

    def test_compareStrings_mocked(self, mocker):
        ssdeepMock = mocker.patch('ssdeep_mock.SsdeepMock')
        attrs = {'hash.return_value': 3, 'compare.return_value': 1}
        ssdeepMock.configure_mock(**attrs)
        comparator = Comparator(ssdeepMock)
        result = comparator.compareStrings('first string', 'second string')
        ssdeepMock.assert_has_calls([mocker.call.hash('first string'), mocker.call.hash('second string')])
        ssdeepMock.compare.assert_called_with(3, 3)
        assert result is 1

    def test_compare_mocked(self, mocker):
        ssdeepMock = mocker.patch('ssdeep_mock.SsdeepMock')
        attrs = {'hash_from_file.return_value': 3, 'compare.return_value': 1}
        ssdeepMock.configure_mock(**attrs)
        comparator = Comparator(ssdeepMock)
        result = comparator.compare('./resources/textFile.txt', './resources/textFile.txt')
        print(result)
        ssdeepMock.assert_has_calls([mocker.call.hash_from_file('./resources/textFile.txt'), mocker.call.hash_from_file('./resources/textFile.txt')])
        ssdeepMock.compare.assert_called_with(3, 3)
        assert result is 1
