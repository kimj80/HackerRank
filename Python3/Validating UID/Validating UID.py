# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

numOfInputs = int(input())

for inputs in range(numOfInputs):
    userInput = input()
    passOrFail = "Valid"
    digits = sum(c.isdigit() for c in userInput)
    capital = sum(c.isupper() for c in userInput)
    checkAlNum = userInput.isalnum()
    uidLength = len(userInput)

    if capital < 2 or uidLength != 10 or checkAlNum is False or digits < 3:
        passOrFail = "Invalid"
    else:
        for letter in userInput:
            if userInput.count(letter) > 1:
                passOrFail = "Invalid"

    sys.stdout.write(passOrFail + "\n")