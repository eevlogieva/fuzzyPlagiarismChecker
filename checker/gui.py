import PySimpleGUI as sg
from checker.usecases import *


USECASES_DICT = {
    'Compare two files': 'cmpTwoFiles',
    'Check the structure of a html file': 'checkStructure',
    'Check the structure of html files in dir': 'checkStructureDir',
    'Compare a single file to all files in dir': 'cmpFile2Dir',
    'Compare all the files in a dir': 'cmpFilesInDir'
}


class GUI:
    def extractUsecase(self):
        layout = [[sg.InputCombo(list(USECASES_DICT.keys()))], [sg.OK(), sg.Cancel()]]
        window = sg.Window('Choose a usecase')
        (button, usecase_arr) = window.Layout(layout).Read()
        window.Close()
        return USECASES_DICT[usecase_arr[0]]

    def extractFiles(self):
        window = sg.Window('Compare two files for similarities')
        event, (filename, filename2) = window. Layout([[sg.Text('First file')], [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Second file')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]]).Read()
        window.Close()
        return (filename, filename2)

    def extractStructureFileAndFile1(self):
        window = sg.Window('Check the structure of a html file')
        event, (structureFilename, filename1) = window. Layout([[sg.Text('Structure file')], [sg.Input(), sg.FileBrowse()], 
            [sg.Text('File to check')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]]).Read()
        window.Close()
        return (structureFilename, filename1)

    def extractFileAndDir(self):
        window = sg.Window('Compare a single file to all files in dir')
        event, (filename, dirname) = window. Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()],
            [sg.Text('Dir to check')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()

        window.Close()
        return (filename, dirname)

    def extractStructureFileAndDir(self):
        window = sg.Window('Check the structure of html files in dir')
        event, (structureFilename, dirname) = window. Layout([[sg.Text('Structure file')], [sg.Input(), sg.FileBrowse()],
            [sg.Text('Dir to check')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()

        window.Close()
        return (structureFilename, dirname)

    def extractDir(self):
        window = sg.Window('Compare all the files in a dir')
        event, dirname = window. Layout([[sg.Text('Dir to check')], [sg.Input(), sg.FolderBrowse()], 
            [sg.OK(), sg.Cancel()]]).Read()
        window.Close()
        return dirname

    def popupResult(self, stringToPrint):
        sg.Popup(stringToPrint)

    def check_file_2_dir(self):
        fileNameToCheck, dirName2ToCheck = self.extract_file_and_dir()

        comparator = Comparator()
        sg.Popup('Result', 'Similar files: ' + str(comparator.compare(fileNameToCheck, dirName2ToCheck)))


def pretty(d, indent=0):
    result = ''
    for key, value in d.items():
        result += ('\t' * indent + str(key)) + '\n'

        if isinstance(value, dict):
            result += pretty(value, indent + 1)
        else:
            result += ('\t' * (indent + 1) + str(value)) + '\n'
    return result


if __name__ == '__main__':
    gui = GUI()
    usecase = gui.extractUsecase()
    message = ''

    if usecase == 'cmpTwoFiles':
        file1, file2 = gui.extractFiles()
        fuzzy_similarity = compareTwoFiles(file1, file2)
        if fuzzy_similarity > 0:
            message = 'The files are with similatities. \n Percentage similatities: ' + str(fuzzy_similarity)
        else:
            message = 'The files have no similarities.'

        gui.popupResult(message)

    elif usecase == 'checkStructure':
        structureFile, file1 = gui.extractStructureFileAndFile1()
        isSame, percentage = isFileStructureTheSame(structureFile, file1)
        if isSame is True:
            message = 'The file complies with the given structure. \n'
        else:
            message = 'The file does not comply with the given structure. \n'
        message += ('Percentage similarities between the structures: ' + str(percentage))

        gui.popupResult(message)

    elif usecase == 'checkStructureDir':
        structureFile, dirToCheck = gui.extractStructureFileAndDir()
        result = isDirStructureTheSame(structureFile, dirToCheck)
        isSame = result[0]
        wrongFiles = result[1:]
        if isSame is True:
            message = 'The files in the dir complies with the given structure. \n'
        else:
            message = 'Some files do not comply with the given structure. \n These files are: [' + ',\n'.join(wrongFiles) + ']'

        gui.popupResult(message)

    elif usecase == 'cmpFile2Dir':
        file1, dirToCheck = gui.extractFileAndDir()
        similarFiles = compareFile2Dir(file1, dirToCheck)
        if not similarFiles:
            message = 'Thed dir does not contain similar files to the given one.'
        else:
            message = 'Some of the files in the dir have similarities with the given file.\n These files are: [' + ',\n'.join(similarFiles) + ']'

        gui.popupResult(message)

    elif usecase == 'cmpFilesInDir':
        dirToCheck = gui.extractDir()[0]
        similarFiles = compareFilesInDir(dirToCheck)
        if not similarFiles:
            message = 'Thed dir does not contain similar files.'
        else:
            message = 'The dir contains similar files.\n Here are the similar files in format <file1>: [<similarFile>, <percentSimilarity>]: \n ' + pretty(similarFiles)
        gui.popupResult(message)
