from sys import maxsize


_minIntValue: int = -maxsize
_maxIntValue: int = maxsize
_minFloatValue: float = -float("inf")
_maxFloatValue: float = float("inf")


def sanitizeInputInt(msg: str = "", vmin: int = _minIntValue, vmax: int = _maxIntValue) -> int:
    while True:
        try:
            Num = int(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be an integer.")

def sanitizeInputFloat(msg: str = "", vmin: float = _minFloatValue, vmax: float = _maxFloatValue) -> float:
    while True:
        try:
            Num = float(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be a float.")

def makeLine(NStr: int | str = 10, symbol: str = "*") -> str:
    if isinstance(NStr, int):
        print(symbol * NStr)
        return f"{symbol * NStr}"
    elif isinstance(NStr, str):
        print(symbol * len(NStr))
        return f"{symbol * len(NStr)}"

def processablestr(stra: str, toremove: tuple[str, ...] = (" ", ".", ",", "'", '"')) -> list:
    stra = stra.upper()
    # delete all characters in str that are in toremove
    for remove in toremove:
        strab = stra.replace(remove, " ")
    # make the final standarized text
    strab = stra.split()
    return strab

def processlisttostr(processablestrl: list[str]) -> str:
    if not isinstance(processablestrl, list):
        raise typeerror
    # make a full string line made of words in the processablestrl list
    fullstr = " ".join(
        word.capitalize() if i == 0 else word.lower() for i, word in enumerate(processablestrl)
    )
    # return that striing
    return fullstr

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

    processableteststr = processablestr(teststr)
    print(processableteststr)
    for each in processableteststr:
        print(each)
    print(processlisttostr(processableteststr))
    

if __name__ == "__main__":
    teststr = "this is a test  for long text. this will be an example of sanitized  string or as i want to called it a text in a 'standardized' form that you can use for any processing you want to make to the text or string."
    main(teststr)
