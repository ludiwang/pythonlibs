from menu import Menu

def cmd1a():
    print("1a")

def cmd2a():
    print("2a")

def cmd1b():
    print("1b")

def cmd2b():
    print("2b")

menu1 = Menu(["main","Main menu",0,
          ["menu sub 1:sub1:menu",
           "menu sub 2:sub2:menu",
           "exit:exit:menu"]])

menu1.add_menu_entry(["sub1", "Sub menu 1", 1,
                     ["run cmd1a:cmd1a():cmd",
                      "run cmd1b:cmd1b():cmd",
                      "up:up:menu",
                      "exit:exit:menu"]])

menu1.add_menu_entry(["sub2", "Sub menu 2", 1,
                      ["run cmd2a:cmd2a():cmd",
                       "run cmd2b:cmd2b():cmd",
                       "up:up:menu",
                       "exit:exit:menu"]])

menu1.show_menu()

while True:
    exec(menu1.get_choice())
    menu1.show_menu()