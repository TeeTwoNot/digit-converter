"""A simple converter that converts binary, decimal and hexadecimal values, as well as characters in ASCII to their value in decimal and vice versa!"""

import os

#DEV NOTES:
#ord(insert char, convert to dec)
#chr(insert dec, convert to char)


def inputBin():
    try:
        num = int(input("Enter a binary number: "), base=2)
        print(f"\nBinary (UserInput): {bin(num)}\nDecimal: {int(num)}\nHexadecimal: {hex(num)}")
        reRun()
    except Exception as e:
        print(e)
        print("\nMake sure the number you input is BINARY (Base 2)\n")
        inputBin()


def inputDec():
    try:
        num = int(input("Enter a decimal number: "), base=10)
        print(f"\nBinary: {bin(num)}\nDecimal (UserInput): {int(num)}\nHexadecimal: {hex(num)}")
        reRun()
    except Exception as e:
        print(e)
        print("\nMake sure the number you input is DECIMAL (Base 10)\n")
        inputDec()


def inputHex():
    try:
        num = int(input("Enter a hexadecimal number: "), base=16)
        print(f"\nBinary: {bin(num)}\nDecimal: {int(num)}\nHexadecimal (UserInput): {hex(num)}")
        reRun()
    except Exception as e:
        print(e)
        print("\nMake sure the number you input is HEXADECIMAL (Base 16)\n")
        inputHex()


def asciiChar():
    try:
        char = str(input("Enter a character (ASCII): "))
        binNum = bin(ord(char))
        print(f"\nCharacter (UserInput): {char}\nDecimal: {ord(char)}\nBinary: {binNum}")
        reRun()
    except Exception as e:
        print(e)
        print("\nMake sure the character you input is an ASCII character.\n")
        asciiChar()


def asciiDec():
    try:
        num = int(input("Enter a decimal number: "), base=10)
        print(f"\nDecimal (UserInput): {num}\nCharacter: {chr(num)}\nBinary: {bin(num)}")
        reRun()
    except Exception as e:
        print(e)
        print("\nMake sure the number you input is DECIMAL (Base 10)\n")
        asciiDec()


def reRun():
    rerun = str(input("\nRerun program (y/n)?\n"))
    if rerun.lower() == "y":
        Mode()
    elif rerun.lower() == "n":
        print("Exiting program...")
        exit()
    else:
        print("Exiting program...")
        exit()


def Mode():
    mode = str(input("Choose mode (bin, dec, hex, ascii, table): "))

    if mode.lower() == "bin":
        inputBin()

    elif mode.lower() == "ascii":
        def subMode():
            submode=str(input("Choose submode (char, dec): "))
            if submode.lower() == "char":
                asciiChar()
            elif submode.lower() == "dec":
                asciiDec()
            else:
                print("Invalid submode! Try again!\n")
                subMode()
        subMode()

    elif mode.lower() == "hex":
        inputHex()

    elif mode.lower() == "dec":
        inputDec()

    elif mode.lower() == "table":
        os.startfile('DATACHART.pdf')
        print("\nOpening ASCII data chart...\n")
        reRun()

    else:
        print("Invalid mode! Try again!\n")
        Mode()


Mode()
