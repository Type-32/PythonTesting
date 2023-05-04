# Morse Code Translator
import os
import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def ClearScreen():
    # if the Operating System is Windows
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
while True:
    print("Enter your message: ", end='')
    message = input()
    flag: bool = False
    if len(message) <= 0:
        pass
    if message.lower() == "morsecode action --exit":
        ClearScreen()
        break
    elif message.lower() == "morsecode action --clear":
        ClearScreen()
        pass
    if message.__contains__(".") and message.__contains__("-"):
        flag = True
    else:
        flag = False
    if flag:
        message = message.split(" ")
        for letter in message:
            if letter not in MORSE_CODE_DICT.values():
                #print("!--Invalid Character--!")
                continue
            print(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)], end='')
        print()
    else:
        message = message.upper()
        for letter in message:
            if letter not in MORSE_CODE_DICT.keys():
                #print("!--Invalid Character--!")
                continue
            print(MORSE_CODE_DICT[letter], end=' ')
        print()
