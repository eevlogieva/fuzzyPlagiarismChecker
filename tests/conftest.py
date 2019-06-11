from pytest import fixture
from checker.argParser.argument_parser import ArgParser
from checker.ssdeepComparator.ssdeep_comparator import Comparator


@fixture(scope="session")
def argParser():
    def parser(args):
        return ArgParser(args)
    return parser


@fixture(scope="session")
def comparator():
    return Comparator()
