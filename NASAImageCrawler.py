import requests
import re
from bs4 import BeautifulSoup as soup
import json
from time import sleep
from subprocess import run
import argparse

def get_links(pages,keys):
	links=[]
	for page in range(pages):
		url = 'https://images-api.nasa.gov/search?page={p}&media_type=image&q={k}'.format(p=page,k=keys)
		r= requests.get(url).json()
		
		try:
			items = r['collection']['items']
			for item in items:
				links.append(item['links'][0]['href'])
		except:
			try:
				sleep(5)
				continue
			except:
				print(page)
				break
	return links

def download_img(links,keys):
	for link in links:
		cmd='googleimagesdownload --keywords {k}  -x {l}'.format(k=keys,l=link.replace('~thumb','~orig'))
		run(cmd,shell=False)
	
if __name__ == '__main__':
	parse = argparse.ArgumentParser()
	parse.add_argument("-k",'--keywords',type=str,required=True,help='keywords')
	#parse.add_argument("-i", "--image_directory", type=str, required=False,help="specify a directory inside of the output directorydefault=keywords")
	#parse.add_argument("-o", "--output", type=str, required=False,help="output directory(default=downloads)")
	parse.add_argument("-p",'--pages',type=int, required=True,help="num of pages")
	
	args = parse.parse_args()
	keys = args.keywords
	pages = args.pages
	#output = args.output
	#folder_name =args.image_directory
	
	links = get_links(pages,keys)
	download_img(links,keys)