#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########

import os
import sys
import time
import urllib
import pyicloud
import datetime
import wikipedia
import json as m_json
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
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json = m_json.loads ( response )
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
		os.system('iceweasel "{0}"'.format(result.url))
	else:
		print "je n'est pas compris le numero"

def search_youtube(ordre): # simple recherche youtube dans un fenetre iceweasel
	length = len(ordre)
	request = make_str(ordre,4,length)
	say_fr("je cherche sur youtube, " + request)
	say_fr("ouverture de la page youtube")
	os.system('iceweasel https://www.youtube.com/results?search_query="{0}"'.format(request))

def search_cal(ordre): # cherche dans calendrier icloud
	from pyicloud import PyiCloudService
	format_date = [" "]*2
	say_fr("connection au calendrier")
	api = PyiCloudService('blaurens31@gmail.com', 'Smok871005')
	say_fr("connection ok")
	length = len(ordre)
	if length > 5:
		request = make_str(ordre,5,length)
		say_fr("je cherche dans ton agenda les événements pour " + request)
	else:
		say_fr("quel date veux tu consulter")
		request = sub_menu()
	request = make_ordre(request)
	test = find_list(request,t_date)
	test2 = find_list(request,t_adj)
	format_date = make_date(test,test2)
	event = str(api.calendar.events(format_date[0],format_date[1]))
	event = supp_spec(event)
	event = make_ordre(event)
	event = make_cal(event)
	print("===============================================================================")
	say_fr("tu a " + str(len(event)) + " événements")
	i = 0
	while i < len(event):
		say_fr(event[i])
		i = i + 1
	print("===============================================================================")
