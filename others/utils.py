def sanatizeInputInt(msg, vmin = -9999999999999, vmax = 9999999999999):
    while True:
        try:
            Num = int(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be an integer.")

def sanatizeInputFloat(msg, vmin = -9999999999999, vmax = 9999999999999):
    while True:
        try:
            Num = float(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be a float.")

def makeLine(NStr: int | str = 10, symbol: str = "*"):
    if isinstance(NStr, int):
        print(symbol * NStr)
        return f"{symbol * NStr}"
    elif isinstance(NStr, str):
        print(symbol * len(NStr))
        return f"{symbol * len(NStr)}"

def processableStr(Str: str, toRemove: tuple = (" ", ".", ",", "'", '"')):
    Str = Str.upper()
    # Delete all characters in toRemove
    for remove in toRemove:
        remove = str(remove)
        Str = Str.split(remove)
        TStr = ""
        for each in Str:
            TStr = TStr + " " + each
        Str = TStr
    # Make the final standarized text
    Str = Str.split()
    seen = []
    for i in Str:
        if i not in seen:
            seen.append(i)
    return seen

if __name__ == "__main__":
    TestStr = "This is a test  for long text. This will be an example of sanatized  string or as I want to called it a text in a 'STANDARIZIED' form that you can use for any processing you want to make to the text or string."
    print(processableStr(TestStr))
    for each in processableStr(TestStr):
        print(each)