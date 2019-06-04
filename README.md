# fuzzyPlagiarismChecker
This is a tool to compare files with the mechanism of fuzzy hashing. It can be used from the command line or throug a gui.

## Installation

1. Clone/Download the repo
2. Create and activate a virtual environment in the repo's folder
3. Install all the dependencies for the project: from the project dir fuzzyPlagiarismChecker run
```
pip install -r requirements.txt
```
4. Install the project: from the project dir fuzzyPlagiarismChecker run
```
pip install .
```
5. Try out some usecases from the command line, e.g.:
```
python checker/main.py --usecase cmpTwoFiles --file1 ./tests/resources/copyOfSimpleFile.html --file2 ./tests/resources/simpleFile.html
```
Expected result: 100

For more information, you can also use the help option, e.g.:
```
python checker/main.py -h
```

## Usage
### Comparing two files
When comparing two files the `--usecase` option has to have the value `cmpTwoFiles`, and then the two files are given with the options `--file1` and `--file2`. The tool will output the percentage of similarity between the two files, calculated with the ssdeep python library for fuzzy hashing.

### Check if a file conforms to a given html structure
The tool has the additional option for ochecking html ftructure of a file. The `--usecase` option should take the value `checkStructure`. The file to be checked is given in the `--file1-` and the structure is put in a txt file and the path to te file is given in the option `--structureFile`. The tool outputs `True` if the file conforms to the given structure, and a tuple of `(False, <%similarity>)`.
