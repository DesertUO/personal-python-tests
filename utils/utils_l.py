def sanatizeInputInt(msg: str = "", vmin: int = -9999999999999, vmax: int = 9999999999999) -> int:
    while True:
        try:
            Num = int(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be an integer.")

def sanatizeInputFloat(msg: str = "", vmin: float = -9999999999999, vmax: float = 9999999999999) -> float:
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

def processlisttostr(processablestrl: list[str]):
    if not isinstance(processablestrl, list):
        raise typeerror
    # make a full string line made of words in the processablestrl list
    fullstr = " ".join(
        word.capitalize() if i == 0 else word.lower() for i, word in enumerate(processablestrl)
    )
    # return that striing
    return fullstr

def main(teststr) -> None:
    processableteststr = processablestr(teststr)
    print(processableteststr)
    for each in processableteststr:
        print(each)
    print(processlisttostr(processableteststr))
    

if __name__ == "__main__":
    teststr = "this is a test  for long text. this will be an example of sanatized  string or as i want to called it a text in a 'standardized' form that you can use for any processing you want to make to the text or string."
    main(teststr)
