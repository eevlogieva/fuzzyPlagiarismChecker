from argument_parser import ArgParser
from usecases import compareTwoFiles, isFileStructureTheSame, isDirStructureTheSame, compareFile2Dir

TRESHOLD = 21


if __name__ == '__main__':
    parser = ArgParser()

    if parser.getUsecase() == "cmpTwoFiles":
        return compareTwoFiles(parser.getFile1(), parser.getFile2())
    elif parser.getUsecase() == "checkStructure":
        return isFileStructureTheSame(parser.getStructureFile(), parser.getFile1())
    elif parser.getUsecase() == "checkStructureDir":
        return isDirStructureTheSame(parser.getStructureFile(), parser.getDir())
    elif parser.getUsecase() == "cmpFile2Dir":
        return compareFile2Dir(parser.getFile1(), parser.getDir())
