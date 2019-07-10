from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.extractedTags = ''
        self.extractedContent = ''

    def handle_starttag(self, tag, attrs):
        self.extractedTags += ('<' + tag + '>')

    def handle_endtag(self, tag):
        self.extractedTags += ('</' + tag + '>')

    def handle_data(self, data):
        self.extractedContent += (data + '\n')

    # a very very basic validity check for html file
    def isValidHtml(self):
        return '<html>' in self.extractedTags and '</html>' in self.extractedTags

    def getTags(self):
        return removeAllWhitespace(self.extractedTags)

    def getContent(self):
        return self.extractedContent

    def generateHTMLReport(self, dirToReportFor, dictToWrite):
        report = open('resultReport.xml', 'w')
        report.write('<dir>' + '\n' + '\t' + '<dirname>' + dirToReportFor + '</dirname>' + '\n')
        for key in dictToWrite:
            report.write('\t' + '<file>' + '\n' + str(2 * '\t') + '<filename>' + key + '</filename>' + '\n')
            for similarFile in dictToWrite[key]:
                report.write(str(2 * '\t') + '<similarFile>' + '\n')
                report.write(str(3 * '\t') + '<filename>' + similarFile[0] + '</filename>' + '\n')
                report.write(str(3 * '\t') + '<percentageSimilarity>' + str(similarFile[1]) + '</percentageSimilarity>' + '\n')
                report.write(str(2 * '\t') + '</similarFile>' + '\n')
            report.write('\t' + '</file>' + '\n')
        report.write('</dir>' + '\n')


def removeAllWhitespace(string):
    return string.lower().strip().replace(" ", "").replace("\n", "").replace("\t", "")
