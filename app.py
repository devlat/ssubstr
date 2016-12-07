# -*- coding: utf-8 -*-
import sys
from Search import Search


"""
=========
БЫДЛОКОД.
Парсим аргументы вызова для дальнейшей передачи в конструктор
=========
"""
"""
args = sys.argv[1:]
n = 0
keysDict = {}
while (n + 1 < len(args)):
    keysDict[args[n]] = args[n + 1]
    n += 2
print keysDict"""

searchEngine = Search('C:/localdev/julia/frontend', 'utm', 'php')

searchEngine.scan()