from pytest import mark


@mark.comparator
class ComparatorTests:
    def test_compare(self, comparator):
        assert comparator.compare('./resources/textFile.txt', './resources/textFile.txt') == 100
