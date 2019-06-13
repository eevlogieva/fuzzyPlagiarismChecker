from checker.ssdeepComparator.ssdeep_comparator import Comparator
from checker.htmlParser.html_parser import MyHTMLParser, removeAllWhitespace

import os


def compareTwoFiles(file1, file2):
    comparator = Comparator()
    return comparator.compare(file1, file2)


def isFileStructureTheSame(structureFile, file1):
    if not str(file1).endswith('.html'):
        raise TypeError('The file to check is not with format html.')
    htmlParser = MyHTMLParser()
    htmlParser.feed(open(file1, 'r').read())
    realStructure = htmlParser.getTags()
    requiredStructure = removeAllWhitespace(open(structureFile, 'r').read())

    if not realStructure == requiredStructure:
        comparator = Comparator()
        return (False, comparator.compareStrings(realStructure, requiredStructure))
    return (True, 100)


# returns an array of the files that do not conform to the given structure
def isDirStructureTheSame(structureFile, dirToCheck):
    filesWrongStructure = []
    for dirName, subdirList, fileList in os.walk(dirToCheck):
        for fname in fileList:
            if str(fname).endswith('.html') and (isFileStructureTheSame(structureFile, os.path.join(dirName, fname)) == (False, 0)):
                filesWrongStructure.append(os.path.join(dirName, fname))

    if len(filesWrongStructure) == 0:
        return (True, 100)
    else:
        return filesWrongStructure


def compareFile2Dir(file1, dirToCheck):
    comparator = Comparator()
    return comparator.compare(file1, dirToCheck)


def compareFilesInDir(dirToCheck):
    comparator = Comparator()
    return comparator.extractSimilarFiles(dirToCheck)
