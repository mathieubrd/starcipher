import re

# Represents a dictionnary containing a list of words.
# Does a frequency analysis to get the frequency of each letter in the entire dictionnary.
# When dictionnary file is set (wih the "file_path" setter), call "load" to read and execute the frequency analysis.
class Dictionnary:

    def __init__(self, dict_file):
        file = open(dict_file, 'r')
        self._frequencies = {}
        self._words = []
        num_letters = 0
        for line in file:
            line = line.strip().replace(' ', '')
            if line != '':
                line = line.lower()
                self._words.append(line.lower())
                for char in line:
                    if re.compile('[a-z]').match(char):
                        num_letters += 1
                        if char in self._frequencies:
                            self._frequencies[char] += 1
                        else:
                            self._frequencies[char] = 1;
        file.close()
        for letter, frequency in self._frequencies.items():
            self._frequencies[letter] = round(self._frequencies[letter] / num_letters * 100, 2)

    def contains(self, word):
        if word.lower() in self._words:
            return True
        return False

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        self._file_path = file_path

    @property
    def frequencies(self):
        return self._frequencies
