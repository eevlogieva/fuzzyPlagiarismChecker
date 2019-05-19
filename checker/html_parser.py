from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.extractedTags = ""
        self.extractedContent = ""

    def handle_starttag(self, tag, attrs):
        self.extractedTags += ('<' + tag + '>')

    def handle_endtag(self, tag):
        self.extractedTags += ('</' + tag + '>')

    def handle_data(self, data):
        self.extractedContent += (data + '\n')

    def getTags(self):
        return removeAllWhitespace(self.extractedTags)

    def getContent(self):
        return self.extractedContent


def removeAllWhitespace(string):
    # TODO regexp
    return string.strip().replace(" ", "").replace("\n", "").replace("\t", "")
