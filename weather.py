#!/usr/bin/env python
# -*- coding: utf-8 -*-
######### library ##########
import urllib2
import json
from speak_listen import *
from tab import *
######### Weather ##########
def check_weather(ordre):
	f = urllib2.urlopen("http://api.wunderground.com/api/89832eb11f0af9f6/forecast/conditions/lang:FR/q/France/Toulouse.json")
	json_string = f.read()
	parsed_json = json.loads(json_string)
	f.close()

	current_temp = parsed_json['current_observation']['temp_c'] # la température en °C
	current_weather = parsed_json['current_observation']['weather'] # le temps actuel
	humidity = parsed_json['current_observation']['relative_humidity'] # le taux d'humidité en %
	wind_kph = parsed_json['current_observation']['wind_kph'] # la vitesse du vent
	wind_dir = parsed_json['current_observation']['wind_dir'] # l'orientation du vent
	pressure_mb = parsed_json['current_observation']['pressure_mb'] # la pression atmosphérique
	pressure_trend = parsed_json['current_observation']['pressure_trend'] # evolution pression atmosphérique

# Une petite transformation de la tendance atmosphérique
	if pressure_trend == '-':
		pressure_trend = 'en baisse'
	elif pressure_trend == '+':
		pressure_trend = 'en hausse'
	else:
		pressure_trend = 'stable'


	t_weather = [[" "]*11 for _ in range(4)]
# Je récupère les prévisions sous le tag "simpleforecast", en bouclant sur chacune des périodes
	forecast = parsed_json['forecast']['simpleforecast']['forecastday']
	for i in forecast:
		jour		= i['date']['day']        # jour
		mois		= i['date']['month']      # mois
		annee		= i['date']['year']       # année
		jour_sem	= i['date']['weekday']    # jour de la semaine
		period		= i['period']             # période
		tempmax		= i['high']['celsius']    # température maximale
		tempmin		= i['low']['celsius']     # température minimale
		condition	= i['conditions']         # conditions
		pop		= i['pop']                # probabilité de précipitation
		hauteur_precip	= i['qpf_allday']['mm']   # hauteur de précipitation pour la journée
		vent		= i['avewind']['kph']     # vitesse moyenne du vent
		tx_humidite	= i['avehumidity']        # taux d'humidité

		# Je définis chacune de mes 4 périodes
		if period == 1:
			t_weather[0][0] = jour
			t_weather[0][1] = mois
			t_weather[0][2] = annee
			t_weather[0][3] = jour_sem
			t_weather[0][4] = tempmax
			t_weather[0][5] = tempmin
			t_weather[0][6] = condition.encode('utf8')
			t_weather[0][7] = pop
			t_weather[0][8] = hauteur_precip
			t_weather[0][9] = vent
			t_weather[0][10] = tx_humidite
		elif period == 2:
			t_weather[1][0] = jour
			t_weather[1][1] = mois
			t_weather[1][2] = annee
			t_weather[1][3] = jour_sem
			t_weather[1][4] = tempmax
			t_weather[1][5] = tempmin
			t_weather[1][6] = condition.encode('utf8')
			t_weather[1][7] = pop
			t_weather[1][8] = hauteur_precip
			t_weather[1][9] = vent
			t_weather[1][10] = tx_humidite
		elif period == 3:
			t_weather[2][0] = jour
			t_weather[2][1] = mois
			t_weather[2][2] = annee
			t_weather[2][3] = jour_sem
			t_weather[2][4] = tempmax
			t_weather[2][5] = tempmin
			t_weather[2][6] = condition.encode('utf8')
			t_weather[2][7] = pop
			t_weather[2][8] = hauteur_precip
			t_weather[2][9] = vent
			t_weather[2][10] = tx_humidite
		elif period == 4:
			t_weather[3][0] = jour
			t_weather[3][1] = mois
			t_weather[3][2] = annee
			t_weather[3][3] = jour_sem
			t_weather[3][4] = tempmax
			t_weather[3][5] = tempmin
			t_weather[3][6] = condition.encode('utf8')
			t_weather[3][7] = pop
			t_weather[3][8] = hauteur_precip
			t_weather[3][9] = vent
			t_weather[3][10] = tx_humidite

	if "aujourd'hui" in ordre or "moment" in ordre: #aujourd'hui
		say_fr("La météo pour aujourd’hui, " + str(t_weather[0][3]) + " " + str(t_weather[0][0]) + "/" + str(t_weather[0][1]) + "/" + str(t_weather[0][2]) + " :")
		say_fr("En ce moment, " + current_weather.encode('utf8') + ", la température, est de, " + str(current_temp) + " °Celsius, et la pression atmosphérique, " + str(pressure_trend) + ", est de, " + str(pressure_mb) + "mb.")
		say_fr("Les températures irons de " + str(t_weather[0][5]) + "°Celsius, le matin, à " + str(t_weather[0][4]) + "°Celsius, maximum, avec un taux d'humidité de, " + str(t_weather[0][10]) + "% et un vent à " + str(t_weather[0][9]) + " km/heure.")
		if t_weather[0][7] > 0: 
			say_fr("il y a " + str(t_weather[0][7]) + "% de chance, qu'il pleuve et les précipitations est égal à, " + str(t_weather[0][8]) + " millimètre.")
	elif "demain" in ordre: #demain
		say_fr("La météo pour demain, " + str(t_weather[1][3]) + " " + str(t_weather[1][0]) + "/" + str(t_weather[1][1]) + "/" + str(t_weather[1][2]) + " :")
		say_fr(str(t_weather[1][6]) + ", les températures irons de " + str(t_weather[1][5]) + "°Celsius, le matin, à " + str(t_weather[1][4]) + "°Celsius, maximum, avec un taux d'humidité de " + str(t_weather[1][10]) + "% et un vent à, " + str(t_weather[1][9]) + " km/heure")
		if t_weather[1][7] > 0: 
			say_fr("Il y aura " + str(t_weather[1][7]) + "% de chance, qu'il pleuve et les précipitations sera égal à environ; " + str(t_weather[1][8]) + " millimètre.")
	elif "semaine" in ordre:
		i = 0
		say_fr("les prévisions pour les 4 prochain jours sont :")
		while i < 4:
			say_fr(str(t_weather[i][3]) + " " + str(t_weather[i][0]) + "/" + str(t_weather[i][1]) + "/" + str(t_weather[i][2]) + " :")
			say_fr(str(t_weather[i][6]) + ", les températures irons de " + str(t_weather[i][5]) + "°Celsius, le matin, à " + str(t_weather[i][4]) + "°Celsius, maximum, avec un taux d'humidité de " + str(t_weather[i][10]) + "% et un vent à " + str(t_weather[i][9]) + " km/h")
		if t_weather[i][7] > 0: 
			say_fr("Il y aura " + str(t_weather[i][7]) + "% de chance, qu'il pleuve et les précipitations sera égal à environ, " + str(t_weather[i][8]) + " millimètre.")
			i = i + 1
	else:
		print "error weather's date"
