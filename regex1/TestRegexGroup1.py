'''
Created on Apr 10, 2019

@author: PIKU
'''
import re


class TestRegexGroup1(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def printAllGroups(self):
        regexPattern = r"^(\d+)[^\d]+(\d+)[^\d]+(\d+)[^\d]+(\d+)[^\d]+$"
        text = "1123-xxx-abcd-45-tsvt-35-pwrst-99-xql"
        matcher = re.compile(regexPattern, flags=re.IGNORECASE)
        matchValue = matcher.match(text);
        if matchValue:
            print("First group : ", matchValue.group(1))
            print("Second group : ", matchValue.group(2))
            print("Third group : ", matchValue.group(3))
            print("Fourth group : ", matchValue.group(4))

    def findAllGroups(self):
        pattern = r"(\d+)";
        string = "1123-abcdefgh-25-45-A-lazy dog"
        matches = re.findall(pattern, string, flags=0)
        for match in matches:
            print("Match : ", match)

    def checkRepetitions(self):
        regexPattern = r"(ruby)+";
        text = "ruby python Ruby java rubytest Ruby perarls"
        matcher = re.compile(regexPattern, flags=re.I)
        matchValue = matcher.match(text)
        if matchValue:
            print("Found match : ", matchValue.group(1))

        matches = matcher.findall(text)
        print("Total occurances : ", len(matches))
        print("Total occurances : ", matches.__len__())
        for match in matches:
            print("Exact match : ", match)

    def searchAndPrint(self):
        regexPattern = r"^The.*Spain$"
        text = "The rain in Spain"
        matcher = re.compile(regexPattern, flags=re.IGNORECASE)
        matchValue = matcher.search(text)
        print("Match Value : ", matchValue.group())


if __name__ == '__main__':
    test = TestRegexGroup1()
    test.findAllGroups()
    test.printAllGroups()
    test.checkRepetitions()
    test.searchAndPrint()
