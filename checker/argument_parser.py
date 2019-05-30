import argparse


class ArgParser:
    def __init__(self, givenArgs=''):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--usecase',
            help='The chosen usecase. Possibe values: cmpTwoFiles, checkStructure, checkStructureDir, cmpFile2Dir, cmpFilesInDir')
        parser.add_argument('--file1', help='file 1')
        parser.add_argument('--file2', help='file 2')
        parser.add_argument('--structureFile', help='A file, containing the html structure that needs to be present.')
        parser.add_argument('--dir', help='Dir')
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
