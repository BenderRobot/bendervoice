#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########

import os
import sys
import time
import urllib
import pyaudio
import datetime
import wikipedia
import json as m_json
import speech_recognition as sr
from make_find_supp import *
from speak_listen import *
from exec_ordre import *
from tab import *
from weather import *

################################## Fonction Main ################################
choix = "null"
exit = 0
say_en("I'm Bender!")
say_fr("Tu veux quoi, l'organic?")
while exit == 0:
	
	print("################### Menu Principal ###################")
	print("pour faire une demande ecrite, tapez le mot : < text >")
	print("pour faire une demande oral, tapez le mot : < speech >")
	while choix != "text" or choix != "speech":
		choix = raw_input("entre ton  choix : ")
		print choix
		print("INFO: Commence ta phrase par Bender suivie de ta demande ou exit pour terminer")
		if choix == "text" or choix == "speech":
			break
	if choix == "text":
		ordre = raw_input("entre ta demande : ")
	elif choix == "speech":
		ordre = listen()
	else:
		say_fr("je n'est pas compris")
	ordre = make_ordre(ordre)
	i = 0
	j = 1
	taille = len(ordre)
	
	if taille > 1:
		salutation_temp = find_word(ordre[0],t_salutation)
		if salutation_temp == "ok" and ordre[1].lower() == "bender":
			say_fr("Bonjour Benjamin")
			check = make_ordre("Bender cherche sur mon agenda aujourd'hui")
			exe_ordre(check)
			check = make_ordre("Bender quel temps fais t'il aujourd'hui")
			exe_ordre(check)
		elif ordre[0].lower() == "bender":
			ordre_temp = find_word(ordre[1],t_ordre)
			if ordre_temp == "ok":
				exe_ordre(ordre)
			elif ordre[1] == "exit":
				exit = 1
			else :
				say_fr("ca ne fais pas partie de mon programme")
		else:
			say_fr("ca ne fais pas partie de mon programme else")
	elif taille == 1:
		if ordre[0] == "Bender":
			say_fr("que puis-je faire pour toi")
		else:
			say_fr("comment pour, jackadit, tu dois dire")
			say_en("bender")
			say_fr("avant un ordre ou une demande")
	else:
		say_fr("comment pour, jackadit, tu dois dire")
		say_en("bender")
		say_fr("avant un ordre")
