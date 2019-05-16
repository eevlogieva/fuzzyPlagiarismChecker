import ssdeep
import os


class Comparator:
    def __init__(self, similarityTreshold):
        self.similarityTreshold = similarityTreshold

    def compare(self, firstFileName, secondName):
        hash1 = ssdeep.hash_from_file(firstFileName)

        if os.path.isfile(secondName):
            hash2 = ssdeep.hash_from_file(secondName)
            return ssdeep.compare(hash1, hash2)
        else:
            similar_files = []
            for dirName, subdirList, fileList in os.walk(secondName):
                for fname in fileList:
                    # print("Checking file: " + dirName + '/' + fname)
                    if ssdeep.compare(hash1, ssdeep.hash_from_file(dirName + '/' + fname)) > self.similarityTreshold:
                        fullFileName = str(dirName + '/' + fname)
                        # print("filename is: " + fullFileName)
                        similar_files.append(fullFileName)
            # print("Size of similar_files is: " + str(len(similar_files)))
            return similar_files
