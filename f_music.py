#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########

from speak_listen import *
from make_find_supp import *
from tab import *

################################## Fonction Application ################################

def f_music(ordre):
	say_fr("je lance la musique")
	#cmd = [""]*3
	if ordre == "false":
		sortie = os.popen("ls /root/Musique/", "r").read()
		sortie = "".join(sortie)
		sortie = make_say(sortie)
		say_fr("j'ai trouvé plusieurs artistes :")
		print sortie
		say_fr("tu veux écouter quel artiste?")
		artiste = sub_menu()
		print artiste
		test_artiste = make_ordre(artiste)
		test = find_word("tous",test_artiste)
		print test_artiste
		print test
		if artiste != 0 and test != "ok" or artiste != "exit" and test != "ok":
			say_fr("ok pour du " + str(artiste))
			cmd_artiste = make_find(artiste)
			sortie = os.popen("ls /root/Musique/" + cmd_artiste, "r").read()
			sortie = "".join(sortie)
			sortie = make_say(sortie)
			say_fr("album de " + artiste + " :")
			say_fr(sortie)
			say_fr("tu veux ecouter quel album?")
			album = sub_menu()
			print album
			test_album = make_ordre(album)
			test = find_word("tous",test_album)
			if artiste != 0 and test != "ok" or artiste != "exit" and test != "ok":
				say_fr("ok pour l'album " + str(album))
				cmd_album = make_find(album)
				os.system("nohup vlc /root/Musique/" + cmd_artiste + "/" + cmd_album + "/ >/dev/null 2>&1 &")
			elif test == "ok":
				say_fr("ok pour tous les l'albums de " + str(artiste))
				os.system("nohup vlc /root/Musique/" + cmd_artiste + "/ >/dev/null 2>&1 &")
		elif test == "ok":
			say_fr("ok je joue tous les artistes")
			os.system("nohup vlc /root/Musique/ >/dev/null 2>&1 &")
	elif ordre != "false":
		i = 0
		j = 0
		count = 0
		print ordre
		test = [0]*2
		t_artiste = [""]*2
		t_album = [""]*10
		ordre = make_ordre(ordre)
		test[0] = find_word("artiste",ordre)
		test[1] = find_word("album",ordre)
		if test[0] == "ok" and test[1] == "ok":
			while i < len(ordre):
				if ordre[i] == "artiste":
					i = i + 1
					while ordre[i] != "album":
						t_artiste[j] = ordre[i]
						j = j + 1
						i = i + 1
				elif ordre[i] == "album":
					j = 0
					i = i + 1
					while i < len(ordre):
						t_album[j] = ordre[i]
						j = j + 1
						i = i + 1
						count = count + 1
					break
				else:
					say_fr("je n'est pas compris l'artistee")
					break
			artiste = make_str(t_artiste,0,len(t_artiste))
			album = make_str(t_album,0,count)
			cmd_artiste = make_find(artiste)
			cmd_album = make_find(album)
			say_fr("ok je lance l'album " + album + " de " + artiste) 
			os.system("nohup vlc /root/Musique/" + cmd_artiste + "/" + cmd_album + "/ >/dev/null 2>&1 &")
		elif test[0] == "ok" and test[1] == "false":
			while i < len(ordre):
				if ordre[i] == "artiste":
					i = i + 1
					while i < len(ordre):
						t_artiste[j] = ordre[i]
						j = j + 1
						i = i + 1
			artiste = make_str(t_artiste,0,len(t_artiste))
			say_fr("ok pour du " + str(artiste))
			cmd_artiste = make_find(artiste)
			sortie = os.popen("ls /root/Musique/" + cmd_artiste, "r").read()
			sortie = "".join(sortie)
			sortie = make_say(sortie)
			say_fr("album :")
			say_fr(sortie)
			say_fr("tu veux écouter quel album?")
			album = sub_menu()
			print album
			test_album = make_ordre(album)
			test = find_word("tous",test_album)
			if artiste != 0 and test != "ok" or artiste != "exit" and test != "ok":
				say_fr("ok pour l'album " + str(album))
				cmd_album = make_find(album)
				os.system("nohup vlc /root/Musique/" + cmd_artiste + "/" + cmd_album + "/ >/dev/null 2>&1 &")
			elif test == "ok":
				say_fr("ok pour tous les l'albums de " + str(artiste))
				os.system("nohup vlc /root/Musique/" + cmd_artiste + "/ >/dev/null 2>&1 &")
		else:
			print "pour que je comprenne votre choix dite 'artiste' puis son nom suivie de 'album' et le nom de l'album voulu"
