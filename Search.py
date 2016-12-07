# -*- coding: utf-8 -*-
import os, re, time

class Search:
    DIRECTORY_SEPARATOR = '/'

    def __init__(self, rootDir, searchPattern, filesExtension = None):
        self.rootCatalogPath = rootDir # Absolute path to directory to parse
        self.filesExtension = filesExtension # Specified files(if typed)
        self.pattern = searchPattern # Key word's regex pattern

    def scan(self, path = '', absPath = ''):
        if (not os.path.exists(self.rootCatalogPath)):
            raise Exception("Directory is not exists.")

        if (not absPath):
            absolutePath = self.rootCatalogPath + self.DIRECTORY_SEPARATOR + path
        else:
            absolutePath = absPath + path + self.DIRECTORY_SEPARATOR
        for item in os.listdir(absolutePath):
            if (os.path.isdir(absolutePath + item)):
                # recursive call
                self.scan(item, absolutePath)
            elif (os.path.isfile(absolutePath + item)):
                if (self.filesExtension):
                    if (not re.search('\.%s$' % (self.filesExtension), item)):
                        return 0;
                self.__parse_file(absolutePath + item)

    def __parse_file(self, pathToFile):
        f = open(pathToFile)
        if (re.search(self.pattern, f.read())):
            print pathToFile;
        return 1;



