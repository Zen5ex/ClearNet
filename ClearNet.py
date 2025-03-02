import os
import colorama
import requests
from stem import Signal
from stem.control import Controller
from colorama import Fore, Style, init


init(autoreset=True)


text = """
 _____  _                     _   _        _   
/  __ \| |                   | \ | |      | |  
| /  \/| |  ___   __ _  _ __ |  \| |  ___ | |_ 
| |    | | / _ \ / _` || '__|| . ` | / _ \| __|
| \__/\| ||  __/| (_| || |   | |\  ||  __/| |_ 
 \____/|_| \___| \__,_||_|   \_| \_/ \___| \__|
"""


print(Fore.RED+ text + Style.RESET_ALL)



print('Created by @takivaratensai or Zen5ex on github')
def change_ip_via_tor():
    try:
        
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  
            controller.signal(Signal.NEWNYM)  

        
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        response = requests.get('http://httpbin.org/ip', proxies=proxies)

        
        print("Your new IP:", response.json()['origin'])
    except Exception as e:
        print(f"Error: {e}")


change_ip_via_tor()
def main_menu():
    while True:
        print("\nmain menu:")
        print("1. start ip changer")
        choice = input("Select options(you don't any other options )")
        if choice == '1':
            change_ip_via_tor()
if __name__ == "__main__":
    main_menu()