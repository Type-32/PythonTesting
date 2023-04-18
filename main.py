import os
import json
import string
import sys

class Menu:
    def __init__(self, mainContent, altContent):
        self.mainContent = mainContent
        self.altContent = altContent
        pass
    def PrintSelf(self, useAlternative: bool):
        if useAlternative:
            for line in self.altContent:
                print(line)
        else:
            for line in self.mainContent:
                print(line)
        pass

menus = (
    Menu([
        "===> Simple Circuit Builder <===",
        "",
        "1 - Create New...",
        "2 - Open New...",
        "Q - Quit Program"
    ],[
        "===> Simple Circuit Builder <===",
        "!--Invalid Key--!",
        "",
        "1 - Create New...",
        "2 - Open New...",
        "Q - Quit Program"
    ]),
    Menu([
        "===> Create New <===",
        "",
        "Q - Quit Mode",
        "Create New File with Name: "
    ],
    [
        "===> Create New <===",
        "!--Invalid Name Convention--!",
        "",
        "Q - Quit Mode",
        "Create New File with Name: "
    ]),
    Menu([
        "===> Open File <===",
        "",
        "Q - Quit Mode",
        "Open File with Directory: "
    ],
    [
        "===> Open File <===",
        "!--Invalid Name Convention--!",
        "",
        "Q - Quit Mode",
        "Open File with Directory: "
    ]),
    Menu(["Cleared Caches."],[])
)

def ClearScreen():
    # if the Operating System is Windows
    if sys.platform == "win32":
        os.system("cls")
    # if the Operating System is Linux
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("clear")
    # if the Operating System is macOS
    if sys.platform == "darwin":
        os.system("clear")

menuInput: string = "?"
while menuInput[0] != 'Q':
    ClearScreen()
    menus[0].PrintSelf(False)
    menuInput = input()
    if menuInput[0] == '1':
        menus[1].PrintSelf(False)
    elif menuInput[0] == '2':
        menus[2].PrintSelf(False)
    elif menuInput[0] == 'Q':
        ClearScreen()
        menus[3].PrintSelf(False)
        break
    else:
        menus[0].PrintSelf(True)
    menuInput = input()