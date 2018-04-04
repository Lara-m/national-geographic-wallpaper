'''
	Who wrote it: Lara

	usage: python WallPaperFetcher.py {working directort} {source}

	working directory: wspecify where the photo can be saved. Like "/home/randomuser/Pictures/Wallpapers"

	source: 
	" " - default - national geographics (literally put nothing)
	"nasa"
	"gopro"
	"bing"
	"desktoppr"
	"unsplash"
	"picsum"
	"splashbase"
	"cats"

	don't forget to add a 
'''

import os, sys, requests, urllib.request
from xml.etree import ElementTree

def natgeo():
	""" National Geographics """
	address = "https://www.nationalgeographic.com/photography/photo-of-the-day/_jcr_content/.gallery.json"
	req = (requests.get(url=address)).json()
	return req['items'][0]['url']+req['items'][0]['originalUrl']

def nasa():
	""" Nasa """
	address = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
	req = (requests.get(url=address)).json()
	return req['hdurl']

def gopro():
	""" GoPro """
	address = "https://api.gopro.com/v2/channels/feed/playlists/photo-of-the-day.json?platform=web&page=1&per_page=1"
	req = (requests.get(url=address)).json()
	wall_url = req['media'][0]['thumbnails']['full']['image']
	return wall_url

def bing():
	""" Bing """
	address = "http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-ww"
	res = requests.get(url=address)
	tree = ElementTree.fromstring(res.content)
	wall_url = "http://www.bing.com" + tree.find('image/url').text
	return wall_url

def desktoppr():
	""" Desktoppr """
	address = "https://api.desktoppr.co/1/wallpapers/random"
	res = (requests.get(url=address)).json()
	wall_url = res['response']['image']['url']
	return wall_url

def unsplash():
	""" Unsplash """
	address = "https://source.unsplash.com/random"
	return address

def picsum():
	""" Picsum """
	address = "https://picsum.photos/1920/1080/?random"
	return address

def splashbase():
	""" SplashBase """
	address = "http://www.splashbase.co/api/v1/images/random"
	res = (requests.get(url=address)).json()
	wall_url = res['large_url']
	return wall_url

def cats():
	""" The Cat API 
		Crazy Cat Lady strikes back ;P 
		It'd be good if I found a dog one as well... :thinking:
	"""
	address = "http://thecatapi.com/api/images/get?format=xml&results_per_page=1"
	res = requests.get(url=address)
	tree = ElementTree.fromstring(res.content)
	wall_url = tree.find('data/images/image/url').text
	return wall_url

def main(loc, source):
	# Change this to be custom
	wall_name = loc + '/wallpaper.jpg'
	if source == "nasa":
		wall_url = nasa()
	elif source == "gopro":
		wall_url = gopro()
	elif source == "bing":
		wall_url = bing()
	elif source == "desktoppr":
		wall_url = desktoppr()
	elif source == "unsplash":
		wall_url = unsplash()
	elif source == "picsum":
		wall_url = picsum()
	elif source == "splashbase":
		wall_url = splashbase()
	elif source == "cats":
		wall_url = cats()
	else:
		wall_url = natgeo()
	# Store the picture 
	urllib.request.urlretrieve(wall_url, wall_name)
	print(wall_url)
	if os.stat(wall_name).st_size < 0:
		return
	# Set the picture
	os.system('DISPLAY=:0 gsettings set org.gnome.desktop.background picture-uri "file://' + wall_name + '"')
	return

if __name__ == '__main__':
	if len(sys.argv) > 1:
		loc = sys.argv[1]
		if len(sys.argv) > 2:
			blah = sys.argv[2]
		else:
			blah = ""
		main(loc, blah)
	else:
		print ("Working directory is empty. Specify.")

