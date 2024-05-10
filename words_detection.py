import pandas as pd
import regex as re

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
    
    def __string_to_regex(string):
        return

    # adds regex column manually
    def add_re(self):
        if 'regex' in self.__mainDict.columns:
            return 'You have already added regex column'
        
    # deletes regex column manually
    def del_re(self):
        if 'regex' not in self.__mainDict.columns:
            return 'Regex already don\'t exist'
        self.__mainDict.drop(labels=['regex'], inplace=True)

### TO DO
# ogolnie wyrazenie nie bedzie szlo dalej niz zdanie
# trzeba wiec dodac kolumne "regex" do self.__mainDict
# i do srodka wyrazen zawierajacych znaki biale wprowadzic
# regex przyjmujacy dowolne znaki oprocz kropki kiedy jest spacja
# lub tylko myslnik i litery (opcjonalnie poszczegolne znaki)
# o ile "biala przestrzen" zaczyna i konczy sie myslnikiem
