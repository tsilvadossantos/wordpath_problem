# Word Ladder Puzzle

A word ladder puzzle begins with two words, and to solve the puzzle one must find a chain of other words to link the two, in which two adjacent words (that is, words in successive steps) differ by one letter by receiving arguments from the command line and searching the path of words in a given file.

The project was develop using the following:
1. Python 2.7.12

## Usage:

1. Clone the world_ladder repository

2. `cd word_path`

3. Help menu: `python app_wordpath.py --help`

4. Run script by passing arguments: `python app_wordpath.py --file=</path/to/file> --word1=<word1> --word2=<word2>`
Example: `python app_wordpath.py --file=/usr/share/dict/words --word1=pie --word2=axe`

## Unit Test Cases

1. `cd word_path/tests`

2. `python -m unittest discover -v`

3. Expected output:
```
test_wordpath_exists (core.test_word_ladder.DataValidationTestCase)
Assert first word has a path two a second given word ... ok
test_wordpath_from_first_word (core.test_word_ladder.DataValidationTestCase)
Assert first word has no path two a second word ... ok
test_wordpath_to_second_word (core.test_word_ladder.DataValidationTestCase)
Assert second word is not path-able ... ok
test_file_exists (core.test_word_ladder.FileTestCase)
Assert a given file exists ... ok
test_file_not_exists (core.test_word_ladder.FileTestCase)
Assert a given file does not exist ... ok

----------------------------------------------------------------------
Ran 5 tests in 23.230s

OK
```

4. If using nosetests: `pip install -r requirements.txt`

5. `nosetests test_wordpath.py -v`
