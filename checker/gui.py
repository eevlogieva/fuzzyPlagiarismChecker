import PySimpleGUI as sg
from ssdeep_comparator import Comparator

TRESHOLD = 21


def extract_filenames():
    event, (filename, filename2) = sg.Window('Get filename to check'). Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()],
        [sg.Text('Filename2')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]]).Read()
    return (filename, filename2)


def extract_file_and_dir():
    event, (filename, dirname) = sg.Window('Get filename to check'). Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()],
        [sg.Text('Dirname')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()

    return (filename, dirname)


def check_file_2_file_gui():
    fileNameToCheck, fileName2ToCheck = extract_filenames()

    comparator = Comparator(TRESHOLD)
    sg.Popup('Result', "Percentage similarity: " + str(comparator.compare(fileNameToCheck, fileName2ToCheck)))


def check_file_2_dir_gui():
    fileNameToCheck, dirName2ToCheck = extract_file_and_dir()

    comparator = Comparator(TRESHOLD)
    sg.Popup('Result', "Similar files: " + str(comparator.compare(fileNameToCheck, dirName2ToCheck)))


if __name__ == '__main__':
    check_file_2_dir_gui()
