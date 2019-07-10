# fuzzyPlagiarismChecker
This is a tool to compare files with the mechanism of fuzzy hashing. It can be used from the command line or throug a gui.

## Installation

### With the source code on Linux

1. Install `python3`, `pip3` and `libfuzzy-dev` (needed for the fuzzy hashing)
```
sudo apt install python3 python3-pip libfuzzy-dev
```
2. Clone/Download the repo
3. Create and activate a virtual environment in the repo's folder
4. Install all the dependencies for the project: from the project dir fuzzyPlagiarismChecker run
```
pip install -r requirements.txt
```
5. Install the project: from the project dir fuzzyPlagiarismChecker run
```
pip install .
```
6. Try out some usecases from the command line, e.g.:
```
python checker/main.py --usecase cmpTwoFiles --file1 ./tests/resources/copyOfSimpleFile.html --file2 ./tests/resources/simpleFile.html
```
Expected result: 100

For more information, you can also use the help option, e.g.:
```
python checker/main.py -h
```
### As a docker contained
The system is also availavble as a docker container. It can be downloaded and used like this:
```
sudo docker pull eevlogieva/fuzzy_plagiarism_checker:latest
sudo docker run -it eevlogieva/fuzzy_plagiarism_checker:latest
cd fuzzyPlagiarismChecker
python3 checker/main.py -h
```
### With the source code on Windows
As on Windows there is no libfuzzy-dev library to install, the installation process is a bit different.
1. Download and install Python3 (with pip)
2. Download and install the ssdeep for Windows library [here](github.com/MacDue/ssdeep-windows-32_64)
3. From the `requirements.txt` file in the current project remove the following lines:
```
cffi==1.12.3,
pycparser==2.19,
ssdeep==3.3
```
4. Navigate to the `fuzzyPlagiarismChecker` dir and execute the commands:
```
pip install -r requirements.txt
pip install .
```
5. The tool is ready to use by:
```
python3 checker\main.py -h
python3 checker\gui.py
```

## Usage through the CLI
### Comparing two files
When comparing two files the `--usecase` option has to have the value `cmpTwoFiles`, and then the two files are given with the options `--file1` and `--file2`. The tool will output the percentage of similarity between the two files, calculated with the ssdeep python library for fuzzy hashing.

### Check if a file conforms to a given html structure
The tool has the additional option for checking html ftructure of a file. The `--usecase` option should take the value `checkStructure`. The file to be checked is given in the `--file1` and the structure is put in a txt file and the path to te file is given in the option `--structureFile`. The tool outputs `True` if the file conforms to the given structure, and a tuple of `(False, <%similarity>)`.

### Check if the files in a dir conform to a given html structure
The tool has the additional option for checking html ftructure of all the files in a dir. The `--usecase` option should take the value `checkStructureDir`. The dir to be checked is given in the `--dir` and the structure is put in a txt file and the path to te file is given in the option `--structureFile`. The tool outputs `True` if all the html files conform to the given structure, and a list of files if some of the files do not conform.

### Comparing all the files in a dir
When comparing the files (every file is compared with everyone else) the `--usecase` option has to have the value `cmpFilesInDir`, and then the dir is given with the option `--dir`. The tool will output a list of similar files (if there are any) together with percentage of similarity between them.

## Usage through the GUI
The GUI can be started on Windows simply by executing the `gui.exe` file in the `checker` dir. 