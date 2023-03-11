import requests
import colorama;from colorama import init;init(autoreset=True)

__author__ = 'bolt#1172'
__server__ = 'dsc.gg/binded'


class Bolt:
    def __init__(self):
        self.webhook = input(colorama.Fore.LIGHTMAGENTA_EX + '[ $ ] Webhook Here : ')
        self.amount = int(input(colorama.Fore.LIGHTMAGENTA_EX + '[ $ ] Amount Here : '))
        self.message = input(colorama.Fore.LIGHTMAGENTA_EX + '[ $ ] Message Here : ')
        self.username = input(colorama.Fore.LIGHTMAGENTA_EX + '[ $ ] Username Here : ')
        self.image = input(colorama.Fore.LIGHTMAGENTA_EX + '[ $ ] Image Addr Here : ')

        self.spam()

    def spam(self):
        count = 0
        while count < self.amount:
            requests.post(self.webhook, data={'content': self.message, 'username': self.username, 'avatar_url': self.image})
            count += 1 
            print(colorama.Fore.GREEN + f"[ * ] Sent {count}")

if __name__ == '__main__':
    Bolt()
