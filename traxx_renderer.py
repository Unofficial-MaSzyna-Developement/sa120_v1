#encoding: UTF-8

from PIL import ImageDraw, ImageFont, Image
from random import random
from datetime import datetime, timedelta, date
from time import gmtime, strftime
from sys import maxint


# definicje kolorow
czarny = (0,0,0)
czarny_gsmr = (25,25,25)
czarny2_gsmr = (10,10,10)
szary_gsmr = (200,200,200)
czarny_diag2 = (20,20,20)
czarny_diag = (0,0,0)
bialy =(255,255,255)
bialy_diag =(255,255,255)
jszary =(218,218,218)
niebieski =(32,96,255)
niebieski_diag =(0,0,255)
ed = (157,145,95)
jasnoniebieski_diag = (128,160,255)
zolty_diag = (255,254,2)


class traxx_renderer(abstractscreenrenderer):
	def __init__(self, lookup_path):
		self.podklad = self.openimage(lookup_path + "ek1")
		lookup_path = lookup_path + "screen/"
		self.ertms = Image.open(lookup_path + "ertms.png")
		self.ertms_tdd = Image.open(lookup_path + "ertms_tdd.png")
		self.diag_1_day = Image.open(lookup_path + "diag_1_day.png")
		self.diag_1_night = Image.open(lookup_path + "diag_1_night.png")
		self.maska  = Image.open(lookup_path + "maska.png")
		self.shp  = Image.open(lookup_path + "shp.png")
		self.pedal  = Image.open(lookup_path + "pedal.png")
		self.ws  = Image.open(lookup_path + "ws.png")
		self.szyna_zbiorcza  = Image.open(lookup_path + "szyna_zbiorcza.png")
		self.drzwi  = Image.open(lookup_path + "drzwi.png")
		
		self.sredni_arial = ImageFont.truetype('./fonts/arialbd.ttf', 34)
		self.maly_arial = ImageFont.truetype('./fonts/arialbd.ttf', 26)
		self.maly_arial20 = ImageFont.truetype('./fonts/arialbd.ttf', 20)
		self.bmaly_arial = ImageFont.truetype('./fonts/arialbd.ttf', 16)
		self.gsmr1 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 22)
		self.gsmr2 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 14)
		self.gsmr3 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 18)
		self.gsmr4 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 80)
		
		self.kilometry = (random()*300000)+5000
		self.last_time_update = 0
		self.dzis = datetime.now().timetuple().tm_yday
		self.rok = datetime.now().year
		self.last_hour = 10
		self.temp = (random()*15) + 20
		self.aktyw = 0		
		self.pasek = 0				
		self.tdd = True # uzyj ekranu TDD ponoc maszynisci czesciej na takim jezdza
		self.shp_flash = True
		
	def _render(self, state):
		dt = 0		
#liczenie pojazdów
		pojazdy = 1
		if (state['unit_no'] == 1):
			pojazdy = 1
		if (state['unit_no'] == 2):
			pojazdy = 2
		if (state['unit_no'] == 3):
			pojazdy = 3
		if (state['unit_no'] == 4):
			pojazdy = 4
		if (state['unit_no'] > 4):
			pojazdy = 4
			
#zmiana kolorów na nocne
		global czarny_diag
		global niebieski_diag
		if (state['universal3']==1):
			czarny_diag = (255,255,255)
			# bialy_diag =(255,255,255)
			niebieski_diag =(0,0,132)
			# jasnoniebieski_diag = (133,128,255)
			# zolty_diag = (255,254,2)
			czarny_gsmr = (200,200,200)
			szary_gsmr = (25,25,25)
			
		else:
			czarny_diag = (0,0,0)
			niebieski_diag =(0,0,255)
			czarny_gsmr = (25,25,25)
			szary_gsmr = (200,200,200)
		# kopia obrazka na potrzeby tego jednego renderowania
		obrazek = self.podklad.copy()
		# chcemy rysowac po teksturze pulpitu
		draw = ImageDraw.Draw(obrazek)
		
#Prędkość
		speed = float(state['velocity'])
		if speed > 180:
			speed = 180
#czas
		if state['seconds'] != self.last_time_update:
			dt = state['seconds'] - self.last_time_update
			if dt < 0:
				dt+=60
			self.kilometry += dt*speed * 0.0002778
			self.last_time_update = state['seconds']
		if state['hours']<10:
			godz = "0" + str(state['hours'])
		else:
			godz = str(state['hours'])
		if state['minutes']<10:
			min = "0" + str(state['minutes'])
		else:
			min = str(state['minutes'])
		if state['seconds']<10:
			sec = "0" +str(state['seconds'])
		else:
			sec = str(state['seconds'])
		
		
#data
		if self.last_hour == 23 and state['hours'] == 0:
			self.dzis = self.dzis+1 # wlasnie wybila polnoc
		self.last_hour = state['hours']
		data = datetime(self.rok, 1, 1) + timedelta(self.dzis - 1)
		dzien = datetime.weekday(data)
		data = data.strftime("%d.%m.%Y")
		DayL = ['Pn','Wt',u'Śr','Cz','Pt','So','Nd']
		
		code = (state['car_name1'])[:123]	
		
#ERTMS------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		if state['eimp_c1_batt']==1:
			self.aktyw += dt			
			if (self.aktyw < 80):				
				if (self.aktyw > 10):			
					draw.rectangle(((0,0),(1280,2048)), czarny_diag2)	
				if (self.aktyw > 35):			
					draw.rectangle(((0,0),(1280,2048)), jszary)					
				if (self.aktyw > 60):			
					draw.rectangle(((0,0),(1280,2048)), jszary)		
					self.print_center(draw, u'Initialisierung', 690, 1275, self.sredni_arial, czarny_diag2)	
					self.print_center(draw, u'Fahrzeugnr.:' + code, 690, 1488, self.sredni_arial, czarny_diag2)								
					draw.rectangle(((446,1322),(954,1381)), niebieski)		
					draw.rectangle(((450,1326),(950,1377)), jszary)	
					
					
					self.print_center(draw, u'Initialisierung', 690, 1275-983, self.sredni_arial, czarny_diag2)	
					self.print_center(draw, u'Fahrzeugnr.:' + code, 690, 1488-983, self.sredni_arial, czarny_diag2)								
					draw.rectangle(((446,1322-983),(954,1381-983)), niebieski)		
					draw.rectangle(((450,1326-983),(950,1377-983)), jszary)								
					self.pasek += dt	
					draw.rectangle((446,1322,446 + 5 * self.pasek,1381), fill=niebieski)		
					draw.rectangle((446,1322-983,446 + 5 * self.pasek,1381-983), fill=niebieski)							
					if (self.pasek > 15):					
						draw.rectangle(((446,1322),(954,1381)), niebieski)	
						draw.rectangle(((446,1322-983),(954,1381-983)), niebieski)		
			else:
				if self.tdd:
					obrazek.paste(self.ertms_tdd,(134,1038),self.ertms_tdd)
				else:
					obrazek.paste(self.ertms,(134,1038),self.ertms)
		#ERTMS godzina
				draw.text((576,1045), godz +":"+ min +":"+ sec, fill=jszary, font=self.sredni_arial)

		#ERTMS prędkościomierz
				draw.ellipse([(431, 1249), (521, 1339)], fill=bialy)
				rotate = speed * 270 / 180 + 45
				rad =  radians(rotate)
				srodek_tacho = (476, 1294)
				point = (-10,37)
				p1 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
				point = (-10,137)
				p2 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
				point = (-4,145)
				p3 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
				point = (-4,187)
				p4 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
				point = (10,37)
				p8 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
				point = (10,137)
				p7 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
				point = (4,145)
				p6 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
				point = (4,187)
				p5 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
				draw.polygon([p1,p2,p3,p4,p5,p6,p7,p8],fill=bialy)

				self.print_fixed_with(draw, (" " * (3 - len('%d' % speed))) + ('%d' % speed), (454, 1278), 3, self.sredni_arial, czarny)

		#ERTMS tempomat
				tempomat = state['new_speed']
				if tempomat > 0:
					rotate = tempomat * 270 / 180 - 135
					rad =  radians(rotate)
					srodek = (476, 1294)
					point = (0,-193)
					p1 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
					point = (-12,-205)
					p2 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
					point = (0,-217)
					p3 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
					point = (12,-205)
					p4 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
					draw.polygon([p1,p2,p3,p4],fill=zolty_diag)


		#ERTMS siła pociągowa/hamowania

				if self.tdd:
					# ekran TDD

					# numer lokomotywy
					raw_number = state["name"].split("'")[0][-3:]
					draw.text((852,1039), "285\n" + raw_number, font=self.maly_arial20, fill=jszary)

					# obroty silnika
					obr = state['diesel_param_1_enrot']
					if obr>2200:
						obr=2200
					if obr > 0:
						y = 1411 - (obr * 306 / 2200)
						draw.rectangle(((826,1411),(903,y)), fill=niebieski)

					if obr>500:
						draw.rectangle(((826,1421),(903,1444)), fill=niebieski)
						draw.text((830,1422), u'GE zał.', font=self.maly_arial20, fill=bialy_diag)
					else:
						draw.text((828,1422), u'GE wył.', font=self.maly_arial20, fill=bialy_diag)

					# temperatura oleju(?)
					temp = state['diesel_param_1_water_temp']
					if temp<0:
						temp=0
					if temp>120:
						temp=120
					if temp > 0:
						y = 1447 - (temp * 342 / 120)
						draw.rectangle(((993,1447),(1071,y)), fill=niebieski)

					#siła pociągowa
					#frt = state['eimp_c1_frt']
					frt = state['tractionforce'] / 1000
					#siła hamowania
					frb = state['eimp_c1_frb']
					if frt>300:
						frt=300
					if frb>300:
						frb=300
					if frt > 0:
						y = 1447 - (frt * 342 / 300)
						draw.rectangle(((1174,1447),(1246,y)), fill=niebieski)
					elif frb > 0:
						y = 1447 - (frb * 342 / 300)
						draw.rectangle(((1174,1447),(1246,y)), fill=ed)

					#siła zadana
					pd = state['eimp_t_pd']
					color = niebieski
					if pd < 0:
						pd = -pd / 2
						color = ed
					x = 1172
					y = 1447 - (pd * 342 / 1)
					p1 = (x, y)
					p2 = (x - 25, y + 8)
					p3 = (x - 20, y)
					p4 = (x - 25, y - 8)
					draw.polygon([p1, p2, p3, p4], fill = color)

					# stan paliwa i cisnienie w ZG
					draw.rectangle(((832, 1463), (892, 1492)), fill = bialy)
					x = 882 - draw.textsize("2169", font = self.maly_arial20)[0]
					draw.text((x, 1467), "2169", font = self.maly_arial20, fill = czarny)

					hbl = state['eimp_pn1_sp']
					draw.rectangle(((1102, 1463), (1162, 1492)), fill = niebieski)
					x = 1152 - draw.textsize("{:.1f}".format(hbl), font = self.maly_arial20)[0]
					draw.text((x, 1467), "{:.1f}".format(hbl), font = self.maly_arial20, fill = bialy)

					# kreski renderowane nad paskami
					color = (197, 193, 198)
					draw.rectangle(((824, 1138), (845, 1139)), fill = color)
					draw.rectangle(((857, 1138), (888, 1139)), fill = color)
					draw.rectangle(((900, 1138), (905, 1139)), fill = color)
					draw.rectangle(((991, 1333), (1011, 1334)), fill = color)
					draw.rectangle(((1025, 1333), (1054, 1334)), fill = color)
					draw.rectangle(((1067, 1333), (1073, 1334)), fill = color)
					draw.rectangle(((991, 1160), (1011, 1161)), fill = color)
					draw.rectangle(((1025, 1160), (1054, 1161)), fill = color)
					draw.rectangle(((1067, 1160), (1073, 1161)), fill = color)
					draw.rectangle(((991, 1153), (1011, 1154)), fill = color)
					draw.rectangle(((1025, 1153), (1054, 1154)), fill = color)
					draw.rectangle(((1067, 1153), (1073, 1154)), fill = color)



					#status

					msg = ""
					color = jasnoniebieski_diag
					msg_color = bialy

					# zrodlo: https://youtu.be/x-hb8zEG_Vk?t=169
					if state['cabactive'] != state['cab']:
						msg = u'Zajmij kabinę'
					elif not state['linebreaker']:
						msg = u'Uruchom silnik wys.'
					elif state['eimp_c1_conv'] == 0:						
						msg = u'Załącz generator'
					elif (state['eimp_c1_ms'] == 0 and state['main_ctrl_actual_pos'] !=0):
						msg = u'Ustaw nastawnik jazdy na 0'
					elif state['direction'] == 0:
						msg = u'Wybierz kierunek jazdy'
					elif state['brakes_1_spring_active']:
						msg = u'Zwolnij Hamulec sprężynowy'
					elif state['localbrake_pos'] > 0:
						msg = u'Niezwolniony ham. pomocniczy'
					elif state['dir_brake'] or state['indir_brake']:
						msg = u'Blokada trakcji'
						color = zolty_diag
						msg_color = czarny

					if msg != "":
						draw.rectangle(((729,1501),(1063,1548)), fill=color)
						self.print_center(draw, msg, 896, 1525, self.maly_arial20, msg_color)

				else:
					# stary ekran z kolkiem mocy (CCD)

					#siła pociągowa
					frt = (state['eimp_c1_frt'])
					if not -maxint-1 <= frt <= maxint:
						frt = (frt + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
					end = int(frt / 2 - 90)
					draw.pieslice((771,1071,1220, 1520), -90, end, fill=niebieski)
					#siła hamowania
					frb = (state['eimp_c1_frb'])
					if not -maxint-1 <= frb <= maxint:
						frb = (frb + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
					end = int(-frb - 90)
					draw.pieslice((771,1071,1220, 1520), end, -90 , fill=ed)

					obrazek.paste(self.maska,(730,1041),self.maska)

					#siła zadana
					# fd = state['eimp_t_fd']
					# if (fd<0):
						# fd=fd*2
					# rotate = fd * 70 / 140
					# if (rotate>140 and fd>0):
						# rotate=140
					# if (rotate<-140 and fd<0):
						# rotate=-140
					pd = state['eimp_t_pd']
					if (abs(speed)<0.01):
						pd = 0
					rotate = pd * 150
					if (rotate>140 and pd>0):
						rotate=140
					if (rotate<-140 and pd<0):
						rotate=-140
					rad =  radians(rotate)
					srodek = (995, 1295)
					point = (0,-220)
					p1 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
					point = (-13,-249)
					p2 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
					point = (13,-249)
					p3 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
					draw.polygon([p1,p2,p3],fill=bialy)



		#ERTMS Ikonki
				if (state['shp']):
					if self.shp_flash:
						obrazek.paste(self.shp,(303,1551),self.shp)
					self.shp_flash = not self.shp_flash
				if (state['ca']):
					obrazek.paste(self.pedal,(1155,1551),self.pedal)
				if (state['eimp_c1_ms']==0):
					obrazek.paste(self.szyna_zbiorcza,(729,1551),self.szyna_zbiorcza)
				if (state['eimp_c1_heat']==0):
					obrazek.paste(self.ws,(801,1551),self.ws)
				if (state['doors_2']==0 and state['doors_no_2']>0):
					obrazek.paste(self.drzwi,(942,1551),self.drzwi)

	#Ekran diagnostyczny--------------------------------------------------------------------------------------------------------------------------------------------------------------------
				pojazdy = 1
				# nie ma ekranow dla trakcji wielokrotnej
				if (pojazdy ==1):
					if (state['universal3']==0):
						obrazek.paste(self.diag_1_day,(130,54),self.diag_1_day)
					if (state['universal3']==1):
						obrazek.paste(self.diag_1_night,(130,54),self.diag_1_night)
		#diag data
				draw.text((1021,60), DayL[dzien] + ", " + data, fill=czarny_diag, font=self.sredni_arial)
		#diag nr pociągu
				trainnumber = state['trainnumber']
				if ((state['trainnumber'] == 'none') or (state['trainnumber'] == 'rozklad') ):
					trainnumber = ' '
				draw.text((1112,387), trainnumber, fill=czarny_diag, font=self.maly_arial)
		#diag długość składu
				#distance_counter = state['distance_counter']

				#if (distance_counter > 0):
				#	draw.text((1026,473), str('%d' % (state['train_length'] - distance_counter)) + ' m', fill=zolty_diag, font=self.sredni_arial)
		#diag ilosc paliwa
				x = 1200 - draw.textsize("2169", font = self.sredni_arial)[0]
				draw.text((x, 567), "2169", font = self.sredni_arial, fill = czarny_diag)
		#diag zasieg
				x = 1185 - draw.textsize("853", font = self.sredni_arial)[0]
				draw.text((x, 664), "853", font = self.sredni_arial, fill = czarny_diag)
		#diag zegarek
				#obroty wskazówek w radianach
				sekundy = radians((state['seconds']*6))
				minuty = radians((state['minutes']*6))
				godziny = radians((state['hours']*30 + state['minutes']*0.5)) #składowa minutowa dla płynnego ruchu
				srodek = (1130, 242)
				#długości wskazówek
				r_s = 105
				r_m = 98
				r_g = 82
				#punkty końcowe
				k_s = (srodek[0]+(r_s*sin(sekundy)), srodek[1]-(r_s*cos(sekundy)))
				k_m = (srodek[0]+(r_m*sin(minuty)), srodek[1]-(r_m*cos(minuty)))
				k_g = (srodek[0]+(r_g*sin(godziny)), srodek[1]-(r_g*cos(godziny)))
				p_s = (srodek[0]+(7*(-sin(sekundy))), srodek[1]-(7*(-cos(sekundy))))
				p_m = (srodek[0]+(7*(-sin(minuty))), srodek[1]-(7*(-cos(minuty))))
				p_g = (srodek[0]+(7*(-sin(godziny))), srodek[1]-(7*(-cos(godziny))))
				#rysowanie wskazówek
				draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=czarny_diag, width=2)
				draw.line((p_m[0], p_m[1],k_m[0], k_m[1]),fill=czarny_diag, width=4)
				draw.line((p_g[0], p_g[1],k_g[0], k_g[1]),fill=czarny_diag, width=8)


		#diag status3
				msg = ""
				color = jasnoniebieski_diag
				msg_color = bialy

				# zrodlo: https://youtu.be/x-hb8zEG_Vk?t=169
				if state['cabactive'] != state['cab']:
					msg = u'Zajmij kabinę'
				elif not state['linebreaker']:
					msg = u'Uruchom silnik wys.'
				elif state['eimp_c1_conv'] == 0:		
					msg = u'Załącz generator'
				elif (state['eimp_c1_ms'] == 0 and state['main_ctrl_actual_pos'] !=0):
					msg = u'Ustaw nastawnik jazdy na 0'
				elif state['direction'] == 0:
					msg = u'Wybierz kierunek jazdy'
				elif state['brakes_1_spring_active']:
					msg = u'Zwolnij Hamulec sprężynowy'
				elif state['localbrake_pos'] > 0:
					msg = u'Niezwolniony ham. pomocniczy'
				elif state['dir_brake'] or state['indir_brake']:
					msg = u'Blokada trakcji'
					color = zolty_diag
					msg_color = czarny

				if msg != "":
					draw.rectangle(((558,720),(969,784)), fill=color)
					self.print_center(draw, msg, 763, 752, self.maly_arial, msg_color)

		#diag slupki 1
				if (pojazdy ==1):
					# obroty silnika
					obr = state['diesel_param_1_enrot']
					if obr>2200:
						obr=2200
					if obr > 0:
						y = 553 - (obr * 418 / 2200)
						draw.rectangle(((221,553),(295,y)), fill=niebieski)

					if obr>500:
						draw.rectangle(((221,574),(295,613)), fill=niebieski)
						draw.text((226,581), u'GE zał', font=self.maly_arial20, fill=bialy)
					else:
						draw.text((223,581), u'GE wył', font=self.maly_arial20, fill=czarny_diag)

					# temperatura oleju(?)
					temp = state['diesel_param_1_water_temp']
					if temp<0:
						temp=0
					if temp>120:
						temp=120
					if temp > 0:
						y = 613 - (temp * 478 / 120)
						draw.rectangle(((389,613),(463,y)), fill=niebieski)

					#siła pociągowa
					#frt = state['eimp_c1_frt']
					frt = state['tractionforce'] / 1000
					#siła hamowania
					frb = state['eimp_c1_frb']
					if frt>300:
						frt=300
					if frb>300:
						frb=300
					if frt > 0:
						y = 612 - (frt * 475 / 300)
						draw.rectangle(((555,612),(629,y)), fill=niebieski)
					elif frb > 0:
						y = 612 - (frb * 475 / 300)
						draw.rectangle(((555,612),(629,y)), fill=ed)

					#siła zadana
					pd = state['eimp_t_pd']
					color = niebieski
					if pd < 0:
						pd = -pd / 2
						color = ed
					x = 553
					y = 612 - (pd * 475 / 1)
					p1 = (x, y)
					p2 = (x - 36, y + 8)
					p3 = (x - 28, y)
					p4 = (x - 36, y - 8)
					draw.polygon([p1, p2, p3, p4], fill = color)

					#cisnienie w ZG
					hbl = state['eimp_pn1_sp']
					if hbl<0:
						hbl=0
					if hbl>13:
						hbl=13
					if hbl > 0:
						y = 612 - (hbl * 474 / 13)
						draw.rectangle(((784,612),(858,y)), fill=niebieski)

					# kreski renderowane nad paskami
					color = czarny_diag
					draw.rectangle(((207, 180), (238, 182)), fill = color)
					draw.rectangle(((250, 180), (282, 182)), fill = color)
					draw.rectangle(((292, 180), (298, 182)), fill = color)
					draw.rectangle(((376, 203), (406, 205)), fill = color)
					draw.rectangle(((418, 203), (448, 205)), fill = color)
					draw.rectangle(((459, 203), (466, 205)), fill = color)
					draw.rectangle(((376, 212), (406, 214)), fill = color)
					draw.rectangle(((418, 212), (448, 214)), fill = color)
					draw.rectangle(((459, 212), (466, 214)), fill = color)
					draw.rectangle(((376, 455), (406, 457)), fill = color)
					draw.rectangle(((418, 455), (448, 457)), fill = color)
					draw.rectangle(((459, 455), (466, 457)), fill = color)
					draw.rectangle(((765, 245), (803, 247)), fill = color)
					draw.rectangle(((815, 245), (845, 247)), fill = color)
					draw.rectangle(((856, 245), (861, 247)), fill = color)

						
		else:
			self.aktyw = 0
			self.pasek = 0		
		return obrazek
