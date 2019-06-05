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
        event, (filename, dirname) = sg.Window('Compare a single file to all files in dir'). Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()],
            [sg.Text('Dir to check')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()

        return (filename, dirname)

    def extractStructureFileAndDir(self):
        event, (structureFilename, dirname) = sg.Window('Check the structure of html files in dir'). Layout([[sg.Text('Structure file')], [sg.Input(), sg.FileBrowse()],
            [sg.Text('Dir to check')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()

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


if __name__ == '__main__':
    gui = GUI()
    usecase = gui.extractUsecase()

    if usecase == 'cmpTwoFiles':
        file1, file2 = gui.extractFiles()
        gui.popupResult(compareTwoFiles(file1, file2))

    elif usecase == 'checkStructure':
        structureFile, file1 = gui.extractStructureFileAndFile1()
        gui.popupResult(isFileStructureTheSame(structureFile, file1))

    elif usecase == 'checkStructureDir':
        structureFile, dirToCheck = gui.extractStructureFileAndDir()
        gui.popupResult(isDirStructureTheSame(structureFile, dirToCheck))

    elif usecase == 'cmpFile2Dir':
        file1, dirToCheck = gui.extractFileAndDir()
        gui.popupResult(compareFile2Dir(file1, dirToCheck))

    elif usecase == 'cmpFilesInDir':
        dirToCheck = gui.extractDir()
        gui.popupResult(compareFilesInDir(dirToCheck))
