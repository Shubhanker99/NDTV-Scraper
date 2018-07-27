import requests
from bs4 import BeautifulSoup

page = requests.get("http://feeds.feedburner.com/ndtvnews-top-stories")
soup = BeautifulSoup(page.content, features="xml")
items = soup.findAll('item')

file = open('Top Stories.txt', "r")
lineList = file.readlines()
file.close()

if len(lineList) != 0:
	notImp = lineList[-8]
	words = notImp.split()
	Imp = words[-2]
	lol = ((int(Imp[0])*10 + int(Imp[1]))*60 + int(Imp[3])*10 + int(Imp[4]))*60 + int(Imp[6])*10 + int(Imp[7])

f = open("Top Stories.txt", "a+")

for item in reversed(items):

	if len(lineList) == 0:
		f.write('Published on: %s\n' %item.pubDate.text)
		f.write('Title: %s\n' %item.title.text)
		f.write('Source: %s\n' %item.source.text)
		f.write('Category: %s\n' %item.category.text)
		f.write('Description: %s\n' %item.description.text)
		f.write('Link: %s\n' %item.link.text)
		f.write('Image URL: %s\n\n' %item.fullimage.text)
		continue

	p = item.pubDate.text
	q = p.split()
	Imp1 = q[-2]
	lol1 = ((int(Imp1[0])*10 + int(Imp1[1]))*60 + int(Imp1[3])*10 + int(Imp1[4]))*60 + int(Imp1[6])*10 + int(Imp1[7])

	if int(q[1]) > int(words[3]):
		f.write('Published on: %s\n' %item.pubDate.text)
		f.write('Title: %s\n' %item.title.text)
		f.write('Source: %s\n' %item.source.text)
		f.write('Category: %s\n' %item.category.text)
		f.write('Description: %s\n' %item.description.text)
		f.write('Link: %s\n' %item.link.text)
		f.write('Image URL: %s\n\n' %item.fullimage.text)
	elif lol1 > lol:
		f.write('Published on: %s\n' %item.pubDate.text)
		f.write('Title: %s\n' %item.title.text)
		f.write('Source: %s\n' %item.source.text)
		f.write('Category: %s\n' %item.category.text)
		f.write('Description: %s\n' %item.description.text)
		f.write('Link: %s\n' %item.link.text)
		f.write('Image URL: %s\n\n' %item.fullimage.text)
	else:
		continue

f.close()

#	crontab -e
#	*/5 * * * * /home/shubhanker/Scraper_NDTV.py