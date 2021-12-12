import requests
from bs4 import BeautifulSoup
import cssutils

# using https://www.crummy.com/software/BeautifulSoup/bs4/doc/

source = 'https://en.wikipedia.org/wiki/Traditional_colors_of_Japan'

r = requests.get(source)

html_text = r.text

soup = BeautifulSoup(html_text, 'html.parser')

color_ja = {}
color_ja_Latn = {}
ja = ''
ja_Latn = ''

for table in soup.find_all('table', {"class": "wikitable"}):
	for data in table.find_all('td'):
	
		j = data.find('span', lang="ja")
		if j:
			ja = j.text
			
		ja_L = data.find('i', lang="ja-Latn")
		if ja_L:
			ja_Latn = ja_L.text.split(" (")[0]
		
		if data.has_attr('style'):
			style = cssutils.parseStyle(data["style"])
			value = style["background"].replace('#','')
	
			color_ja_Latn[ja_Latn] = value
			color_ja[ja] = value

	

with open('Nihonnoiro_wikipedia_ja_Latn.sty', 'a') as f:
	
	for c in color_ja_Latn.keys():
		#print(c)
		#print(color[c])
		
		latex_definecolor = f'\\definecolor{{{c}}}{{HTML}}{{{color_ja_Latn[c]}}}'
		#print(latex_definecolor)
		
		f.write(f'{latex_definecolor}\n')
		
with open('Nihonnoiro_wikipedia_ja.sty', 'a') as f:
	
	for c in color_ja.keys():
		#print(c)
		#print(color[c])
		
		latex_definecolor = f'\\definecolor{{{c}}}{{HTML}}{{{color_ja[c]}}}'
		#print(latex_definecolor)
		
		f.write(f'{latex_definecolor}\n')
