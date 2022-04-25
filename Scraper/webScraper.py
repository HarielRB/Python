from bs4 import BeautifulSoup
import requests


# .content traz todo o conteúdo
site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')
agroclima = soup.find("a", class_ = "link actTriggerGA" )
# print(soup.prettify()) para printar o site
print(agroclima.string)
print(soup.title.string)
# pretify transforma todo o html em string
