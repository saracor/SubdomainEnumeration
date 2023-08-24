#! /usr/bin/python3

import requests
import time

print(
'''
 ____        _         _                       _       
/ ___| _   _| |__   __| | ___  _ __ ___   __ _(_)_ __  
\___ \| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \ 
 ___) | |_| | |_) | (_| | (_) | | | | | | (_| | | | | |
|____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|
                                                       
                                           _   _             
  ___ _ __  _   _ _ __ ___   ___ _ __ __ _| |_(_) ___  _ __  
 / _ \ '_ \| | | | '_ ` _ \ / _ \ '__/ _` | __| |/ _ \| '_ \ 
|  __/ | | | |_| | | | | | |  __/ | | (_| | |_| | (_) | | | |
 \___|_| |_|\__,_|_| |_| |_|\___|_|  \__,_|\__|_|\___/|_| |_|

''')

targeturl = input("Input target URL > ")
targeturl = targeturl.replace("http://", "")
targeturl = targeturl.replace("https://", "")
targeturl = targeturl.replace("www.", "")
found_subdomains = []

wordlist = input("Input subdomain wordlist location > ")

print()

with open(wordlist, "r") as subdomain:
	for sub in subdomain:
		newsub = sub.replace("\n", "")
		time.sleep(0.5)
		try:
			try_page = requests.get(f"https://{newsub}.{targeturl}")
			status = try_page.status_code
			print(f"Subdomain found! >>> https://{newsub}.{targeturl} >> Status code: {status}")
			found_subdomains.append(f"https://{newsub}.{targeturl} >> Status code: {status}")
		except requests.exceptions.ConnectionError:
			print("ConnectionError, moving on to next subdomain...")

print("--------------------------------------------")
if found_subdomains:
	print("List of found subdomains\n")
	for i in found_subdomains:
		print(i)
else:
	print("No subdomains found.")