import os
import json
import string
import sys

import keyboard
import numpy

class Diagram:
    def __init__(self, circuitmap, cplot, iplot):
        self.circuitmap = circuitmap
        self.cplot = cplot
        self.iplot = iplot
    def WriteToFile(self, fileName):
        with open(fileName, 'w') as file:
            file.write(json.dumps(self.circuitmap))
            file.write(json.dumps(self.cplot))
            file.write(json.dumps(self.iplot))
    def ReadFromFile(self, directory):
        with open(directory, 'r') as file:
            self.circuitmap = json.loads(file.readline())
            self.cplot = json.loads(file.readline())
            self.iplot = json.loads(file.readline())
    def PlaceObject(self, x, y, index):
        self.iplot[y][x] = index
        self.cplot[y][x] = True if not index == 8 or index == 0 else False
        self.circuitmap[y][x] = GetObjectIcon(index)
    def PrintSelf(self, x, y):
        for i in range(len(self.circuitmap)):
            for j in range(len(self.circuitmap[i])):
                print(((" " + self.circuitmap[i][j]) if not (x == j and y == i) else ("{" + self.circuitmap[i][j])) if not (x == j-1 and y == i) else ("}" + self.circuitmap[i][j]), end='')
            print(" ")
                #print(" " + self.circuitmap[i][j] if not (x == j and y == i) else "{" + self.circuitmap[i][j]+ "}", end=('' if not j >= len(self.circuitmap[i])-1 else '\n'))
class Menu:
    def __init__(self, mainContent, altContent, endLine: bool = True):
        self.mainContent = mainContent
        self.altContent = altContent
        self.endLine = endLine

    def PrintSelf(self, useAlternative: bool):
        if useAlternative:
            for i in range(len(self.altContent)):
                print(self.altContent[i], end=('' if not self.endLine and i == len(self.altContent)-1 else '\n'))
        else:
            for i in range(len(self.mainContent)):
                print(self.mainContent[i], end=('' if not self.endLine and i == len(self.mainContent)-1 else '\n'))


menus = (
    Menu(
        [
            "===> Simple Circuit Builder <===",
            "",
            "1 - Create New...",
            "2 - Open New...",
            "Q - Quit Program"
        ],
        [
            "===> Simple Circuit Builder <===",
            "!--Invalid Key--!",
            "",
            "1 - Create New...",
            "2 - Open New...",
            "Q - Quit Program"
        ]
    ),
    Menu(
        [
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
        ], False
    ),
    Menu(
        [
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
        ], False
    ),
    Menu(["Cleared Caches."], []),
    Menu(["===> Diagram Editor <===","Control + Q - Quit\nW,A,S,D - Up,Left,Down,Right\nE - Place Object\nR - Rotate Object"], []),
    Menu([
        "===> Select Tool <===",
        "",
        "1 - Wire",
        "2 - Resistor",
        "3 - Capacitor",
        "4 - Inductor",
        "5 - Voltage Source",
        "6 - Current Source",
        "7 - Ground",
        "8 - Delete",
        "Q - Quit Mode"
    ], [
        "===> Select Tool <===",
        "!--Invalid Key--!",
        "",
        "1 - Wire",
        "2 - Resistor",
        "3 - Capacitor",
        "4 - Inductor",
        "5 - Voltage Source",
        "6 - Current Source",
        "7 - Ground",
        "8 - Delete",
        "Q - Quit Mode"
    ]),
    Menu(["===> Save File <===","Save file? (Y/N): "],["===> Save File <===","!--Invalid Key--!","","Save file? (Y/N): "], False)
)
emptyDiagramMap = numpy.full((20,20),'.')
emptyCPlot = numpy.full((20,20), False)
emptyIPlot = numpy.full((20,20),-1)
tempDiag = Diagram(emptyDiagramMap, emptyCPlot, emptyIPlot)

def ClearScreen():
    # if the Operating System is Windows
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


menuInput: string = "?"
lastMenuIndex = -1
currentMenuIndex = 0
currentSelectedObject = 0
brushDown = False
tempX = 0
tempY = 0
def GetObjectKeyword(index):
    if index == 1:
        return "Wire"
    elif index == 2:
        return "Resistor"
    elif index == 3:
        return "Capacitor"
    elif index == 4:
        return "Inductor"
    elif index == 5:
        return "Voltage Source"
    elif index == 6:
        return "Current Source"
    elif index == 7:
        return "Ground"
    elif index == 8:
        return "Delete"
    else:
        return "None"
def GetObjectIcon(index):
    if index == 1:
        return "+"
    elif index == 2:
        return "R"
    elif index == 3:
        return "C"
    elif index == 4:
        return "D"
    elif index == 5:
        return "B"
    elif index == 6:
        return "I"
    elif index == 7:
        return "G"
    elif index == 8:
        return "."
    else:
        return "."

while 0 == len(menuInput) or menuInput[0].lower() != 'q':
    ClearScreen()
    menus[currentMenuIndex].PrintSelf(False if not lastMenuIndex == currentMenuIndex else True)
    if currentMenuIndex == 0: #Main Menu
        lastMenuIndex = currentMenuIndex
        menuInput = input()
        if menuInput[0] == '1':
            currentMenuIndex = 1
        elif menuInput[0] == '2':
            currentMenuIndex = 2
        elif menuInput[0].lower() == 'q':
            ClearScreen()
            break
        else:
            menus[currentMenuIndex].PrintSelf(True)
    elif currentMenuIndex == 1: #New File Menu
        lastMenuIndex = currentMenuIndex
        menuInput = input()
        if menuInput.lower() == "q":
            currentMenuIndex = 0
        else:
            if menuInput.__contains__("*") or menuInput.__contains__("!") or menuInput.__contains__("&") or menuInput.__contains__("#") or menuInput.__contains__(".json"):
                menus[currentMenuIndex].PrintSelf(True)
            else:
                currentMenuIndex = 4
                tempDiag = Diagram(emptyDiagramMap, emptyCPlot, emptyIPlot)
    elif currentMenuIndex == 4: #Editor Menu
        lastMenuIndex = currentMenuIndex
        tempDiag.PrintSelf(tempX,tempY)
        print("Selector Position: ({},{})".format(tempX,tempY))
        print("Current Selected Object: {}".format(GetObjectKeyword(currentSelectedObject)))
        print("Brush Down: {}".format(brushDown))
        menuInput = input()
        if menuInput.lower() == "quit":
            currentMenuIndex = 0
            continue
        for i in range(len(menuInput)):
            if menuInput.lower() == "save":
                currentMenuIndex = 6
            elif menuInput[i].lower() == 'w':
                tempY -= 1 if not tempY <= 0 else 0
            elif menuInput[i].lower() == 'a':
                tempX -= 1 if not tempX <= 0 else 0
            elif menuInput[i].lower() == 's':
                tempY += 1 if not tempY >= len(tempDiag.circuitmap)-1 else 0
            elif menuInput[i].lower() == 'd':
                tempX += 1 if not tempX >= len(tempDiag.circuitmap[tempY])-1 else 0
            elif menuInput[i].lower() == 't':
                currentMenuIndex = 5
                break
            elif menuInput[i].lower() == 'e':
                brushDown = True if not brushDown else False
            if(brushDown == True): tempDiag.PlaceObject(tempX,tempY,currentSelectedObject)
    elif currentMenuIndex == 5: #Tool Selection Menu
        lastMenuIndex = currentMenuIndex
        menuInput = input()
        if len(menuInput) == 0:
            continue
        if menuInput.lower() == "quit":
            currentMenuIndex = 4
        elif ('1' <= menuInput[0] <= '8') and int(menuInput[0]) <= 8:
            currentSelectedObject = int(menuInput[0])
            currentMenuIndex = 4
    elif currentMenuIndex == 6: #Save Menu
        lastMenuIndex = currentMenuIndex
        menuInput = input()
        if menuInput[0].lower() == 'y':
            currentMenuIndex = 4
        elif menuInput[0].lower() == 'n':
            currentMenuIndex = 4
