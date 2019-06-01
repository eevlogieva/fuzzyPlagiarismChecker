import ssdeep
import os

from checker.htmlParser.html_parser import MyHTMLParser, removeAllWhitespace

TRESHOLD = 21


class Comparator:

    def compare(self, firstFileName, secondFileOrDirName):
        hash1 = self.hashContentOfFile(firstFileName)

        if os.path.isfile(secondFileOrDirName):
            secondFileName = secondFileOrDirName
            hash2 = self.hashContentOfFile(secondFileName)
            return ssdeep.compare(hash1, hash2)
        else:
            dirToCheck = secondFileOrDirName
            similar_files = []
            filesInDir = self.hashAllFilesInDir(dirToCheck)
            for fileTuple in filesInDir:
                currFileName = fileTuple[1]
                currFileHash = fileTuple[0]
                if ssdeep.compare(hash1, currFileHash) > TRESHOLD and firstFileName != currFileName:
                    similar_files.append(currFileName)
            return similar_files

    def extractSimilarFiles(self, dirToProcess):
        similarFilesDict = {}
        filesInDir = self.hashAllFilesInDir(dirToProcess)
        for fileTuple in filesInDir:
            currFileName = fileTuple[1]
            currFileHash = fileTuple[0]
            filesInDir.remove(fileTuple)
            similarFiles = []
            for innerFileTuple in filesInDir:
                similarityCoefficient = ssdeep.compare(currFileHash, innerFileTuple[0])
                if similarityCoefficient > TRESHOLD:
                    similarFiles.append((innerFileTuple[1], similarityCoefficient))
            if similarFiles:
                similarFilesDict[currFileName] = similarFiles
        return similarFilesDict

    def hashAllFilesInDir(self, dirToProcess):
        hashedFiles = []
        for dirName, subdirList, fileList in os.walk(dirToProcess):
                for fname in fileList:
                    filePath = os.path.join(dirName, fname)
                    hashedFiles.append((self.hashContentOfFile(filePath), filePath))
        return hashedFiles

    def compareStrings(self, str1, str2):
        hash1 = ssdeep.hash(str1)
        hash2 = ssdeep.hash(str2)

        return ssdeep.compare(hash1, hash2)

    def hashContentOfFile(self, fileName):
        try:
            if fileName.split('.')[-1] == 'html':
                htmlParser = MyHTMLParser()
                htmlParser.feed(open(fileName, 'r').read())
                content = removeAllWhitespace(htmlParser.getContent())
                return ssdeep.hash(content)
            else:
                return ssdeep.hash_from_file(fileName)
        except IndexError:
            return ssdeep.hash_from_file(fileName)
