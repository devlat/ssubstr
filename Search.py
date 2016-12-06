# -*- coding: utf-8 -*-
import os, re, time

class Search:
    DIRECTORY_SEPARATOR = '/'

    def __init__(self, rootDir, filesExtension = None):
        self.rootCatalogPath = rootDir
        self.filesExtension = filesExtension

    def scan(self, path = '', absPath = ''):
        if (not os.path.exists(self.rootCatalogPath)):
            raise Exception("Directory is not exists.")

        if (not absPath):
            absolutePath = self.rootCatalogPath + self.DIRECTORY_SEPARATOR + path
        else:
            absolutePath = absPath + path + self.DIRECTORY_SEPARATOR
        for item in os.listdir(absolutePath):
            if (os.path.isdir(absolutePath + item)):
                print absolutePath + item
                # recursive call
                self.scan(item, absolutePath)
            elif (os.path.isfile(absolutePath + item)):
                #file = open(absolutePath + item, 'r')
                print absolutePath + item



