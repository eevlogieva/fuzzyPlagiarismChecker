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

    def extractFilenames(self):
        window = sg.Window('Compare two files for similarities')
        event, (filename, filename2) = window. Layout([[sg.Text('First file')], [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Second file')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]]).Read()
        window.Close()
        return (filename, filename2)

    def extract_file_and_dir(self):
        event, (filename, dirname) = sg.Window('Get filename to check'). Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()],
            [sg.Text('Dirname')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()

        return (filename, dirname)

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
        file1, file2 = gui.extractFilenames()
        gui.popupResult(compareTwoFiles(file1, file2))
    elif usecase == 'checkStructure':
        print(isFileStructureTheSame(parser.getStructureFile(), parser.getFile1()))
    elif usecase == 'checkStructureDir':
        print(isDirStructureTheSame(parser.getStructureFile(), parser.getDir()))
    elif usecase == 'cmpFile2Dir':
        print(compareFile2Dir(parser.getFile1(), parser.getDir()))
    elif usecase == 'cmpFilesInDir':
        print(compareFilesInDir(parser.getDir()))
    # print(usecase)