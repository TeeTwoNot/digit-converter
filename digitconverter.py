import os


def binNum():
    num = int(input("Enter a binary number: "), base=2)
    print(f"\nBinary (UserInput): {bin(num)}\nDecimal: {int(num)}\nHexadecimal: {hex(num)}")
    reRun()


def decNum():
    num = int(input("Enter a decimal number: "), base=10)
    print(f"\nBinary: {bin(num)}\nDecimal (UserInput): {int(num)}\nHexadecimal: {hex(num)}")
    reRun()


def hexNum():
    num = int(input("Enter a hexadecimal number: "), base=16)
    print(f"\nBinary: {bin(num)}\nDecimal: {int(num)}\nHexadecimal (UserInput): {hex(num)}")
    reRun()


def reRun():
    rerun = str(input("\nRerun program (y/n)?\n"))
    if rerun.lower() == "y":
        Mode()
    elif rerun.lower() == "n":
        print("Exiting program...")
    else:
        print("Exiting program...")


def Mode():
    mode = str(input("Choose mode (bin, dec, hex, chart): "))

    if mode.lower() == "bin":
        binNum()
    elif mode.lower() == "dec":
        decNum()
    elif mode.lower() == "hex":
        hexNum()
    elif mode.lower() == "chart":
        os.startfile('DATACHART.pdf')
        print("Opening ASCII data chart...")
        reRun()
    else:
        print("Invalid mode! Try again!\n")
        Mode()


Mode()