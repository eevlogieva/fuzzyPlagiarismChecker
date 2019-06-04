import PySimpleGUI as sg
from ssdeepComparator.ssdeep_comparator import Comparator


def extract_filenames():
    event, (filename, filename2) = sg.Window('Compare two files for similarities'). Layout([[sg.Text('First file')], [sg.Input(), sg.FileBrowse()], 
       [sg.Text('Second file')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]]).Read()
    return (filename, filename2)


def extract_file_and_dir():
    event, (filename, dirname) = sg.Window('Get filename to check'). Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()],
        [sg.Text('Dirname')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]]).Read()

    return (filename, dirname)


def check_file_2_file_gui():
    fileNameToCheck, fileName2ToCheck = extract_filenames()

    comparator = Comparator()
    sg.Popup("The system successfully compared the two files.\n" + "Percentage similarity: " + str(comparator.compare(fileNameToCheck, fileName2ToCheck)))


def check_file_2_dir_gui():
    fileNameToCheck, dirName2ToCheck = extract_file_and_dir()

    comparator = Comparator()
    sg.Popup('Result', "Similar files: " + str(comparator.compare(fileNameToCheck, dirName2ToCheck)))


if __name__ == '__main__':
    check_file_2_file_gui()
