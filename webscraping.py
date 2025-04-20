import urllib.request
from bs4 import BeautifulSoup

content = urllib.request.urlopen("https://en.wikipedia.org/wiki/Comet")
readcontent = content.read()

soup = BeautifulSoup(readcontent, "html.parser")  # Beatiful Soup variable
paragraphs = soup.find_all("p")
print(paragraphs[2], "\n")
h2 = soup.find_all("h2")
print("H2=", h2[0])


# Check in content
