import argparse


class ArgParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--usecase', help='The chosen usecase. Possibe values: cmp2files, checkStructure, checkStructureDir')
        parser.add_argument('--file1', help='file 1')
        parser.add_argument('--file2', help='file 2')
        parser.add_argument('--structureFile', help='A file, containing the html structure that needs to be present.')
        parser.add_argument('--dir', help='Dir')
        self.args = parser.parse_args()

    def getUsecase(self):
        return self.args.usecase

    def getFile1(self):
        return self.args.file1

    def getFile2(self):
        return self.args.file2

    def getStructureFile(self):
        return self.structureFile

    def getDir(self):
        return self.dir
