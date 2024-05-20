import pandas as pd
import re
import numpy as np

# builds a regex basing on the string
def string_to_regex(string):
    help_str = r''
    for i in string:
        for j in i:
            num = ord(j)
            if (num > 64 and num < 91) or (num > 96 and num < 123):
                help_str += j
            else:
                help_str += r'[\-,\s*]\w+[\-,\s*]|[\-,\s*]'
    help_str = re.compile(fr'{help_str}', re.IGNORECASE)
    return help_str

# class responsible for file analysis
# and comparing words in file with dictionary
class Detection():
    # there is a list of dictionaries you need several of them
    def __init__(self, dictPaths: list):
        self.__mainDict = pd.read_csv(dictPaths[0], header = None)
        column_names = ['word', 'definition']
        self.__mainDict.columns = column_names
        for i in range(1, len(dictPaths)):
            help_one = pd.read_csv(dictPaths[i], header = None)
            help_one.columns = column_names
            self.__mainDict = pd.concat([self.__mainDict, help_one], ignore_index=True)

    # adds regex column manually
    def add_re(self):
        if 'regex' in self.__mainDict.columns:
            return 'You have already added regex column'
        else:
            self.__mainDict['regex'] = self.__mainDict['word'].apply(string_to_regex)
        
    # deletes regex column manually
    def del_re(self):
        if 'regex' not in self.__mainDict.columns:
            return 'Regex already don\'t exist'
        self.__mainDict.drop(labels=['regex'], inplace=True)

    # Function which is responsible for filtering dictionary
    # We do not want to have useless words in dictionry
    def filtering(self, document):
        self.__mainDict['is in txt?'] = np.nan
        with open(document, 'r') as file:
            sentence = ''
            # to avoid too big strings it is needed
            # to read file sign by sign
            while True:
                sign = file.read(1)
                if sign == '.':
                    for i in self.__mainDict.index.to_list():
                        if self.__mainDict['is in txt?'].at[i] == 1:
                            continue
                        to_re = self.__mainDict['regex'].at[i]
                        is_in_txt = re.search(to_re, sentence)
                        if is_in_txt:
                            self.__mainDict['is in txt?'].at[i] = 1
                    sentence = ''
                elif not sign:
                    break
                else:
                    sentence += sign
        self.__mainDict.dropna(inplace = True)

    # is just showing the current state of data frame
    def show(self):
        print(self.__mainDict)

to_det = Detection(['words.csv'])
to_det.add_re()
to_det.filtering('list.txt')
to_det.show()
