import argparse


class ArgParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--usecase', help='file 1')
        parser.add_argument('--file1', help='file 1')
        parser.add_argument('--file2', help='file 2')
        self.args = parser.parse_args()

    def getUsecase(self):
        return self.args.usecase

    def getFile1(self):
        return self.args.file1

    def getFile2(self):
        return self.args.file2
