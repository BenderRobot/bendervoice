#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########

from make_find_supp import *
from speak_listen import *
from f_search import *
#from f_reveil import *
from f_music import *
from weather import *
from tab import *

################################## Fonction Execute Ordre ################################

def exe_ordre(ordre):
	length = len(ordre)
	say_fr("éxécution")
	if ordre[1] == t_ordre[0] and length > 4 or ordre[1] == t_ordre[1] and length > 4: #cherche
		media = find_word(ordre[3],t_media)
		if media == "false" and length > 4:
			media = find_word(ordre[4],t_media)
		if media == "ok":
			if ordre[3] == t_media[0] or ordre[3] == t_media[1] or ordre[3] == t_media[6]:
				search_web(ordre)
			elif ordre[3] == t_media[2] or ordre[3] == t_media[3]:
				search_wiki(ordre)
			elif ordre[3] == t_media[4]:
				search_youtube(ordre)
			elif ordre[4] == t_media[5]:
				search_cal(ordre)
			### ajouter recherche ###
		else:
			say_fr("je ne connait pas ce media")
	elif ordre[1] == t_ordre[2] and length >= 3 or ordre[1] == t_ordre[3] and length >= 3: #ouvre ou lance
		index = 2
		app = find_word(ordre[index],t_app)
		if app == "false":
			index = 3
			app = find_word(ordre[index],t_app)
		if app == "ok":
			if ordre[index] == t_app[0] or ordre[index] == t_app[2]:
				say_fr("j'ouvre l'application internet")
				os.system('iceweasel www.google.fr')
			elif ordre[index] == t_app[1]:
				length = len(ordre)
				if index == (length - 1):
					music = "false" 
				else:
					index = index + 1
					music = make_str(ordre,index,length)
				f_music(music)
			elif ordre[index] == t_app[3]:
				say_fr("ca ne marche pas encore")
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
	elif ordre[1] == t_ordre[5] and length >= 3 or ordre[1] == t_ordre[6] and length >= 3:
		index = 2
		media = find_word(ordre[index],t_media)
		if media == "false":
			index = 3
			media = find_word(ordre[index],t_media)
			if media == "false":
				index = 4 
				media = find_word(ordre[index],t_media)
		if media == "ok":
			index = index + 1
			ordre = make_str(ordre,index,length)
			check_weather(ordre)
		else:
			say_fr("je ne connait pas ce media")
	elif ordre[1] == t_ordre[7] and length >= 3:
		ordre = make_str(ordre,4,length)
		f_reveil(ordre)
	else:
		say_fr("pas suffisament d'information")

