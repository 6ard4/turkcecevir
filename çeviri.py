import os
import time
os.system("python -m pip install colorama")
os.system("pip install tabulate")
print("tabulate yüklendi")
os.system("pip install googletrans")
print("googletrans ve tabulate yüklendi! \nBitti!")
time.sleep(2)
os.system("clear")
import colorama
from colorama import Fore, Back, Style

colorama.init()
print(Fore.RED)
print(Fore.YELLOW + Back.BLUE)
print("""

            ########################
            |                      |
            |   created by 6ard4   |
            |                      |
            ########################
""")
print(Style.RESET_ALL)

from tabulate import tabulate
from googletrans import Translator

class Simple_Translator(object):
    def __init__(self, word, Language):
        self.word = word
        self.language = Language
        self.cursor = Translator(service_urls=["translate.google.com"])

    def __repr__(self):
        translated = self.cursor.translate(self.word,
                            dest=self.language).text

        data = [["Diller:","Çeviri: "],
                ["girilen dil", self.word],
                ["Turkish", str(translated)]]     

        table = str(tabulate(data, headers="firstrow", tablefmt="grid")) 
        return table

if __name__ == "__main__":
    translate = input(r"Giriniz==> ")
    language = "tr"
    print(Simple_Translator(translate, language))


input("Devam etmek için herhangi bir tuşa bas...")
