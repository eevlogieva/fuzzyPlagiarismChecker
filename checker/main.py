from argument_parser import ArgParser
from usecases import compare2Files

TRESHOLD = 21


def console():
    # isRequiredTagsPresent = False
    # try:
        # requiredTagsFile = open("requiredTagsStructure.txt", 'r')
        # isRequiredTagsPresent = True
    # except FileNotFoundError as e:
        # pass

    # tagsFile = open("tags.txt", 'w')
    # contentsFile = open("content.txt", 'w')

    fileNameToCheck = input("Input the filename to be checked: ")
    return fileNameToCheck


if __name__ == '__main__':
    parser = ArgParser()

    if parser.getUsecase() == "cmp2files":
        print(compare2Files(parser.getFile1(), parser.getFile2()))

    # parser = MyHTMLParser("tags.txt", "content.txt")
    # parser.feed(content)

    # if isRequiredTagsPresent:
        # validateRequiredTags(requiredTagsFile, open("tags.txt", 'r'))
    # fileName2ToCheck = input("Input the second filename to be checked: ")
    # file2ToCheck = open(fileName2ToCheck, 'r')

    # comparator = Comparator()

    # print("Percentage similarity: " + str(comparator.compare(fileNameToCheck, fileName2ToCheck)))
