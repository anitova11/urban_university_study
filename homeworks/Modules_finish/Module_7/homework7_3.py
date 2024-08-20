import string


class WordsFinder:
    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        words = []
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    line_new = line.lower()
                    for char in string.punctuation:
                        line_new = line_new.replace(char, '')
                    words.extend(line_new.split())
                    all_words[i] = words
            words = []
        return all_words

    def find(self, word):
        finder = {}
        for name, words in self.get_all_words().items():
            for k in range(len(words)):
                if words[k] == word.lower():
                    finder[name] = k + 1
                    break
        return finder

    def count(self, word):
        counter = {}
        for name, words in self.get_all_words().items():
            num = 0
            for k in range(len(words)):
                if words[k] == word.lower():
                    num += 1
            counter[name] = num
        return counter


p = WordsFinder('file_name.txt', 'test.txt')
print(p.get_all_words())
print(p.find('teXt'))
print(p.count('text'))
