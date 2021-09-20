import string

"""This program will read from a file, for each word, with the delimiter as a blank space, it will evalaute if the word is part of a language.
    If no matching languages are found, 'none' is outputed.
"""
def get_words(filename: str) -> list:
    '''This takes each word individually and places it in a list. I assumed there can be multiple lines.'''
    with open(filename, 'r') as myFile:
        contents = myFile.read()

    list_of_words:list = []
    for word in contents.split():
        list_of_words.append(word)

    return list_of_words, filename

def id_language(word: str) -> bool:
    '''This Represents the ID language'''
    # defining useful alphabets a...z, A...Z, a...z and A...Z, 0...9, and the combination of all of them
    alphabet_list_lowercase:list = list(string.ascii_lowercase)
    alphabet_list_uppercase:list = list(string.ascii_uppercase)
    english_alphabet = [*alphabet_list_lowercase, *alphabet_list_uppercase]
    numbers_list:list =  [str(i) for i in list(range(0, 10))]
    language_complete_alphabet:list = [*english_alphabet, *numbers_list]
    # This is not part of the language itseld, but rather to avoid any errors that the program might produce if given strings that are not at least length 2,
    # since we use index 0 and 1 explicitely.
    if len(word) < 2:
        return False
    if word[0] not in english_alphabet:
            return False
    for character in word[1:]:
        if character not in language_complete_alphabet:
            return False
    return True

def num_language(word: str) -> bool:
    '''This Represents the num language'''
    # defining 0...9
    numbers_list:list = [str(i) for i in list(range(0, 10))]
    for character in word:
        if character not in numbers_list:
            return False
    return True

def semicolon_language(word: str) -> bool:
    '''This Represents the semicolon language'''
    if word != ';':
        return False
    return True

def and_language(word: str) -> bool:
    '''This Represents the and language'''
    if word != "&&":
        return False
    return True

def while_language(word: str) -> bool:
    '''This Represents the while language'''
    if word != "while":
        return False
    return True

def create_output_string(word: str) -> str:
    '''This will create the resulting output string that will be displayed'''
    id_l:str = "Id" if id_language(word) else ""
    num_l:str = "Num" if num_language(word) else ""
    semicolon_l:str = "Semicolon" if semicolon_language(word) else ""
    and_l:str = "And" if and_language(word) else ""
    while_l:str = "While" if while_language(word) else ""
    
    raw_of_output_words:list = [id_l, num_l, semicolon_l, and_l, while_l]
    output_words:list = list(filter(lambda output_word: output_word != "", raw_of_output_words))
    if len(output_words) == 0:
        return "none"
    else:
        # this will output the string desired separated by commas, except if it is the last word.
        return','.join(map(str,output_words))

def main() -> None:
    # We read from out file
    list_of_words, filename = get_words("test.txt")
    for word in list_of_words:
        # this will output the "File ..." string of the output, only for the first word found in the list
        if list_of_words[0] == word:
            print(
            f"File: {filename}\n{word}: {create_output_string(word)}")
        else:
            print(f"{word}: {create_output_string(word)}")

if __name__ == "__main__":
    main()