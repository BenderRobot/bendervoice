#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########
import time
import datetime
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
	
	return "false"

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
		 
def supp_spec(t_char):
	new_t_char = [" "]*(len(t_char))
	length = len(t_char)
	i = 0
	j = 0
	while j <= (length-1):
		if t_char[j] == '[':
			j = j + 1
		elif t_char[j] == ']':
			j = j + 1
		elif t_char[j] == '{':
			j = j + 1
		elif t_char[j] == '}':
			j = j + 1
		elif t_char[j] == ':':
			j = j + 1
		elif t_char[j] == ',':
			j = j + 1
		elif t_char[j] == 'u':
			j = j + 1
			if t_char[j] == "'":
				j = j + 1
			else:
				j + j - 1
		elif t_char[j] == "'":
			j = j + 1
			if t_char[j] == " ":
				j = j - 1
			else:
				j + j - 1
		else:
			new_t_char[i] = t_char[j]
			j = j + 1
			i = i + 1
	return "".join(new_t_char)

def make_str(ordre,index,length): # decoupe un tableau de string a partir de l'argument "index" a "length"
	request = [0]*(((length - index) * 2) - 1)
	j = 0
	while index <= (length-1):
		request[j] = ordre[index]
		index = index + 1
		j = j + 1
		if j < len(request):
			request[j] = " "
			j = j + 1
	return "".join(request)

def make_ordre(ordre): # construit un tableau de string a partir du tableau de char 
	space_count = 0
	count_char = 0
	length = 0
	space = 0
	i = 0
	j = 0
	k = 0
	z = 0
	while i < len(ordre):
		if ordre[i] == " " and space == 0:
			space_count = space_count + 1
			space = 1
			i = i + 1
		else:
			space = 0
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
		if z < len(ordre) and i < length:
			if ordre[z] == " ":
				z = z + 1
		k = 0
	return new_ordre

def make_date(index,index2):
	now = datetime.datetime.now()
	from_day = 0
	to_day = 0
	from_month = 0
	to_month = 0	
	date = [0]*2
	if index == 0 and index2 == "false": # aujourd'hui
		from_day = 0
		to_day = 0
	elif index == 1 and index2 == "false": # demain
		from_day = 1
		to_day = 1
	elif index == 1 and index2 == 4: # apres demain
		from_day = 2
		to_day = 2
	elif index == 2 and index2 == 2 or index == 2 and index2 == "false": # ce weekend
		day = time.strftime('%A',time.localtime())
		if day == "Sunday":
			from_day = -1
			to_day = 0
		elif day == "Monday":
			from_day = 5
			to_day = 6
		elif day == "Tuesday":
			from_day = 4
			to_day = 5
		elif day == "Wednesday":
			from_day = 3
			to_day = 4
		elif day == "Thursday":
			from_day = 2
			to_day = 3
		elif day == "Friday":
			from_day = 1
			to_day = 2
		elif day == "Saturday":
			from_day = 0
			to_day = 1
	elif index == 2 and index2 == 0: # le weekend prochain
		day = time.strftime('%A',time.localtime())
		if day == "Sunday":
			from_day = 6
			to_day = 7
		elif day == "Monday":
			from_day = 12
			to_day = 13
		elif day == "Tuesday":
			from_day = 11
			to_day = 12
		elif day == "Wednesday":
			from_day = 10
			to_day = 11
		elif day == "Thursday":
			from_day = 9
			to_day = 10
		elif day == "Friday":
			from_day = 8
			to_day = 9
		elif day == "Saturday":
			from_day = 7
			to_day = 8
	elif index == 3 and index2 == 3 or index == 3 and index2 == "false": # cette semaine
		day = time.strftime('%A',time.localtime())
		if day == "Sunday":
			from_day = 0
			to_day = 0
		elif day == "Monday":
			from_day = 0
			to_day = 6
		elif day == "Tuesday":
			from_day = -1
			to_day = 5
		elif day == "Wednesday":
			from_day = -2
			to_day = 4
		elif day == "Thursday":
			from_day = -3
			to_day = 3
		elif day == "Friday":
			from_day = -4
			to_day = 2
		elif day == "Saturday":
			from_day = -5
			to_day = 1
	elif index == 3 and index2 == 1: # la semaine prochaine
		day = time.strftime('%A',time.localtime())
		if day == "Sunday":
			from_day = 1
			to_day = 7
		elif day == "Monday":
			from_day = 7
			to_day = 13
		elif day == "Tuesday":
			from_day = 6
			to_day = 12
		elif day == "Wednesday":
			from_day = 5
			to_day = 11
		elif day == "Thursday":
			from_day = 4
			to_day = 10
		elif day == "Friday":
			from_day = 3
			to_day = 9
		elif day == "Saturday":
			from_day = 2
			to_day = 8
	elif index == 4 and index2 == 2 or index == 4 and index2 == "false": # ce mois
		from_day = -now.day + 1
		to_day = -now.day + 1
		from_month = 0
		to_month = 1		
	elif index == 4 and index2 == 0: # mois prochain
		from_day = -now.day + 1
		to_day = -now.day + 1
		from_month = 1
		to_month = 2
	date[0] = datetime.datetime(now.year, now.month + from_month, now.day + from_day)
	date[1] = datetime.datetime(now.year, now.month + to_month, now.day + to_day)
	#print date
	return date

def make_cal(event):
	i = 0
	count_event = 0
	while i < len(event):
		if event[i] == "startDate":
			count_event = count_event + 1
			i = i + 1
		else:
			i = i + 1
	i = 0
	j = 0
	k = 0
	l = 0
	t_event = [[" "]*3 for _ in range(count_event)]
	t_cut = [""]*11
	while j < count_event:
		while k < len(event):
			if event[k] == "startDate":
				i = 0
				t_cut[i] = "de "
				i = i + 1
				k = k + 5
				t_cut[i] = event[k]
				k = k + 1
				i = i + 1
				t_cut[i] = " heures "
				i = i + 1
				t_cut[i] = event[k]
				k = k - 2
				i = i + 1
				t_cut[i] = ", le "
				i = i + 1
				t_cut[i] = event[k]
				k = k - 1
				i = i + 1
				t_cut[i] = "/"
				i = i + 1
				t_cut[i] = event[k]
				k = k - 1
				i = i + 1
				t_cut[i] = "/"
				i = i + 1
				t_cut[i] = event[k]
				t_event[j][l] = "".join(t_cut)
				l = l + 1
				k = k + 6
			elif event[k] == "endDate":
				i = 0
				t_cut[i] = "a "
				i = i + 1
				k = k + 5
				t_cut[i] = event[k]
				k = k + 1
				i = i + 1
				t_cut[i] = " heures "
				i = i + 1
				t_cut[i] = event[k]
				k = k - 2
				i = i + 1
				t_cut[i] = ", le "
				i = i + 1
				t_cut[i] = event[k]
				k = k - 1
				i = i + 1
				t_cut[i] = "/"
				i = i + 1
				t_cut[i] = event[k]
				k = k - 1
				i = i + 1
				t_cut[i] = "/"
				i = i + 1
				t_cut[i] = event[k]
				t_event[j][l] = "".join(t_cut)
				l = l + 1
				k = k + 6
			elif event[k] == "title":
				k = k + 1
				i = 0
				for i in range(len(t_cut)):
					t_cut[i] = " "
				i = 0
				while event[k] != "localEndDate":
					t_cut[i] = event[k]
					i = i + 1
					t_cut[i] = " "
					i = i + 1
					k = k + 1
					if event[k] == " ":
						k = k + 1
						if event[k] == "localEndDate":
							break
						else:
							k = k - 1
				encode = "".join(t_cut)
				t_event[j][l] = encode
				l = 0
				break
			else:
				k = k + 1
		j = j + 1
	return t_event

def make_find(ordre):
	i = 0
	space_count = 0
	while i < len(ordre):
		if ordre[i] == " ":
			space_count = space_count + 1
			i = i + 1
		else:
			i = i + 1
	length = space_count + len(ordre)
	new_ordre = [" "]*length
	i = 0
	j = 0
	while i < len(ordre):
		if ordre[i] == " ":
			new_ordre[j] = "\\"
			j = j + 1
			new_ordre[j] = ordre[i]
			i = i + 1
			j = j + 1
		else:
			new_ordre[j] = ordre[i]
			i = i + 1
			j = j + 1
	#print new_ordre	
	return "".join(new_ordre)

def make_say(string):
	new_string = [" "]*(len(string))
	length = len(string)
	i = 0
	j = 0
	while j < length:
		if string[j] == '\n':
			new_string[i] = "; "
			j = j + 1
			i = i + 1
		else:
			new_string[i] = string[j]
			j = j + 1
			i = i + 1
	return "".join(new_string)
			
def sub_menu(): # affiche un sous-menu pour choisir une action dans une fonction
	ordre = 0
	while ordre == 0:
		choix = raw_input("choix par < text > ou < speech > : ")
		if choix == "text":
			ordre = raw_input("tape ta selection : ")
		elif choix == "speech":
			print("parle maintenant")
			ordre = listen()
		elif choix == "exit":
			say_fr("retour au menu principale")
			ordre = "exit"
		else:
			say_fr("je n'est pas compris")
			ordre = 0
	return str(ordre)
