import os
from functions import *
from pyfiglet import Figlet
from config import config_Globals

class main_Globals:
    main_menu = 1
    welcome_text = Figlet(font=config_Globals.welcome_text["font"]).renderText(config_Globals.welcome_text["text"])

def main():
    input("Be sure to run the program with sudo permission!\nPress Enter to continue")
    while main_Globals.main_menu == 1:
        os.system('clear')
        print("#" * 80)
        print(main_Globals.welcome_text)
        print("#" * 80)
        print("\n" + status('nginx') + "\t" + status('mysql') + "\t" + status('php7.2-fpm'))
        x = input("\nMain menu:\n"
                  "\n1)Start nginx\t2)Stop nginx\t3)Reload nginx"
                  "\n11)Start mysql\t22)Stop mysql\t33)Reload mysql"
                  "\n111)Start php\t222)Stop php\t333)Reload php"
                  "\n\ne)exit\n"
                  "\nInput: ")

        if x == '1':
            start('nginx')
        elif x == '2':
            stop('nginx')
        elif x == '3':
            reload('nginx')

        elif x == '11':
            start('mysql')
        elif x == '22':
            stop('mysql')
        elif x == '33':
            reload('mysql')

        elif x == '111':
            start('php7.2-fpm')
        elif x == '222':
            stop('php7.2-fpm')
        elif x == '333':
            reload('php7.2-fpm')

        elif x == 'e':
            input("Press enter to exit")
            main_Globals.main_menu = 0

        else:
            input("Please give a valid input!")
    exit(0)


if __name__ == '__main__':
    main()
