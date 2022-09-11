import requests
import os
import sys
import time

sys.path.append("/main")
num = input("Enter valid free phone number : ")
free = requests.get("http://annuaire.freebox.fr/annuaire/?tel=" + num + "&submit_inv=Rechercher")


if "<!-- TEL -->" in free.text:
    time.sleep(0.25)
    print("Number Found !")
    print("Please wait..")
    time.sleep(1.5)
    os.system('main.py')
else:
    print("The number was not found.")
    print("Menu")
    print("[1]" + "Exit" + "\n[2]Enter Another Number")
    select = int(input("Enter a Number : "))
    if select == 2:
        os.system("python main.py")
    else:
        print("See you soon :)")

from main import StrNum
print("Numero de telephone :" + str(StrNum).lstrip())
from main import StrNomdeFamille
print("Prenom-Nom :" + str(StrNomdeFamille).strip())
from main import adress
print("Adresse : " + str(adress).strip())
from main import postal_code
print("Code Postal : " + str(postal_code).strip())
from main import city
print("Ville : " + str(city).strip())
time.sleep(2)
print("Menu\n")
time.sleep(1)
print("[1]" + "Exit" + "\n[2]Enter Another Number")
select = int(input("Enter a Number : "))
if select == 2:
  os.system("python main.py")
else:
     print("See you soon :)")
     time.sleep(3)

