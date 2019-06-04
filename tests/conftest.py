from pytest import fixture
from checker.argParser.argument_parser import ArgParser


@fixture(scope="session")
def argParser():
    def parser(args):
        return ArgParser(args)
    return parser
