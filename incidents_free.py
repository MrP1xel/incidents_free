import socket
from json import load
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

arguments = sys.argv
if len(arguments) == 2:
        dlsam_name = arguments[1]
else:
        public_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
        temp_public_hostname = socket.gethostbyaddr(public_ip)
        public_hostname = temp_public_hostname[0]
        dlsam_name = public_hostname.split("-")[0]
        print("IP publique : %s" % public_ip)
        print("Hostname public : %s" %public_hostname)
        print("NRA free : %s" % dlsam_name)


free_reseau_page = "http://www.free-reseau.fr/"
custom_free_reseau_page = free_reseau_page + dlsam_name


print("######[Liste des derniers incidents]########")

page = urlopen(custom_free_reseau_page)
soup = BeautifulSoup(page,"html.parser")
general_box = soup.find(attrs={'ul','class','general'})
liste = general_box.find('ul')
incidents =  liste.findAll('a')
for incident in incidents[:-1]:
        print(incident.text)
