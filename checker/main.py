from html.parser import HTMLParser
from ssdeep_comparator import Comparator

TRESHOLD = 21


class MyHTMLParser(HTMLParser):
    def __init__(self, tagsFileName, contentFileName):
        HTMLParser.__init__(self)
        self.tagsFileName = tagsFileName
        self.contentFileName = contentFileName

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        tagsFile = open(self.tagsFileName, 'a')
        tagsFile.write('<' + tag + '>' + '\n')

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        tagsFile = open(self.tagsFileName, 'a')
        tagsFile.write('</' + tag + '>' + '\n')

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        contentFile = open(self.contentFileName, 'a')
        contentFile.write(data + '\n')


def removeWhitespaceFromFileContent(file):
    # TODO regexp
    return file.read().strip().replace(" ", "").replace("\n", "").replace("\t", "")


def validateRequiredTags(requiredTagsFile, tagsFile):
    realStructure = removeWhitespaceFromFileContent(tagsFile)
    requiredStructure = removeWhitespaceFromFileContent(requiredTagsFile)

    if realStructure != requiredStructure:
        print("The file does not conform to the required html structure!")
    else:
        print("The file conforms to the required html structure.")


def console():
    # isRequiredTagsPresent = False
    # try:
        # requiredTagsFile = open("requiredTagsStructure.txt", 'r')
        # isRequiredTagsPresent = True
    # except FileNotFoundError as e:
        # pass

    # tagsFile = open("tags.txt", 'w')
    # contentsFile = open("content.txt", 'w')

    fileNameToCheck = input("Input the filename to be checked: ")
    return fileNameToCheck


if __name__ == '__main__':
    # fileToCheck = open(fileNameToCheck, 'r')
    # content = fileToCheck.read()

    # parser = MyHTMLParser("tags.txt", "content.txt")
    # parser.feed(content)

    # if isRequiredTagsPresent:
        # validateRequiredTags(requiredTagsFile, open("tags.txt", 'r'))
    # fileName2ToCheck = input("Input the second filename to be checked: ")
    # file2ToCheck = open(fileName2ToCheck, 'r')

    # comparator = SSDeepComparator()

    # print("Percentage similarity: " + str(comparator.compare(fileNameToCheck, fileName2ToCheck)))
