import pandas as pd
import re
import numpy as np

# builds a regex basing on the string
def string_to_regex(string):
    help_str = r''
    for i in string:
        for j in i:
            print(j)
            num = ord(j)
            if (num > 64 and num < 91) or (num > 96 and num < 123):
                help_str += j
            else:
                help_str += r'([-," "]\w+[-," "]|[-," "])'
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

    # is adding NaN
    # NaN because it will be easy to get rid of it
    def __nan_add(self):
        return np.nan
    # Function which is responsible for filtering dictionary
    # We do not want to have useless words in dictionry
    def filtering(self):
        self.__mainDict['is in txt?'] = np.nan
    
    def show(self):
        print(self.__mainDict)

to_det = Detection(['words.csv'])
to_det.show()
to_det.add_re()
to_det.show()
to_det.filtering()
to_det.show()

### TO DO
# ogolnie wyrazenie nie bedzie szlo dalej niz zdanie
# trzeba wiec dodac kolumne "regex" do self.__mainDict
# i do srodka wyrazen zawierajacych znaki biale wprowadzic
# regex przyjmujacy dowolne znaki oprocz kropki kiedy jest spacja
# lub tylko myslnik i litery (opcjonalnie poszczegolne znaki)
# o ile "biala przestrzen" zaczyna i konczy sie myslnikiem
# warto jeszcze dodac kolumne sprawdzajaca czy slowo juz wystapilo w tekscie ktory idzie do sprawdzenia
# funkcja odpowiadajaca za ta kolumne powinna przerwac dzialanie przy pierwszym
# wykryciu zeby zaoszczedzic moc obliczeniowa. funkcja ta powinna brac jako test regexa,
# a dopiero jezeli go nie ma brac kolumne z wyrazeniem.
# to jednak dopiero na etapie sprawdzania. najpierw regex
