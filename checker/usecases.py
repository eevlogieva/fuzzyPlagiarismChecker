from checker.ssdeep_comparator import Comparator
from checker.html_parser import MyHTMLParser, removeAllWhitespace


def compare2Files(file1, file2):
    comparator = Comparator()
    return comparator.compare(file1, file2)


def isFileStructureTheSame(structureFile, file1):
    htmlParser = MyHTMLParser()
    htmlParser.feed(open(file1, 'r').read())
    realStructure = htmlParser.getTags()
    requiredStructure = removeAllWhitespace(open(structureFile, 'r').read())

    if realStructure != requiredStructure:
        return False
    else:
        return True
