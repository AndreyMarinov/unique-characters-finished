'''Modul for checking if the characters in string are unique'''


def is_unique(words:str) -> bool:
    '''Function that checks if there are repeating characters

    :param: words: str word to compare if the characters in it are unique
    :return: bool  if there are only unique characters in the str
    '''
    return len(set(words)) == len(words)
