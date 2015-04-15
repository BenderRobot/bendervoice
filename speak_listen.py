#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########
import os
import pyaudio
import speech_recognition as sr
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
    		print("pas compris")
		return "pas compris"
	ordre = r.recognize(audio)
	return ordre.encode('utf8')
