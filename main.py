from bs4 import BeautifulSoup
import urllib.request
import re
import sys
sys.path.append("/freestart")
from freestart import num
num = num
url = 'http://annuaire.freebox.fr/annuaire/?tel=' + num +'&submit_inv=Rechercher'
page = urllib.request.urlopen(url, timeout=20)
soup = BeautifulSoup(page,features="html.parser")
test = soup.find_all('div', {'class': 'error'})

tel = soup.find_all('div', {'class': 'tel'})
telephone = []
for e in tel:
    e = e.text
    telephone.append(e)
    e = e.replace('\n', '')
    res = [str(sub.split('\n')[1]) for sub in telephone]
    StrNum = "".join(res)
nom = soup.find_all('span',{'class': 'bold'})
NomDeFamille = []
for x in nom:
    x = x.text
    NomDeFamille.append(x)
    x = x.replace('[<span class="bold">', '   </span>, <span class="bold">Free, la société</span>, <span class="bold">Free recrute</span>, <span class="bold">Nous contact')#choisi entre les espace la valeur
    res1 = [str(sub.split('\n')[1]) for sub in NomDeFamille]
    res2 = [str(sub.split('\n')[2]) for sub in NomDeFamille]
    StrNomdeFamille = "".join(NomDeFamille)
    break
adress = soup.find('div',{'class': 'rue'})
List_adress = []
adress_text = adress.text
List_adress.append(adress_text)
adress = adress_text.replace('<div class="rue"> ', ' </div>')



city = soup.find('div',{'class': 'ville'})
List_city = []
city_text = city.text
List_city.append(city_text)
city = city_text.replace('<div class="rue"> ', ' </div>')
postal_code = re.sub(r'[^\d]+', '', city)
city = re.sub(r'[^\D]+', '', city)

