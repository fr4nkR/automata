import string

"""This program will read from a file, for each word, with the delimiter as a blank space, it will evalaute if the word is part of a language.
    If no matching languages are found, 'none' is outputed.
"""
def get_words(filename: str) -> list:

    # This closes the file for you when you are done
    with open(filename, 'r') as myFile:
        contents = myFile.read()

    list_of_words:list = []
    for word in contents.split():
        list_of_words.append(word)

    return list_of_words, filename

def id_language(word: str) -> bool:
    alphabet_list_lowercase:list = list(string.ascii_lowercase)
    alphabet_list_uppercase:list = list(string.ascii_uppercase)
    english_alphabet = [*alphabet_list_lowercase, *alphabet_list_uppercase]
    numbers_list:list =  [str(i) for i in list(range(0, 10))]
    language_complete_alphabet:list = [*english_alphabet, *numbers_list]
    # print(language_complete_alphabet)
    if len(word) < 2:
        return False
    if word[0] not in english_alphabet:
            return False
    for character in word[1:]:
        if character not in language_complete_alphabet:
            return False
    return True

def num_language(word: str) -> bool:
    numbers_list:list = [str(i) for i in list(range(0, 10))]
    for character in word:
        if character not in numbers_list:
            return False
    return True

def semicolon_language(word: str) -> bool:
    if word != ';':
        return False
    return True

def and_language(word: str) -> bool:
    if word != "&&":
        return False
    return True

def while_language(word: str) -> bool:
    if word != "while":
        return False
    return True

def create_output_string(word: str) -> str:
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
        return','.join(map(str,output_words))

def main() -> None:
    list_of_words, filename = get_words("test.txt")
    for word in list_of_words:
        if list_of_words[0] == word:
            print(
            f"File: {filename}\n{word}: {create_output_string(word)}")
        else:
            print(f"{word}: {create_output_string(word)}")

if __name__ == "__main__":
    main()