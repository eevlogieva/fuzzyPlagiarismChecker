from checker.ssdeep_comparator import Comparator
from checker.html_parser import MyHTMLParser, removeAllWhitespace

import os


def compareTwoFiles(file1, file2):
    comparator = Comparator()
    return comparator.compare(file1, file2)


def isFileStructureTheSame(structureFile, file1):
    htmlParser = MyHTMLParser()
    htmlParser.feed(open(file1, 'r').read())
    realStructure = htmlParser.getTags()
    requiredStructure = removeAllWhitespace(open(structureFile, 'r').read())

    return realStructure == requiredStructure


def isDirStructureTheSame(structureFile, dirToCheck):
    filesWrongStructure = []
    for dirName, subdirList, fileList in os.walk(dirToCheck):
        for fname in fileList:
            if str(fname).endswith('.html') and isFileStructureTheSame(structureFile, dirName + '/' + fname) is False:
                filesWrongStructure.append(dirName + '/' + fname)

    print(filesWrongStructure)
    if len(filesWrongStructure) == 0:
        return True
    else:
        return filesWrongStructure


# def compareFile2Dir(file1, dirToCheck):
    
