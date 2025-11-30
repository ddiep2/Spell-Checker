Spell Checker & Text Auto-Correction Tool

This project is a Python-based spell-checking script that automatically detects and corrects misspelled words in a text file. It uses a customizable dictionary of common misspellings to replace incorrect words while preserving capitalization and punctuation.

The program is adapted from Ben Dicken’s spell checker and expanded with cleaner parsing, punctuation handling, and structured file processing.

Features:

Customizable dictionary support
Reads correction pairs (e.g., teh -> the) from a misspellings.txt file.

Automatic word correction
Corrects words based on dictionary matches.

Preserves writing style

Maintains ending punctuation (. , ! ? ; :)

Preserves capitalization of corrected words

Handles hyphens and apostrophes inside words

Processes entire text files
Outputs a corrected version of the input text as output_<filename>.

How It Works:
1. Load misspellings

The program reads lines from misspellings.txt formatted like:

teh -> the
adress -> address
recieve -> receive


These are stored in a dictionary used for lookups.

2. Process each word

For each word in the text:

Strip punctuation

Check if it appears in the misspelling dictionary

Preserve capitalization

Reattach punctuation

3. Write corrected output

A new file named:

output_<original_filename>


is created with all corrections applied.

Usage:
1. Add your misspellings

Edit misspellings.txt and list each correction:

wrong -> right
mispell -> misspell
enviroment -> environment

2. Place the text you want to correct in the same folder

Example: essay.txt

3. Run the program
python spell_checker.py


OR within a Python environment:

spellings = read_spellings()
correct_spelling("essay.txt", spellings)

4. Get your corrected file

A new file will be created:

output_essay.txt

Example:

Input text:

Teh quick brown fox jumpd over teh lazi dog.


Output text:

The quick brown fox jumped over the lazy dog.


(Assuming the dictionary contains those corrections.)

Potential Improvements:

Add command-line arguments (e.g., --input, --output)

Implement Levenshtein distance–based suggestions

Add support for full dictionaries (e.g., WordNet)

Build a GUI or web interface

Author:

Dylan Diep

Adapted from coursework by Ben Dicken, expanded and documented for clarity and usability.
