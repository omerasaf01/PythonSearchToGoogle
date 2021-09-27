from googlesearch import search
import webbrowser
import json

"""

Çalışması İçin "Google" Api Kütüphanesi Kurulu Olmalı 
"pip install google"
Diğer Kütüphaneler Python ile Yüklü Gelir

"""

class Google:

    def __init__(self, arama):
        self.arama = arama
        with open("Settings.json", "r") as fpp:
            self.data = json.load(fpp)
        self.max = self.data["MaxSearch"]

    def Arama(self):
        links = ["https://codexplant.com"]
        number = 0
        for url in search(self.arama, stop = int(self.max)):
            number += 1
            print(str(number) + " " + str(url))
            links.append(url)
        input_number = int(input(":"))
        webbrowser.open_new_tab(links[input_number])

    def SetMaxSearch(self, maxsearch = "20"):
        print("Settings Updating")
        self.data["MaxSearch"] = {}
        self.data["MaxSearch"] = maxsearch
        with open("Settings.json", "w") as fp:
            json.dump(self.data, fp, indent = 4)
        print("Task Ended")

while True:
    search_text = input("Search -> ")
    Search = Google(search_text)
    if search_text == "SetMax":
        max = input("Max: ")
        Search.SetMaxSearch(max)
    else:
        Search.Arama()