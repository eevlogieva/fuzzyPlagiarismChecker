import PySimpleGUI as sg
from checker.usecases import *


USECASES_DICT = {
    'cmpTwoFiles': 'Compare two files',
    'checkStructure': 'Check the structure of an html file',
    'checkStructureDir': 'Check the structure of html files in dir',
    'cmpFile2Dir': 'Compare a single file to all files in dir',
    'cmpFilesInDir': 'Compare all the files in a dir'
}


class GUI:
    def extractUsecase(self):
        layout = [[sg.InputCombo(list(USECASES_DICT.values()))], [sg.OK(), sg.Cancel()]]
        window = sg.Window('Choose a usecase')
        (button, usecase_arr) = window.Layout(layout).Read()
        if button == 'Cancel':
            exit()
        window.Close()
        return [key for key, value in USECASES_DICT.items() if value == usecase_arr[0]][0]

    def extractFiles(self):
        window = sg.Window(USECASES_DICT['cmpTwoFiles'])
        event, (filename, filename2) = window. Layout([[sg.Text('First file')], [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Second file')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]]).Read()
        if event == 'Cancel':
            exit()
        window.Close()
        return (filename, filename2)

    def extractStructureFileAndFile1(self):
        window = sg.Window(USECASES_DICT['checkStructure'])
        event, (structureFilename, filename1) = window. Layout([[sg.Text('Structure file')], [sg.Input(), sg.FileBrowse()], 
            [sg.Text('File to check')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]]).Read()
        if event == 'Cancel':
            exit()
        window.Close()
        return (structureFilename, filename1)

    def extractFileAndDir(self):
        window = sg.Window(USECASES_DICT['cmpFile2Dir'])
        event, (filename, dirname) = window. Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()],
            [sg.Text('Dir to check')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()
        if event == 'Cancel':
            exit()
        window.Close()
        return (filename, dirname)

    def extractStructureFileAndDir(self):
        window = sg.Window(USECASES_DICT['checkStructureDir'])
        event, (structureFilename, dirname) = window. Layout([[sg.Text('Structure file')], [sg.Input(), sg.FileBrowse()],
            [sg.Text('Dir to check')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()
        if event == 'Cancel':
            exit()
        window.Close()
        return (structureFilename, dirname)

    def extractDir(self):
        window = sg.Window(USECASES_DICT['cmpFilesInDir'])
        event, dirname = window. Layout([[sg.Text('Dir to check')], [sg.Input(), sg.FolderBrowse()], 
            [sg.OK(), sg.Cancel()]]).Read()
        if event == 'Cancel':
            exit()        
        window.Close()
        return dirname

    def popupResult(self, windowTitle, message):
        window = sg.Window(windowTitle)
        event = window.Layout([[sg.Multiline(default_text=message, size=(100, 10), disabled=True)], [sg.OK()]]).Read()
        if event == 'OK':
            window.Close()
            exit()

    def validateInput(self, args):
        for arg in args:
            if arg == '':
                self.popupResult('ERROR! \n Some of the field names were left blank!')
                exit()


def pretty(d, indent=0):
    result = ''
    for key, value in d.items():
        result += ('\t' * indent + str(key)) + '\n'

        if isinstance(value, list):
            result += '['
            for elem in value:
                result += '\t' + str(elem) + '\n'
            result += ']' + '\n'
        else:
            result += ('\t' * (indent + 1) + str(value)) + '\n'
    return result


if __name__ == '__main__':
    gui = GUI()
    usecase = gui.extractUsecase()
    message = ''

    if usecase == 'cmpTwoFiles':
        file1, file2 = gui.extractFiles()
        gui.validateInput([file1, file2])
        fuzzy_similarity = compareTwoFiles(file1, file2)
        if fuzzy_similarity > 0:
            message = 'The files are with similatities. \n Percentage similatities: ' + str(fuzzy_similarity)
        else:
            message = 'The files have no similarities.'

        sg.Popup(message)

    elif usecase == 'checkStructure':
        structureFile, file1 = gui.extractStructureFileAndFile1()
        gui.validateInput([structureFile, file1])
        try:
            isSame, percentage = isFileStructureTheSame(structureFile, file1)
            if isSame is True:
                message = 'The file complies with the given structure. \n'
            else:
                message = 'The file does not comply with the given structure. \n'
                message += ('Percentage similarities between the structures: ' + str(percentage))
        except TypeError as e:
            message = 'ERROR! \n' + str(e)

        sg.Popup(message)

    elif usecase == 'checkStructureDir':
        structureFile, dirToCheck = gui.extractStructureFileAndDir()
        gui.validateInput([structureFile, dirToCheck])
        result = isDirStructureTheSame(structureFile, dirToCheck)
        isSame = result[0]
        wrongFiles = result[1:]
        if isSame is True:
            message = 'All the files in the dir comply with the given structure. \n'
            sg.Popup(message)
        else:
            message = 'Some files in the dir do not comply with the given structure. \nDirname: ' + dirToCheck + '\nFiles that do not comply: [' + ', '.join(wrongFiles) + ']'
            gui.popupResult('Result from checking the structure of html files in a dir', message)

    elif usecase == 'cmpFile2Dir':
        file1, dirToCheck = gui.extractFileAndDir()
        gui.validateInput([file1, dirToCheck])
        similarFiles = compareFile2Dir(file1, dirToCheck)
        file1 = file1[len(dirToCheck):]
        if not similarFiles:
            message = 'The dir does not contain similar files to the given one.'
            sg.Popup(message)
        else:
            message = 'Some of the files in the dir have similarities with the given file.\nDirname: ' + dirToCheck + '\nFiles, similar to ' + file1 + ': [' + ',\n'.join(similarFiles) + ']'
            gui.popupResult('Result from comparing a file to files in a dir', message)

    elif usecase == 'cmpFilesInDir':
        dirToCheck = gui.extractDir()[0]
        gui.validateInput([dirToCheck])
        similarFiles = compareFilesInDir(dirToCheck)
        if not similarFiles:
            message = 'The dir does not contain similar files.'
            sg.Popup(message)
        else:
            message = 'The dir ' + dirToCheck + ' contains similar files.\nThe result is also saved in the file /fuzzyPlagiarismChecker/resultReport.xml\nHere are the similar files in format <file1>: [<similarFile>, <percentSimilarity>]: \n ' + pretty(similarFiles)
            gui.popupResult('Result from comparing files in a dir', message)
