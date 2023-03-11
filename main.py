import requests
import colorama;from colorama import init;init(autoreset=True)
import os

_author_ = 'bolt#1172'
_server_ = 'https://dsc.gg/binded'
_language_ = 'python'

class Bolt:
    def __init__(self):
        os.system('title killhook | bolt#1172')
        self.webhook = input(colorama.Fore.MAGENTA + '[ % ] Webhook Here : ')
        self.amount = int(input(colorama.Fore.MAGENTA + '[ % ] Amount Here : '))
        self.message = input(colorama.Fore.MAGENTA + '[ % ] Message Here : ')
        self.username = input(colorama.Fore.MAGENTA + '[ % ] Username Here : ')
        self.image = input(colorama.Fore.MAGENTA + '[ % ] Image Addr Here : ')

        self.spam()

    def spam(self):
        count = 0 
        while count <= self.amount:
            requests.post(self.webhook, json={'content': self.message, 'username': self.username, 'avatar_url': self.image})
            count += 1 
            print(colorama.Fore.GREEN + f'[ ! ] Sent {count}')
        delete = input(colorama.Fore.MAGENTA + '[ % ] Delete Webhook ? Y/n : ')
        if delete.lower() == 'y':
            self.delete()
            self.__init__()
        else:
            self.__init__()
    
    def delete(self):
        requests.delete(self.webhook)
        print(colorama.Fore.GREEN + "[ ! ] Deleted !")

if __name__ == '__main__':
    Bolt()
