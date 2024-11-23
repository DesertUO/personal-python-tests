def sanatizeInputInt(msg = "", vmin = -9999999999999, vmax = 9999999999999) -> int:
    while True:
        try:
            Num = int(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be an integer.")

def sanatizeInputFloat(msg = "", vmin = -9999999999999, vmax = 9999999999999) -> float:
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

def processableStr(Str: str, toRemove: tuple = (" ", ".", ",", "'", '"')) -> list:
    Str = Str.upper()
    # Delete all characters in Str that are in toRemove
    for remove in toRemove:
        remove = str(remove)
        Str = Str.split(remove)
        TStr = ""
        for each in Str:
            TStr = TStr + " " + each
        Str = TStr
    # Make the final standarized text
    Str = Str.split()
    return Str

def processListToStr(processableStrL: list):
    if not isinstance(processableStrL, list):
        raise TypeError
    # Make a full string line made of words in the processableStrL list
    fullStr = ""
    for word in processableStrL:
        if processableStrL.index(word) == 1:
            word = str(word).capitalize()
        fullStr = fullStr + str(word) + (" " if (processableStrL.index(word) == -1) else "")
    # Return that striing
    return fullStr
 
if __name__ == "__main__":
    TestStr = "This is a test  for long text. This will be an example of sanatized  string or as I want to called it a text in a 'STANDARIZIED' form that you can use for any processing you want to make to the text or string."
    print(processableStr(TestStr))
    for each in processableStr(TestStr):
        print(each)