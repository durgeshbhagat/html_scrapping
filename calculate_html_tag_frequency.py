"""
python script to print html tag and their frquency in decending order

To Run : python calculate_htl_tag_frequency.py HTML_FILE_NAME
"""
import sys

from bs4 import BeautifulSoup

fname = sys.argv[1]


f= open(fname,'r')
html = f.read()
f.close()
soup = BeautifulSoup(html, 'html.parser')

tag_list = [tag.name for tag in soup.find_all()]
tag_dict = {}
for tag in tag_list:
    if tag in tag_dict:
        tag_dict[tag] += 1
    else:
        tag_dict[tag] = 1

tag_freq = tag_dict.items()
tag_freq.sort(key =  lambda item : item[-1], reverse= True)
for tag,freq in tag_freq:
    #print tag
    print '<%s> : %d' %(tag, freq)


