#!/usr/bin/env python3

import subprocess, sys, time # replaced os with subprocess. its safer

try:
    from Instagram import SearchInsta
    from Search import WebSearch
    from EmailLookup import EmailLookup
    from SearchUsername import SearchUsername
    from PhoneLookup import PhoneLookup
    from IpLookup import IpLookup
except (ModuleNotFoundError, ImportError) as e:
    print(f"\033[31mimporting failed\033[0m. {e}")
    sys.exit(1)
# ui functions
def typewriter(text:str, delay:float=0.001) -> None:
    """
    prints char by char to STDOUT
    """
    for char in text:
        sys.stdout.write(char)
        time.sleep(delay)
        sys.stdout.flush()

    print("\n")


# helper functions
def list_options() -> None:
    """
    lists all the options available
    """
    options:list[str] = [
        "1. Scrape/Search Instagram",
        "2. Google Search",
        "3. Phone Number Lookup",
        "4. Ip Lookup",
        "5. Email Lookup",
        "6. Search Username across the web",
        "7. Update the tool",
        "8. re-list the options",
        "9. exit"
    ]


    print("*" * 25 + " OPTIONS " + "*" * 25)
    for option in options:
        print(f"\033[33m\t+\033[0m{option.upper()}.")

# main entry
def main():
    tool_logo:str = r"""
    0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777

    """

    typewriter(tool_logo)
    print("[user-agreement] by using this tool, you agree that the authors are not involved in any misuse of this tool. [Y]es [N]o")

    warning_agreement = input("agree?: ")
    if warning_agreement.lower() in ["y", "yes"]:
        ...
    else:
        raise Exception("User-Agreement: user did not agree")

    print("\033[2J\033[H") # clears the screen
    list_options()

    while True:
        try:
            option = int(input(">>> "))
        except ValueError:
            print("invalid input")
            continue

        match option:
            case 1:
                username = input("Enter the Instagram username: ")
                SearchInsta(username)
            case 2:
                query = input("Search here: ")
                WebSearch(query)
            case 3:
                phoneNo = input("Enter the phone no (with country code) : ")
                PhoneLookup(phoneNo)
            case 4:
                ip = input("Enter the ip address: ")
                IpLookup(ip)
            case 5:
                email = input("Enter the email address: ")
                EmailLookup(email)
            case 6:
                username = input("Enter the username: ")
                SearchUsername(username)
            case 7:
                try:
                    subprocess.run(["git pull"])
                except Exception as e:
                    print(f"\033[31mfailed to update due to \033[0m{e}")
            case 8:
                list_options()
            case 9:
                sys.exit()

            case _:
                print("option not recognized")

if __name__ == "__main__":
    main()
