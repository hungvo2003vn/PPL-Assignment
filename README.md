# PPL-Assignment-1

## Install Requirements

- MacOS/Linux:
```
pip3 install -r requirements.txt
```
- Window:
```
pip install -r requirements.txt
```

## Usage

1.  Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
2. Change current directory to initial/src where there is file run.py

```
Type: python run.py gen
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite
Then type: python run.py test ASTGenSuite
Then type: python run.py test CheckerSuite
Then type: python run.py test CodeGenSuite
```