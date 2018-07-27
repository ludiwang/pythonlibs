class Menu:
    def __init__(self, menuEntry: list):
        self.menuList = []
        self.menuList.append(menuEntry)
        self.curCmd = ""
        self.lastMenuCmd = ""
        self.menuNameHist = []
        self.menuNameHist.append(menuEntry[0])

    def levelUp(self):
        if len(self.menuNameHist) == 1:
            print("Already at Top level.")
            self.showMenu()
        curLevel = self.getMenuEntry(self.menuNameHist[-1])[2]
        while int(self.getMenuEntry(self.menuNameHist[-1])[2]) >= int(curLevel):
            self.menuNameHist.pop()
        self.showMenu()

    def getChoice(self):
        return self.curCmd

    def addMenuEntry(self, menuEntry: list):
        self.menuList.append(menuEntry)

    def getMenuEntry(self, name):
        menuEntry = []
        for entry in self.menuList:
            if entry[0] == name:
                menuEntry = entry
        if len(menuEntry) == 0:
            print("Error, menu item {} not found.".format(name))
            exit()
        return menuEntry

    def showMenuEntry(self, name):
        menuEntry = self.getMenuEntry(name)
        print("{}{}{}".format(30*'=', menuEntry[1], 30*'='))
        for ind, val in enumerate(menuEntry[3]):
            # print("{}.  {} {}".format(ind+1 , val[:val.find(":")], val[val.find(":")+1:]))
            print("{}.  {}".format(ind+1, val[:val.find(":")]))
        print("{}{}{}".format(30*'=', len(menuEntry[1])*'=', 30*'='))
        return menuEntry

    def showMenu(self):
        self.runMenuEntry(self.menuNameHist[-1])

    def runMenuEntry(self, name):
        menuEntry = self.showMenuEntry(name)
        choice = input("Please choose option: ").strip()
        for ind, val in enumerate(menuEntry[3]):
            if ind + 1 == int(choice):
                cmd = val[val.find(":")+1:]
                if cmd[cmd.find(":")+1:] == "menu":
                    menuItemName = cmd[:cmd.find(":")]
                    if menuItemName == "exit":
                        exit()
                    if menuItemName == "up":
                        self.levelUp()
                    else:
                        self.menuNameHist.append(menuItemName)
                        self.runMenuEntry(menuItemName)
                else:
                    self.curCmd = cmd[:cmd.find(":")]
                break
