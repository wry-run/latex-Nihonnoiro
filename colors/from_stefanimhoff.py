import requests
from bs4 import BeautifulSoup

# using https://www.crummy.com/software/BeautifulSoup/bs4/doc/

source = 'https://www.stefanimhoff.de/traditional-colors-of-japan/'

r = requests.get(source)

html_text = r.text

soup = BeautifulSoup(html_text, 'html.parser')

color = {}
#ja_Latn = ''

for info in soup.find_all('div', {"class": "color-swatch-info"}):

	title = info.find('h2', {"class": "color-swatch-title"})
	value = info.find('p', {"class": "color-swatch-value"})
	color[title.text] = value.text.replace('#','')
		

with open('Nihonnoiro_Hamada_Imhoff.sty', 'a') as f:
	
	for c in color.keys():
		#print(c)
		#print(color[c])
		
		latex_definecolor = f'\\definecolor{{{c}}}{{HTML}}{{{color[c]}}}'
		#print(latex_definecolor)
		
		f.write(f'{latex_definecolor}\n')
		
