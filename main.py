from bs4 import BeautifulSoup
import urllib.request
import re
num = input("Entrez le numero : ")
url = 'http://annuaire.freebox.fr/annuaire/?tel=' + num +'&submit_inv=Rechercher'
page = urllib.request.urlopen(url, timeout=20)
soup = BeautifulSoup(page,features="html.parser")
tel = soup.find_all('div', {'class': 'tel'}) #va chercher la classe tel dans le site de l'annuaire free
telephone=[]
for e in tel:
    e=e.text #prend le bout du code html avec le num
    telephone.append(e)
    e = e.replace('\n', '')
    res = [str(sub.split('\n')[1]) for sub in telephone]#convertion pip
    StrNum = "".join(res)#convertie en str
    print("Numero de telephone :" + str(StrNum).lstrip())#affiche et supprime les espaces de devant dans la liste
#PS:la tout est ok pas de verif
nom = soup.find_all('span',{'class': 'bold'})
NomDeFamille = []
for x in nom:
    x = x.text
    NomDeFamille.append(x)
    x = x.replace('[<span class="bold">', '   </span>, <span class="bold">Free, la société</span>, <span class="bold">Free recrute</span>, <span class="bold">Nous contact')#choisi entre les espace la valeur
    res1 = [str(sub.split('\n')[1]) for sub in NomDeFamille]#convertion pour extraire les str
    res2 = [str(sub.split('\n')[2]) for sub in NomDeFamille]
    StrNomdeFamille = "".join(NomDeFamille)#convertis les str trouvé
    print("Nom-Prenom :" + str(StrNomdeFamille).strip())#affiche et supprime les espace devant et derrière
    break
adress = soup.find('div',{'class': 'rue'})
List_adress = []
adress_text = adress.text
List_adress.append(adress_text)
adress = adress_text.replace('<div class="rue"> ', ' </div>')
print("Adresse : " + str(adress).strip())

city = soup.find('div',{'class': 'ville'})
List_city = []
city_text = city.text
List_city.append(city_text)
city = city_text.replace('<div class="rue"> ', ' </div>')
postal_code = re.sub(r'[^\d]+', '', city) 
city = re.sub(r'[^\D]+', '', city) 
print("Code Postal : " + str(postal_code).strip())

print("Ville : " + str(city).strip())
