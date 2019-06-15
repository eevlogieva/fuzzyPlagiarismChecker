import argparse

general_description = 'This is a program to check files for plagiarism and to check if html files conform to a given structure. There are 5 usecases it supports.'
description_usecase1 = 'If the usecase is cmpTwoFiles, the files are given as aruments --file1 and --file2 and the result is a number between 0 and 100, 0 being files are different, 100 meaning they are the same.'
description_usecase2 = 'If the usecase is cmpFile2Dir in --file1 is given the file and it will check it against the files in --dir. The result will be a list of similar files to file1.'
description_usecase3 = 'If the usecase is cmpFilesInDir it will compare all the files in --dir two by two and output tuples of similar files.'
description_usecase4 = 'If the usecase is checkStructure in --file1 is expected an html file and in --structureFile is expected a text file containing html structure. It will output True if the file conforms the structure and False otherwise.'
description_usecase5 = 'If the usecase is checkStructureDir, in --structureFile a text file with a structure is expected, and all the html files in --dir will be checked against it. The result will be a list with files not conforming to the structureFile.'


class ArgParser:
    def __init__(self, givenArgs=''):
        parser = argparse.ArgumentParser(description=general_description + description_usecase1 + description_usecase2 + description_usecase3 + description_usecase4 + description_usecase5)
        parser.add_argument('--usecase', help='The chosen usecase. Possibe values: cmpTwoFiles, checkStructure, checkStructureDir, cmpFile2Dir, cmpFilesInDir')
        parser.add_argument('--file1', help='Required if usecase is cmpTwoFiles, checkStructure or cmpFile2Dirfile. This is the file to be processed.')
        parser.add_argument('--file2', help='Required if usecase is cmpTwoFiles. This is the file to be compared to file1.')
        parser.add_argument('--structureFile', help='Required if usecase is checkStructure or checkStructureDir. This is the a text file, containing the html structure that needs to be checked.')
        parser.add_argument('--dir', help='Required if usecase is checkStructureDir, cmpFile2Dirfile or cmpFilesInDir. This is the directory name that will be checked')
        if givenArgs == '':
            self.args = parser.parse_args()
        else:
            self.args = parser.parse_args(givenArgs)

    def getUsecase(self):
        return self.args.usecase

    def getFile1(self):
        return self.args.file1

    def getFile2(self):
        return self.args.file2

    def getStructureFile(self):
        return self.args.structureFile

    def getDir(self):
        return self.args.dir
