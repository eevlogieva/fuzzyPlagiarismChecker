import ssdeep
import os

from checker.htmlParser.html_parser import MyHTMLParser, removeAllWhitespace

TRESHOLD = 21


class Comparator:
    def __init__(self, ssdeepInstance=ssdeep):
        self.ssdeep = ssdeepInstance

    def compare(self, firstFileName, secondFileOrDirName):
        hash1 = self.hashContentOfFile(firstFileName)

        if os.path.isfile(secondFileOrDirName):
            secondFileName = secondFileOrDirName
            hash2 = self.hashContentOfFile(secondFileName)
            return self.ssdeep.compare(hash1, hash2)
        else:
            dirToCheck = secondFileOrDirName
            similar_files = []
            filesInDir = self.hashAllFilesInDir(dirToCheck)
            for fileTuple in filesInDir:
                currFileName = fileTuple[1]
                currFileHash = fileTuple[0]
                if self.ssdeep.compare(hash1, currFileHash) > TRESHOLD and firstFileName != currFileName:
                    similar_files.append(currFileName)
            return similar_files

    def extractSimilarFiles(self, dirToProcess):
        similarFilesDict = {}
        filesInDir = self.hashAllFilesInDir(dirToProcess)
        for index, fileTuple in enumerate(filesInDir):
            currFileName = fileTuple[1]
            currFileHash = fileTuple[0]
            similarFiles = []
            for innerFileTuple in filesInDir[index + 1:]:
                similarityCoefficient = self.ssdeep.compare(currFileHash, innerFileTuple[0])
                if similarityCoefficient > TRESHOLD:
                    similarFiles.append((innerFileTuple[1], similarityCoefficient))
            if similarFiles:
                similarFilesDict[currFileName] = similarFiles
        return similarFilesDict

    def hashAllFilesInDir(self, dirToProcess):
        hashedFiles = []
        for dirName, subdirList, fileList in os.walk(dirToProcess):
                for fname in fileList:
                    # do not consider hidden files
                    if not os.path.basename(fname).startswith('.'):
                        filePath = os.path.join(dirName, fname)
                        hashedFiles.append((self.hashContentOfFile(filePath), filePath))
        return hashedFiles

    def compareStrings(self, str1, str2):
        hash1 = self.ssdeep.hash(str1)
        hash2 = self.ssdeep.hash(str2)

        return self.ssdeep.compare(hash1, hash2)

    def hashContentOfFile(self, fileName):
        try:
            if fileName.split('.')[-1] == 'html':
                htmlParser = MyHTMLParser()
                htmlParser.feed(open(fileName, 'r').read())
                content = removeAllWhitespace(htmlParser.getContent())
                return self.ssdeep.hash(content)
            else:
                return self.ssdeep.hash_from_file(fileName)
        except IndexError:
            return self.ssdeep.hash_from_file(fileName)
