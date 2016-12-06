# -*- coding: utf-8 -*-
import os, re, time;

timeAmount = time.time();

DIRECTORY_SEPARATOR = '/';

rootCatalogPath = "C:/puphpet";
absolutePath = '';

catalog = os.listdir(rootCatalogPath);

def listDir(path = '', absPath = ''):
    if (not absPath):
        absolutePath = rootCatalogPath + DIRECTORY_SEPARATOR + path;
    else:
        absolutePath = absPath + path + DIRECTORY_SEPARATOR;
    for item in os.listdir(absolutePath):
        if (os.path.isdir(absolutePath + item)):
            # print absolutePath + item;
            # recursive call
            listDir(item, absolutePath);
        elif (os.path.isfile(absolutePath + item)):
            file = open(absolutePath + item, 'r');

listDir();

