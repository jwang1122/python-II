"""
bind operation on functional programing
"""
from pymonad import *

def openVSCode(x):
    return Just("\n" + x+" Open VSCode application.")

def openTerminal(x):
    return Just(x+"\nTerminal > New Terminal.")

def enterSourceCode(x):
    return Just(x + "\nEnter python source code in editor window.")

def runCode(x):
    return Just(x + "\nRight click > Run Python file in terminal.")

def checkResult(x):
    return Just(x + "\nCheck output result.")

x= Just("John ") >> openVSCode >> openTerminal >> enterSourceCode >> runCode >> checkResult
print("11:",x)