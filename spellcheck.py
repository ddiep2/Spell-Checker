'''
Dylan Diep
This program is an adaptation of Ben Dicken's Spell Checker, 
which checks a text file for misspelled words using a dictionary file.
'''
def read_spellings():
    misspelled_words = {}
    with open('misspellings.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if "->" in line:
                wrong, correct = line.split("->")
                wrong = wrong.strip()
                correct = correct.strip()
                misspelled_words[wrong] = correct
    return misspelled_words
def fix_word(word, spellings):
    end_punctuation = ''
    if len(word) > 0 and word[-1] in '.,!?;:':
        end_punctuation = word[-1]
        word = word[:-1]
    starts_capital = len(word) > 0 and word[0].isupper()
    word_lower = word.lower()
    if word_lower in spellings:
        correct = spellings[word_lower]
        if starts_capital:
            correct = correct.capitalize()
        return correct + end_punctuation
    return word + end_punctuation
def correct_spelling(filename, spellings):
    output_filename = "output_" + filename
    input_file = open(filename, "r")
    output_file = open(output_filename, "w")
    for line in input_file:
        current_word = ""
        new_line = ""
        for char in line:
            if char.isalpha() or char in "'-":
                current_word += char
            else:
                if current_word != "":
                    new_line += fix_word(current_word, spellings)
                    current_word = ""
                new_line += char
        if current_word != "":
            new_line += fix_word(current_word, spellings)
        output_file.write(new_line)           
    input_file.close()
    output_file.close()