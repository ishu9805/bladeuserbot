

import os

a = r"""

██████╗░██╗░░░░░░█████╗░██████╗░███████╗  ██╗░░██╗  ██╗░░░██╗░██████╗███████╗██████╗░██████╗░░█████╗░████████╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝  ╚██╗██╔╝  ██║░░░██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░░░░███████║██║░░██║█████╗░░  ░╚███╔╝░  ██║░░░██║╚█████╗░█████╗░░██████╔╝██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░░░░██╔══██║██║░░██║██╔══╝░░  ░██╔██╗░  ██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗██╔══██╗██║░░██║░░░██║░░░
██████╦╝███████╗██║░░██║██████╔╝███████╗  ██╔╝╚██╗  ╚██████╔╝██████╔╝███████╗██║░░██║██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═╝░░╚═╝  ░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░
"""


def start():

    clear_screen()
    check_for_py()

    print(f"{a}\n\n")
    print("Welcome to blade_x_userbot, lets start setting up!\n\n")
    print("Cloning the repository...\n\n")
    os.system("rm -rf bladeuserbot")
    os.system("git clone https://github.com/ishu9805/bladeuserbot")
    print("\n\nDone")
    os.chdir("bladeuserbot")
    clear_screen()
    print(a)
    print("\n\nLet's start!\n")

   
    # start bleck megik
    print("\n\nLets start entering the variables.\n\n")
    varrs = [
        "API_ID",
        "API_HASH",
        "SESSION",
        "MONGO_URI",
    ]
    all_done = "# Ultroid Environment Variables.\n# Do not delete this file.\n\n"
    for i in varrs:
        all_done += do_input(i)
    clear_screen()
    print(a)
    print("\n\nHere are the things you've entered.\nKindly check.")
    print(all_done)
    isitdone = input("\n\nIs it all correct? [y/n]")
    if isitdone == "y" or isitdone != "n":
       
        f = open(".env", "w")
        f.write(all_done)
    else:
        print("Oh, let's redo these then.")
        start()
    clear_screen()
    print("\nCongrats. All done!\nTime to start the bot!")
    print("\nInstalling requirements... This might take a while...")
    os.system("pip3 install --no-cache-dir -r requirements.txt")
    ask = input(
        "Enter 'yes/y' to Install other requirements, required for local deployment."
    )
    if ask.lower().startswith("y"):
        print("Started Installing...")
        os.system(
            "pip3 install --no-cache-dir -r resources/startup/optional-requirements.txt"
        )
    else:
        print("Skipped!")
    clear_screen()
    print(a)
    print("\nStarting Blade_x_userbot...")
    os.system("sh startup")


def do_input(var):
    val = input(f"Enter your {var}: ")
    return f"{var}={val}\n"


def clear_screen():
    # clear screen
    _ = os.system("clear") if os.name == "posix" else os.system("cls")


def check_for_py():
    print(
        "Please make sure you have python installed. \nGet it from http://python.org/\n\n",
    )
    try:
        ch = int(
            input(
                "Enter Choice:\n1. Continue, python is installed.\n2. Exit and install python.\n",
            ),
        )
    except BaseException:
        print("Please run the script again, and enter the choice as a number!!")
        exit(0)
    if ch == 1:
        pass
    elif ch == 2:
        print("Please install python and continue!")
        exit(0)
    else:
        print("Weren't you taught how to read? Enter a choice!!")
        return


def gen_session():
    print("\nProcessing...")
    os.system("python3 resources/session/ssgen.py")


start()
