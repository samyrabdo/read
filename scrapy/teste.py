import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

'''with open('cfederal.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html.parser')
print(soup_string)'''

'''r = requests.get('http://www.planalto.gov.br/ccivil_03/Constituicao/Constituicao.htm')
soup = BeautifulSoup(r.text,'lxml')
print(soup)'''

'''with open('cfederal.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
tag = soup.title
print(tag)
print(tag.name)

print(soup.p['class'])

#print(soup.a['href'])
print(soup.a['name'])'''

#with open('cfederal.html', 'r') as f:
#    soup = BeautifulSoup(f, 'html5lib')
#print(soup.prettify()) #traz todo o html da pagina formatdo
#print(soup.get_text()) #traz só o texto

#print(soup.p.get_text())#traz o texto da tag p, mas apenas da primeira, nesse caso

with open('cfederal.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
#print(soup.body.contents[15]) #acesso 15 elemento de body: id= art


#for child in soup.body.contents[15]: #traz cada paragrafo contendo o artigo refernte ao id[15]
#    print(child)                     #content só acesso filho direto, não acessa descendentes   

'''for child in soup.body.contents[15].p.children:
    if child.name != 'a':
        print(child) #pega o text da primeira p do id = art

for child in soup.body.contents[15].p.children:
    if child.name != 'a':
        print(child) #pega o text da primeira p do id = art'''

#print(len(list(soup.body))) 
#print(len(list(soup.descendants))) #acessa todos os filhos dos filhos

for tag in soup.descendants:
    if isinstance(tag, NavigableString): #testa se é uma string, se for uma string, imprime a string
        print(tag) #traz todos os textos de todos os elementos (filhos de filhos etc..)

for string in soup.stripped_strings: #remove espaços em branco    
    print(string)