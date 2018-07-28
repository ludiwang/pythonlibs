class Menu:
    def __init__(self, menu_entry: list):
        self.menu_list = []
        self.menu_list.append(menu_entry)
        self.cur_cmd = ""
        self.menu_name_hist = []
        self.menu_name_hist.append(menu_entry[0])

    def level_up(self):
        if len(self.menu_name_hist) == 1:
            print("Already at Top level.")
            self.show_menu()
        curLevel = self.get_menu_entry(self.menu_name_hist[-1])[2]
        while int(self.get_menu_entry(self.menu_name_hist[-1])[2]) >= int(curLevel):
            self.menu_name_hist.pop()
        self.show_menu()

    def get_choice(self):
        return self.cur_cmd

    def add_menu_entry(self, menu_entry: list):
        self.menu_list.append(menu_entry)

    def get_menu_entry(self, name):
        menu_entry = []
        for entry in self.menu_list:
            if entry[0] == name:
                menu_entry = entry
        if len(menu_entry) == 0:
            print("Error, menu item {} not found.".format(name))
            exit()
        return menu_entry

    def show_menu_entry(self, name):
        menu_entry = self.get_menu_entry(name)
        print("{}{}{}".format(30*'=', menu_entry[1], 30*'='))
        for ind, val in enumerate(menu_entry[3]):
            # print("{}.  {} {}".format(ind+1 , val[:val.find(":")], val[val.find(":")+1:]))
            print("{}.  {}".format(ind+1, val[:val.find(":")]))
        print("{}{}{}".format(30*'=', len(menu_entry[1])*'=', 30*'='))
        return menu_entry

    def show_menu(self):
        self.run_menu_entry(self.menu_name_hist[-1])

    def run_menu_entry(self, name):
        menu_entry = self.show_menu_entry(name)
        choice = input("Please choose option: ").strip()
        for ind, val in enumerate(menu_entry[3]):
            if ind + 1 == int(choice):
                cmd = val[val.find(":")+1:]
                if cmd[cmd.find(":")+1:] == "menu":
                    menu_item_name = cmd[:cmd.find(":")]
                    if menu_item_name == "exit":
                        exit()
                    if menu_item_name == "up":
                        self.level_up()
                    else:
                        self.menu_name_hist.append(menu_item_name)
                        self.run_menu_entry(menu_item_name)
                else:
                    self.cur_cmd = cmd[:cmd.find(":")]
                break
