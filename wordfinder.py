from random import randint

class WordFinder:
    """
    Class for making list of words from a file and then picking a random word
    
    attributes
    ----------------------
    self.wordlist --> list of all words read from file
    """
    def __init__(self, path):
        self.wordlist = open_file(path)

    def __repr__(self):
        return f"{len(self.wordlist)} words read"

    def random(self):
        idx = randint(0, len(self.wordlist) - 1)
        return self.wordlist[idx]

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)

    def random(self):
        word = super().random()
        while word == '' or word[0] == '#':
            word = super().random()

        return word 

        
def open_file(path):
    file = open(path, "r")

    res = file.read()
    word_list = res.split('\n')

    file.close()
    return word_list
