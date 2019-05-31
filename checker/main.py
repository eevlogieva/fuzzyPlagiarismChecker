from checker.argParser.argument_parser import ArgParser
from checker.usecases import *
import sys


def calculateResult(arguments):
    parser = ArgParser(arguments)

    if parser.getUsecase() == "cmpTwoFiles":
        return compareTwoFiles(parser.getFile1(), parser.getFile2())
    elif parser.getUsecase() == "checkStructure":
        return isFileStructureTheSame(parser.getStructureFile(), parser.getFile1())
    elif parser.getUsecase() == "checkStructureDir":
        return isDirStructureTheSame(parser.getStructureFile(), parser.getDir())
    elif parser.getUsecase() == "cmpFile2Dir":
        return compareFile2Dir(parser.getFile1(), parser.getDir())
    elif parser.getUsecase() == "cmpFilesInDir":
        return compareFilesInDir(parser.getDir())


if __name__ == '__main__':
    print(calculateResult(sys.argv[1:]))