#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########

import os
import sys
import time
import urllib
import datetime
import wikipedia
import json
from speak_listen import *
from make_find_supp import *
from tab import *

################################## Fonction Recherche ################################

def search_web(ordre): # cherche sur google les 4 premier resultat et ouvre le lien choisi
	length = len(ordre)
	request = make_str(ordre,4,length)
	say_fr("je cherche sur internet, " + request)
	query = request
	query = urllib.urlencode ( { 'q' : query } )
	reponse = urllib.urlopen ( 'http://api.duckduckgo.com/?' + query + 'format=json')
	os.system('chromium-browser https://duckduckgo.com/?' + query)
	print reponse
	data = json.load(reponse)   
	print data
	results = json [ 'responseData' ] [ 'results' ]
	say_fr("les 4 premiers resultats sont :")
	print("===============================================================================")
	i = 0
	t_url = [" "]*4
	for result in results:
   		title = result['title']
   		url = result['url']
		title_str = supp_balise(title)
		t_url[i] = url
		i = i + 1
   		print ( str(i) + ' ==> ' + title_str + '; ' + url )
	print("===============================================================================")
	say_fr("pour ouvrire un lien, donné sont numéro, sinon tape exit")
	num = sub_menu()
	num = make_ordre(num)
	test = find_list(num,t_num)
	if test != "false":
		if test <= 2:
			url_open = t_url[0]
		elif test > 2 and test <= 6:
			url_open = t_url[1]
		elif test > 6 and test <= 9:
			url_open = t_url[2]
		elif test > 9 and test <= 13:
			url_open = t_url[3]
		os.system('nohup iceweasel "{0}" >/dev/null 2>&1 &'.format(url_open))
	else:
		print "je n'est pas compris le numero"

def search_wiki(ordre): # cherche sur Wiki, affiche un resume et ouvre un page wiki si desiré
	length = len(ordre)
	request = make_str(ordre,4,length)
	say_fr("je cherche sur wiki, " + request)
	wikipedia.set_lang("fr")
	result = wikipedia.page(request)
	print result.title
	print("===============================================================================")
	content = [" "]*100
	content = make_ordre(result.content)
	content = make_str(content,0,50)
	print(content + ".......")
	print("===============================================================================")
	say_fr("pour ouvrire la page, dit ouvre ou lance, sinon tape exit")
	open_link = sub_menu()
	open_link = make_ordre(open_link)
	if open_link[0] == t_ordre[2] or open_link[0] == t_ordre[3]:
		os.system('chromium-browser "{0}"'.format(result.url))
	else:
		print "je n'est pas compris le numero"

def search_youtube(ordre): # simple recherche youtube dans un fenetre iceweasel
	length = len(ordre)
	request = make_str(ordre,4,length)
	say_fr("je cherche sur youtube, " + request)
	say_fr("ouverture de la page youtube")
	os.system('chromium-browser https://www.youtube.com/results?search_query="{0}"'.format(request))
