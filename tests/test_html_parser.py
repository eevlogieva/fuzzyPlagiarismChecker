from checker.html_parser import MyHTMLParser


def test_parseTags():
    fileContent = open('./tests/resources/simpleFile.html', 'r').read()
    htmlParser = MyHTMLParser()
    htmlParser.feed(fileContent)
    assert htmlParser.getTags() == "<head></head><body></body>"
