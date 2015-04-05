#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########
import os  
import sys
import time
import urllib
import pyaudio
import pyicloud
import datetime
import wikipedia
import json as m_json
import speech_recognition as sr
######### tableau ##########
t_salutation = ["Bonjour", "Salut", "Yo", "Hello"]
t_ordre = ["cherche", "recherche", "ouvre", "lance", "allume"]
t_media = ["internet","google","wiki","Wikipédia","Youtube","agenda"]
t_app = ["internet", "gedit", "arduino", "terminal","putty","music"]
t_domotique = ["lumière", "ordinateur", "pc", "télé", "rétro", "rétroprojecteur"] 
t_room = ["salon", "bureau"]
t_num = ["1","un","premier","second","2","deux","deuxième","troisième","3","trois","quatre","quatrième","4","dernier"]
t_date = ["aujourd'hui","demain","week-end","semaine","mois"]
t_adj = ["prochain","prochaine","ce","cette","après"]
exit = 0

################################## Fonction Speak/Listen ################################

def say_fr(something): # parle en francais
	print something 
	os.system('espeak -s 180 -p 99 -v fr "{0}" --stdout|paplay'.format(something))

def say_en(something): # parle en englais
	print something
	os.system('espeak -s 180 -p 99 -v en "{0}" --stdout|paplay'.format(something))

def listen(): # ecoute et ecrit
	r = sr.Recognizer(language = "fr-FR")
	with sr.Microphone() as source:               
  		audio = r.listen(source)
	try:
  		print(r.recognize(audio))  
	except LookupError:                            # speech is unintelligible
    		print("Could not understand audio")
		return "pas compris"
	ordre = r.recognize(audio)
	return ordre.encode('utf8')

################################## Fonction Gestion ################################

def find_list(l1,l2): # cherche si un argument de "l1" et dans "l2" et retourne sont n'indice
	i = 0
	while i < len(l1):
		j = 0
		while j < len(l2):
			if l1[i] == l2[j]:
				return j
			else :
				j = j + 1
		i = i + 1
	return "false"		

def find_word(w,li): # cherche un mot "w" dans une liste "li" et retourne "ok" si oui 
	k = 0
	while k < len(li):
		if w == li[k]:
			return "ok"
			break
		else:
			k=k+1
	
	return 0

def supp_balise(t_char): # supprime les balise HTML dans un tableau de charactere
	new_t_char = [" "]*(len(t_char))
	length = len(t_char)
	balise = 0
	i = 0
	j = 0
	while j <= (length-1):
		if t_char[j] == '<' and balise == 0:
			j = j + 1
			balise = 1
		elif t_char[j] == '>' and balise == 1:
			j = j + 1
			balise = 0
		elif balise == 1:
			j = j + 1
		else:
			new_t_char[i] = t_char[j]
			j = j + 1
			i = i + 1
	return "".join(new_t_char)
		 
			
def make_str(ordre,index,length): # decoupe un tableau de string a partir de l'argument "index" a "length"
	request = [0]*((length - index) * 2)
	j = 0
	while index <= (length-1):
		request[j] = ordre[index]
		index = index + 1
		j = j + 1
		request[j] = " "
		j = j + 1
	return "".join(request)

def make_ordre(ordre): # construit un tableau de string a partir du tableau de char 
	space_count = 0
	count_char = 0
	length = 0
	i = 0
	j = 0
	k = 0
	z = 0
	while i < len(ordre):
		if ordre[i] == " ":
			space_count = space_count + 1
			i = i + 1
		else:
			i = i + 1
	length = space_count + 1
	new_ordre = [" "]*length
	i = 0
	while i < length:
		count_char = 0
		while ordre[z] != " ":
			count_char = count_char + 1
			z = z + 1
			if z == len(ordre):
				break
		temp = [" "]*count_char
		while ordre[j] != " ":
			temp[k] = ordre[j]
			j = j + 1
			k = k + 1
			if k == count_char:
				break
		new_ordre[i] = "".join(temp)
		i = i + 1
		if j < len(ordre) and i < length:
			if ordre[j] == " ":
				j = j + 1
		if z < len(ordre):
			if ordre[z] == " ":
				z = z + 1
		k = 0
	return new_ordre

def make_date(index):
	date = [0]*2
	if index == 0:
		date[0] = datetime.datetime.now() - datetime.timedelta(days=1)
		print date[0]
		return date
	elif index == 1:
		return 0

def sub_menu(): # affiche un sous-menu pour choisir une action dans une fonction
	choix = raw_input("choix par < text > ou < speech > : ")
	if choix == "text":
		ordre = raw_input("tapez votre selection : ")
	elif choix == "speech":
		print("parler maintenant")
		ordre = listen()
	elif choix == "exit":
		say_fr("retour au menu principale")
	else:
		say_fr("je n'est pas compris")
	return str(ordre)

################################## Fonction Recherche ################################

def search_web(ordre): # cherche sur google les 4 premier resultat et ouvre le lien choisi
	length = len(ordre)
	say_fr("je cherche sur internet")
	request = make_str(ordre,4,length)
	say_fr(request)
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
	say_fr("pour ouvrire un lien, donné sont numéro, sinon exit")
	num = sub_menu()
	num = make_ordre(num)
	test = find_list(num,t_num)
	if test <= 2:
		url_open = t_url[0]
	elif test > 2 and test <= 6:
		url_open = t_url[1]
	elif test > 6 and test <= 9:
		url_open = t_url[2]
	elif test > 9 and test <= 13:
		url_open = t_url[3]
	else:
		print "je n'est pas compris le numero"
	os.system('iceweasel "{0}"'.format(url_open))

def search_wiki(ordre): # cherche sur Wiki, affiche un resume et ouvre un page wiki si desiré
	say_fr("je cherche sur wikipédia")
	length = len(ordre)
	request = make_str(ordre,4,length)
	say_fr(request)
	wikipedia.set_lang("fr")
	result = wikipedia.page(request)
	print result.title
	print("===============================================================================")
	content = [" "]*100
	content = make_ordre(result.content)
	content = make_str(content,0,50)
	print (content + ".......")
	print("===============================================================================")
	say_fr("pour ouvrire la page, dite ouvre ou lance, sinon exit")
	open_link = sub_menu()
	open_link = make_ordre(open_link)
	if open_link[0] == t_ordre[2] or open_link[0] == t_ordre[3]:
		os.system('iceweasel "{0}"'.format(result.url))
	else:
		print "je n'est pas compris le numero"

def search_youtube(ordre): # simple recherche youtube dans un fenetre iceweasel
	say_fr("je cherche sur youtube")
	length = len(ordre)
	request = make_str(ordre,4,length)
	say_fr(request)
	say_fr("ouverture de la page youtube")
	os.system('iceweasel https://www.youtube.com/results?search_query="{0}"'.format(request))

def search_cal(ordre): # cherche dans calendrier icloud
	from pyicloud import PyiCloudService
	format_date = [" "]*2
	say_fr("je cherche dans votre agenda")
	#api = PyiCloudService('blaurens31@gmail.com', 'Smok871005')
	say_fr("connection a l'agenda, ok")
	say_fr("quel date voulez vous consulter")
	date = sub_menu()
	date = make_ordre(date)
	test = find_list(date,t_date)
	format_date = make_date(test)
	event = api.calendar.events(format_date[0],format_date[1])
	say_fr(event)

def exe_ordre(ordre):
	length = len(ordre)
	say_fr("éxécution")
	if ordre[1] == t_ordre[0] and length > 4 or ordre[1] == t_ordre[1] and length > 4: #cherche ou recherche
		media = find_word(ordre[3],t_media)
		if media == 0 and length > 4:
			media = find_word(ordre[4],t_media)
		if media == "ok":
			if ordre[3] == t_media[0] or ordre[3] == t_media[1]:
				search_web(ordre)
			elif ordre[3] == t_media[2] or ordre[3] == t_media[3]:
				search_wiki(ordre)
			elif ordre[3] == t_media[4]:
				search_youtube(ordre)
			elif ordre[4] == t_media[5]:
				search_cal(ordre)
		else:
			say_fr("je ne connait pas ce media")
	elif ordre[1] == t_ordre[2] and length >= 3 or ordre[1] == t_ordre[3] and length >= 3: #ouvre ou lance
		app = find_word(ordre[2],t_app)
		if app == "ok":
			if ordre[2] == t_app[0]:
				say_fr("j'ouvre l'application internet")
			elif ordre[2] == t_app[1]:
				say_fr("j'ouvre l'application gedit")
			elif ordre[2] == t_app[2]:
				say_fr("j'ouvre l'application arduino")
			elif ordre[2] == t_app[3]:
				say_fr("j'ouvre l'application terminal")
			elif ordre[2] == t_media[4]:
				say_fr("j'ouvre l'application putty")
			elif ordre[2] == t_media[5]:
				say_fr("j'ouvre l'application music")
		else:
			say_fr("je ne connait pas cette application")
	elif ordre[1] == t_ordre[4] and length >= 3: #allume
		domo = find_word(ordre[3],t_domotique)
		if domo == "ok":
			if ordre[3] == t_domotique[0]:
				say_fr("j'allume la lumiére")
				if ordre[length-1] == t_room[0]:
					say_fr("du salon")
				elif ordre[length-1] == t_room[1]:
					say_fr("du bureau ")
				else:
					say_fr("le bureau ou le salon?")
			elif ordre[3] == t_domotique[1] or ordre[3] == t_domotique[2]:
				say_fr("j'allume l'ordinateur")
				if ordre[length-1] == t_room[0]:
					say_fr("du salon")
				elif ordre[length-1] == t_room[1]:
					say_fr("du bureau ")
				else:
					say_fr("le bureau ou le salon?")
			elif ordre[3] == t_domotique[3]:
				say_fr("j'allume la télé")
			elif ordre[2] == t_domotique[4] or ordre[3] == t_domotique[5]:
				say_fr("j'allume le retroprojecteur")
		else:
			say_fr("je ne connait pas ce périphérique")
	else:
		say_fr("pas suffisament d'information")

say_en("i'm Bender, lick my shiny metal ass")
say_fr("Que puis-je faire pour vous")
test = make_date(0)
while exit == 0:
	print("pour faire une demande ecrite, tapez le mot : < text >")
	print("pour faire une demande oral, tapez le mot : < speech >")
	choix = raw_input("entrez votre choix : ")
	if choix == "text":
		print("commencer votre phrase par Bender suivie de votres demande ou exit pour terminer")
		ordre = raw_input("entrez votre demande : ")
	elif choix == "speech":
		print("commencer votre phrase par Bender suivie de votres demande ou exit pour terminer")
		ordre = listen()
	else:
		say_fr("je n'est pas compris")
		break
	ordre = make_ordre(ordre)
	i = 0
	j = 1
	taille = len(ordre)
	
	if taille > 1:
		salutation_temp = find_word(ordre[0],t_salutation)
		if salutation_temp == "ok" and ordre[1] == "Bender":
			say_fr("Bonjour grand maitre")
		elif ordre[0] == "Bender":
			ordre_temp = find_word(ordre[1],t_ordre)
			if ordre_temp == "ok":
				exe_ordre(ordre)
			elif ordre[1] == "exit":
				exit = 1
			else :
				say_fr("ca ne fais pas partie de mon programme")
		else:
			say_en("sorry dude")
			say_fr("ca ne fais pas partie de mon programme")
	elif taille == 1:
		if ordre[0] == "Bender":
			say_fr("que puis-je faire pour vous")
		else:
			say_fr("comment pour, jackadit, vous devez dire")
			say_en("bender")
			say_fr("avant un ordre ou une demande")
	else:
		say_fr("comment pour, jackadit, vous devez dire")
		say_en("bender")
		say_fr("avant un ordre")