from checker.htmlParser.html_parser import MyHTMLParser
from pytest import mark


@mark.htmlParser
def test_parseTags():
    fileContent = open('./resources/simpleFile.html', 'r').read()
    htmlParser = MyHTMLParser()
    htmlParser.feed(fileContent)
    assert htmlParser.getTags() == "<head></head><body></body>"
