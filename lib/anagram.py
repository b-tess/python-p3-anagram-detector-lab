# your code goes here!
class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, anagrams_list):
        valid_anagrams = []
        for anagram in anagrams_list:
            if sorted([letter for letter in anagram]) == sorted([letter for letter in self.word]):
                valid_anagrams.append(anagram)

        return valid_anagrams