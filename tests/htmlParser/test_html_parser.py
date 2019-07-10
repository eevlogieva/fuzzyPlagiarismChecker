from checker.htmlParser.html_parser import MyHTMLParser
from pytest import mark


@mark.htmlParser
def test_parseTags():
    fileContent = open('./resources/simpleFile.html', 'r').read()
    htmlParser = MyHTMLParser()
    htmlParser.feed(fileContent)
    assert htmlParser.getTags() == '<html><head></head><body></body></html>'
    assert htmlParser.getContent().strip() == 'This is the head.\n\n\n\n\nThis is the body.'
