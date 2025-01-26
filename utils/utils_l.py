from enum import Enum
from sys import maxsize
import os

MIN_INT: int = -maxsize
MAX_INT: int = maxsize
MIN_FLOAT: float = -float("inf")
MAX_FLOAT: float = float("inf")


def sanitizeInputInt(msg: str = "", vmin: int = MIN_INT, vmax: int = MAX_INT, errorMsg: str = "ERROR. Input must be an integer", errorOutOfRange: str = "default", exitKey: str = "q", useExitKey: bool = True) -> int:
    if errorOutOfRange == "default":
        errorOutOfRange = f"Please enter a number between {vmin} and {vmax}."
    while True:
        userInput = input(msg)
        if userInput == exitKey and useExitKey == True:
            print("Exiting input...")
            return 0
        try:
            Num = int(userInput)
            if Num < vmin or Num > vmax:
                print(errorOutOfRange)
            else:
                return Num
        except ValueError:
            print(errorMsg)

def sanitizeInputFloat(msg: str = "", vmin: float = MIN_FLOAT, vmax: float = MAX_FLOAT, errorMsg: str = "ERROR. Input must be a float.", exitKey: str = "q", useExitKey: bool = True) -> float:
    userInput = input(msg)
    if userInput == exitKey and useExitKey == True:
        print("Exiting input...")
        return 0
    while True:
        try:
            Num = float(userInput)
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print(errorMsg)

def makeLine(NStr: int | str = 10, symbol: str = "*", printLine: bool = True) -> str:
    line = symbol * (NStr if isinstance(NStr, int) else len(NStr))

    if printLine == True:
        print(line)
    return f"{line}"

def processableStr(strN: str, toRemove: tuple[str, ...] = (" ", ".", ",", "'", '"'), ignoreCase: bool = True) -> list[str]:
    if ignoreCase == True:
        strN = strN.upper()
    # delete all characters in str that are in toremove
    for remove in toRemove:
        strab = strN.replace(remove, " ")
    # make the final standarized text
    strNB = strN.split()
    return strNB

class CapMode(Enum):
    CAP_ALL = 1
    CAP_FIRST = 2
    CAP_NONE = 3

def processlistToStr(processableStrL: list[str], capMode: CapMode = CapMode.CAP_FIRST) -> str:
    if not isinstance(processableStrL, list):
        raise TypeError
    # make a full string line made of words in the processablestrl list
    match capMode:
        case capMode.CAP_ALL:
            fullStr = " ".join(word.capitalize() for word in processableStrL)
        case capMode.CAP_FIRST:
            fullStr = " ".join(word.capitalize() if i == 0 else word.lower() for i, word in enumerate(processableStrL))
        case capMode.CAP_NONE:
            fullStr = " ".join(word.lower() for word in processableStrL)

    # return that striing
    return fullStr

# New----------------------------->

# Files and directories utils
def readFile(filePath: str) -> str:
    try:
        with open(filePath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found on {filePath}.")
        return ""

def writeFile(filePath: str, content: str) -> None:
    with open(filePath, "w") as file:
        file.write(content)

def fileExists(filePath: str) -> bool:
    return os.path.exists(filePath)

def makeDirectory(directoryPath) -> None:
    os.makedirs(directoryPath, exist_ok=True)

def getFileExt(filePath: str) -> str:
    _, ext = os.path.splitext(filePath)
    return ext

# Trying to do a test for this module

def main(teststr) -> None:
    def testsanitizeInt(msg: str = "TEST", _vmin: int = 25, _vmax: int = 96):
        _msg = msg
        _msgVmin = msg + f" vmin={_vmin}"
        _msgVmax = msg + f" vmax={_vmax}"
        _msgVminVmax = msg + f" vmin={_vmin} vmax={_vmax}"

        test1 = sanitizeInputInt(msg + ": ")
        test2 = sanitizeInputInt(_msgVmin + ": ", _vmin)
        test3 = sanitizeInputInt(_msgVmax + ": ", vmax=_vmax)
        test4 = sanitizeInputInt(_msgVminVmax + ": ", _vmin, _vmax)
        print(test1, test2, test3, test4)

    def testsanitizeFloat(msg: str = "TEST", _vmin: int = 25, _vmax: int = 96):
        _msg = msg
        _msgVmin = msg + f" vmin={_vmin}"
        _msgVmax = msg + f" vmax={_vmax}"
        _msgVminVmax = msg + f" vmin={_vmin} vmax={_vmax}"

        test1 = sanitizeInputFloat(_msg + ": ")
        test2 = sanitizeInputFloat(_msgVmin + ": ", _vmin)
        test3 = sanitizeInputFloat(_msgVmax + ": ", vmax=_vmax)
        test4 = sanitizeInputFloat(_msgVminVmax + ": ", _vmin, _vmax)
        print(test1, test2, test3, test4)

    testsanitizeInt()
    testsanitizeFloat()

    processableteststr = processableStr(teststr)
    print(processableteststr)
    for each in processableteststr:
        print(each)
    print(processlistToStr(processableteststr)) 

if __name__ == "__main__":
    teststr = "this is a test  for long text. this will be an example of sanitized  string or as i want to called it a text in a 'standardized' form that you can use for any processing you want to make to the text or string."
    main(teststr)
