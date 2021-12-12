import requests
from bs4 import BeautifulSoup
import cssutils

# using https://www.crummy.com/software/BeautifulSoup/bs4/doc/

source = 'http://kidorakujapan.com/know/others_color_2.html'

r = requests.get(source)

html_text = r.text

soup = BeautifulSoup(html_text, 'html.parser')

table = soup.find('table', id='menu6')

color = {}

for data in table.find_all('td'):
	
	# color definition is in the background property of inline style tag. Remove the # symbol for latex
	
	style = cssutils.parseStyle(data["style"])
	value = style["background"].replace('#','')
	#print(value)
	
	# roomaji text is followed by (english translation), sometimes with typos; just get the first part
	romaji = data.text.split(" (")[0]
	#print(f'text: {romaji}')
				
	color[romaji]=value
	
with open('Nihonnoiro_kidorakujapan.sty', 'a') as f:
	
	for c in color.keys():
		#print(c)
		#print(color[c])
		
		latex_definecolor = f'\\definecolor{{{c}}}{{HTML}}{{{color[c]}}}'
		#print(latex_definecolor)
		
		f.write(f'{latex_definecolor}\n')
