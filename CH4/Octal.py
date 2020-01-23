def printOctal():
    print("Octal          Decimal     Hex    Bin               Char")
    print("-------------------------------------------------------")
    for number in range(63,73):
        print("{0:>#5o}{0:>12}{0:>12x}{0:>12b}{0:>12c}".format(number))
printOctal()