import os

prefix = "$"
cprefix = prefix

background = "0"
textcolor = "7"

def refresh():
    global prefix, cprefix, background, textcolor
    os.system(f"color {background + textcolor}")
    prefix = cprefix

refresh()

print("Custom CMD by Wojtmic v1.0\n")

while True:
    cmd = input(f"{os.getcwd()} {prefix} ")
    cmdS = cmd.split()
    if cmd == "exit":
        break
    if cmdS[0] == "cd":
        os.chdir(cmdS[1])
    if cmdS[0] == "style":
        if len(cmdS) > 1:
            if cmdS[1] == "refresh":
                refresh()
                print("Refreshed style!")
            elif cmdS[1] == "background":
                if len(cmdS) > 2:
                    if cmdS[2] == "black":
                        background = "0"
                    elif cmdS[2] == "blue":
                        background = "1"
                    elif cmdS[2] == "green":
                        background = "2"
                    elif cmdS[2] == "aqua":
                        background = "3"
                    elif cmdS[2] == "red":
                        background = "4"
                    elif cmdS[2] == "purple":
                        background = "5"
                    elif cmdS[2] == "yellow":
                        background = "6"
                    elif cmdS[2] == "white":
                        background = "7"
                    elif cmdS[2] == "gray":
                        background = "8"
                    elif cmdS[2] == "lblue":
                        background = "9"
                    elif cmdS[2] == "lgreen":
                        background = "a"
                    elif cmdS[2] == "laqua":
                        background = "b"
                    elif cmdS[2] == "lred":
                        background = "c"
                    elif cmdS[2] == "lpurple":
                        background = "d"
                    elif cmdS[2] == "lyellow":
                        background = "e"
                    elif cmdS[2] == "lwhite":
                        background = "f"
                    else:
                        print("Invalid color! Use \"style colors\" for list of colors!")
                else:
                    print("style color requires color argument!")
            elif cmdS[1] == "text":
                if len(cmdS) > 2:
                    if cmdS[2] == "black":
                        textcolor = "0"
                    elif cmdS[2] == "blue":
                        textcolor = "1"
                    elif cmdS[2] == "green":
                        textcolor = "2"
                    elif cmdS[2] == "aqua":
                        textcolor = "3"
                    elif cmdS[2] == "red":
                        textcolor = "4"
                    elif cmdS[2] == "purple":
                        textcolor = "5"
                    elif cmdS[2] == "yellow":
                        textcolor = "6"
                    elif cmdS[2] == "white":
                        textcolor = "7"
                    elif cmdS[2] == "gray":
                        textcolor = "8"
                    elif cmdS[2] == "lblue":
                        textcolor = "9"
                    elif cmdS[2] == "lgreen":
                        textcolor = "a"
                    elif cmdS[2] == "laqua":
                        textcolor = "b"
                    elif cmdS[2] == "lred":
                        textcolor = "c"
                    elif cmdS[2] == "lpurple":
                        textcolor = "d"
                    elif cmdS[2] == "lyellow":
                        textcolor = "e"
                    elif cmdS[2] == "lwhite":
                        textcolor = "f"
                    else:
                        print("Invalid color! Use \"style colors\" for list of colors!")
                else:
                    print("style color requires color argument!")
            elif cmdS[1] == "colors":
                os.system("start https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/color")
            elif cmdS[1] == "prefix":
                if len(cmdS) > 2:
                    cprefix = cmdS[2]
        else:
            print("Command style requires arguments.")
    else:
        os.system(cmd)

os.system("color 07")
