from urllib2 import urlopen
from bs4 import BeautifulSoup
#URL = 'http://phocks.org/stumble/creepy/'
URL=raw_input("Enter URL (e.g http://google.com)  : ")
soup = BeautifulSoup(urlopen(URL))
print(soup.title)
count=0
for link in soup.find_all('a'):
   print(link.get('href'))
   count+=1;
print("Number of URLs obtained = "+str(count))