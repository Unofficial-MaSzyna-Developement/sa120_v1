#encoding: UTF-8

import math
from PIL import ImageDraw, ImageFont, Image
from random import random, randint
from datetime import datetime, timedelta
from time import gmtime, strftime

class screen_en57al(abstractscreenrenderer):
	def __init__(self, lookup_path):
		# definicje kolorow
		self.czarny = (0,0,0)
		self.blekitny=(155,249,255)
		self.niebieski=(196,236,255)
		self.szary=(51,51,51)
		self.szary2=(78,77,71)		
		self.zielony=(58,202,27)
		self.czerwony=(255,0,0)
		self.zolty=(233,246,6)
		self.bialy=(255,255,255)
		self.pomaranczowy = (255,128,40)
		self.niebieski_boot = (71,121,176)
		self.zielonastrzalka = (0,255,0)	
		self.niebieskastrzalka = (0,255,255)		
		self.zoltastrzalka = (255,255,0)			
		# wczytanie obrazka
		self.tlo = self.openimage("./dynamic/pkp/en57akl_v1/cab/ekran")
		lookup_path = lookup_path + "screen/"
		self.podklad = None
		self.ramki1  = Image.open(lookup_path + "ramki1.png")
		self.ramki2  = Image.open(lookup_path + "ramki2.png")
		self.ramki3  = Image.open(lookup_path + "ramki3.png")
		self.ezt  = Image.open(lookup_path + "ezt.png")
		self.WN_off  = Image.open(lookup_path + "WN_off.png")
		self.WS_off  = Image.open(lookup_path + "WS_off.png")
		self.WS_gotowosc  = Image.open(lookup_path + "WS_gotowosc.png")
		self.przetwornica_off  = Image.open(lookup_path + "przetwornica_off.png")
		self.bateria_off  = Image.open(lookup_path + "bateria_off.png")
		self.falownik_off  = Image.open(lookup_path + "falownik_off.png")
		self.sprezarka_off  = Image.open(lookup_path + "sprezarka_off.png")
		self.M1M2_off  = Image.open(lookup_path + "M1M2_off.png")
		self.M3M4_off  = Image.open(lookup_path + "M3M4_off.png")
		self.WN_on  = Image.open(lookup_path + "WN_on.png")
		self.WS_on  = Image.open(lookup_path + "WS_on.png")
		self.przetwornica_on  = Image.open(lookup_path + "przetwornica_on.png")
		self.bateria_on  = Image.open(lookup_path + "bateria_on.png")
		self.falownik_on  = Image.open(lookup_path + "falownik_on.png")
		self.sprezarka_on  = Image.open(lookup_path + "sprezarka_on.png")
		self.sprezarka_idle  = Image.open(lookup_path + "sprezarka_idle.png")
		self.M1M2_on  = Image.open(lookup_path + "M1M2_on.png")
		self.M3M4_on  = Image.open(lookup_path + "M3M4_on.png")
		self.M1M2_awaria  = Image.open(lookup_path + "M1M2_awaria.png")
		self.M3M4_awaria  = Image.open(lookup_path + "M3M4_awaria.png")	
		self.M1M2_gotow  = Image.open(lookup_path + "M1M2_gotowy.png")
		self.M3M4_gotow  = Image.open(lookup_path + "M3M4_gotowy.png")			
		self.awaria_off  = Image.open(lookup_path + "awaria_off.png")
		self.awaria_on  = Image.open(lookup_path + "awaria_on.png")
		self.hamulec_off  = Image.open(lookup_path + "hamulec_off.png")
		self.hamulec_on  = Image.open(lookup_path + "hamulec_on.png")
		self.poslizg_on  = Image.open(lookup_path + "poslizg_on.png")
		self.poslizg_off  = Image.open(lookup_path + "poslizg_off.png")
		self.klima_on  = Image.open(lookup_path + "klima_on.png")
		self.klima_off  = Image.open(lookup_path + "klima_off.png")
		self.grzanie_on  = Image.open(lookup_path + "grzanie_on.png")
		self.grzanie_off  = Image.open(lookup_path + "grzanie_off.png")
		self.terminal_msg = None
		self.hamulce = None		
		self.ipsz = Image.open(lookup_path + "podklad_hamulec_ipsz_kwadraty.png")	
		self.knorr = Image.open(lookup_path + "podklad_hamulec_knorr_kwadraty.png")			
		self.terminal_msg_slice = Image.open(lookup_path + "komunikat_linijka.png")	
		self.reflektory = Image.open(lookup_path + "podklad_reflektory_km.png")	
		self.drzwi = Image.open(lookup_path + "podklad_drzwi_km.png")		
		self.drzwiezt2 = Image.open(lookup_path + "drzwiezt2.png")	
		self.drzwiezt3 = Image.open(lookup_path + "drzwiezt3.png")	
		self.boot1 = Image.open('./textures/tabor/python/medcom_en57/bootowanie_medcom_1.png')
		self.boot2 = Image.open('./textures/tabor/python/medcom_en57/bootowanie_medcom_2.png')
		self.boot3 = Image.open('./textures/tabor/python/medcom_en57/bootowanie_medcom_3.png')
		self.boot4 = Image.open('./textures/tabor/python/medcom_en57/bootowanie_medcom_4.png')
		self.boot5 = Image.open('./textures/tabor/python/medcom_en57/bootowanie_medcom_5.png')
		# wczytanie czcionki
		czcionka = "./fonts/verdana.ttf"
		self.font = ImageFont.truetype( czcionka, 20)
		self.sredni_font = ImageFont.truetype( czcionka, 17)
		self.maly_font = ImageFont.truetype( czcionka, 15)
		self.bardzo_maly_font = ImageFont.truetype( czcionka, 12)
		self.polduzy_font = ImageFont.truetype( czcionka, 27)
		self.fontv16 = ImageFont.truetype( czcionka, 14)
		self.fontv16b = ImageFont.truetype('./fonts/verdanab.ttf', 16)
		self.font_komunikat = ImageFont.truetype('./fonts/myriadpro-semibold.otf', 20)	
		
		self.kilometry = (random()*300000)+5000
		self.last_time_update = 0
		self.dzis = datetime.now().timetuple().tm_yday
		self.rok = datetime.now().year
		self.last_hour = 10
		self.aktyw = 0
		self.aktywm1m2 = 0		
		self.aktywm3m4 = 0	
		self.aktyw2m1m2 = 0		
		self.aktyw2m3m4 = 0		
		self.aktyw3m1m2 = 0		
		self.aktyw3m3m4 = 0		
		self.pasek = 0
		self.temp12 = (random()*21) + 18
		self.temp34 = (random()*19) + 16
		self.temp56 = (random()*20) + 14
		self.temp78 = (random()*18) + 17
		self.temp910 = (random()*19) + 16
		self.temp1112 = (random()*20) + 14		
		self.losowanie_niskie_wc = randint(0, 15)
		self.losowanie_24v = randint(0, 15)		
		self.losowanie_110v = randint(0, 15)	
		self.losowanie_bufor = randint(0, 25)		
		self.konsola = ImageFont.truetype('./fonts/unifont.ttf', 18)
		self.last_praca_update = 0		
		self.praca2 = 0		
		self.praca = 0			
		self.tryb = 0
		self.stan1 = False
		self.stan2 = False
		self.stan4 = False
		self.stan5 = False
		self.stan6 = False
		self.klikniete = -1
		self.woz = None # nazwa pojazdu			
		self.active_messages = []		

	def _render(self, state):
		if self.podklad == None and self.terminal_msg == None:
			if int(state["zadajnik"]) == 1:
				self.podklad = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_km.png")
				self.terminal_msg = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_komunikaty_km.png")
				if int(state["ipsz"]) == 1:
					self.hamulce = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_hamulec_ipsz.png")		
				else:
					self.hamulce = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_hamulec_knorr.png")	
			if int(state["zadajnik"]) == 0:
				self.podklad = Image.open("./dynamic/pkp/en57al_v1/screen/podklad.png")
				self.terminal_msg = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_komunikaty_km.png")	
				if int(state["ipsz"]) == 1:
					self.hamulce = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_hamulec_ipsz.png")		
				else:
					self.hamulce = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_hamulec_knorr.png")						
			if int(state["zadajnik"]) == 2:
				self.podklad = Image.open("./dynamic/pkp/en57al_v1/screen/podklad.png")	
				self.terminal_msg = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_komunikaty_km.png")		
				if int(state["ipsz"]) == 1:
					self.hamulce = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_hamulec_ipsz.png")	
				else:
					self.hamulce = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_hamulec_knorr.png")						
			if int(state["zadajnik"]) == 3:
				self.podklad = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_akm.png")		
				self.terminal_msg = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_komunikaty_akm.png")		
				if int(state["ipsz"]) == 1:
					self.hamulce = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_hamulec_ipsz_akm.png")
				else:
					self.hamulce = Image.open("./dynamic/pkp/en57al_v1/screen/podklad_hamulec_knorr.png")						
		tlo = self.tlo.copy()
		dt = 0
		# Liczenie pojazdow
		pojazdy = 0
		unit_no = state['unit_no']
		if (unit_no == 1):
			pojazdy = 1
		if (unit_no == 2):
			pojazdy = 2
		if (unit_no == 3):
			pojazdy = 3
			
			
		niskie_wc = (self.losowanie_niskie_wc < 2)
		v24 = (self.losowanie_24v < 2)		
		v110 = (self.losowanie_110v < 2)	
		bufor = (self.losowanie_bufor < 2)			
		napiecie1 = state['eimp_c1_uhv']
		napiecie2 = state['eimp_c2_uhv']
		napiecie3 = state['eimp_c3_uhv']
		velocity = state['velocity']
		speed = float(velocity)
		if speed > 200:
			speed = 200
		temp = state['air_temperature']
		direction = state['direction']
		direction2 = (state['direction'] == 1) or (state['direction'] == -1)
		seconds = state['seconds']
		minutes = state['minutes']
		hours = state['hours']
		dir_brake = state['dir_brake']
		epfuse = state['epfuse']
		indir_brake = state['indir_brake']
		brakes_1_spring_active = state['brakes_1_spring_active']
		brakes_3_spring_active = state['brakes_3_spring_active']
		brakes_4_spring_active = state['brakes_4_spring_active']
		brakes_6_spring_active = state['brakes_6_spring_active']
		brakes_7_spring_active = state['brakes_7_spring_active']
		brakes_9_spring_active = state['brakes_9_spring_active']
		spring_brake = ((brakes_1_spring_active == 1) | (brakes_3_spring_active == 1) |(brakes_4_spring_active == 1) | (brakes_6_spring_active == 1) | (brakes_7_spring_active == 1) | (brakes_9_spring_active == 1) )
		dir_or_indir_brake = (dir_brake | indir_brake )
		doors_1 = state['doors_1']
		doors_2 = state['doors_2']
		doors_3 = state['doors_3']
		doors_ezt1 = (doors_1 | doors_2 | doors_3)
		doors_4 = state['doors_4']
		doors_5 = state['doors_5']
		doors_6 = state['doors_6']
		doors_ezt2 = (doors_4 | doors_5 | doors_6)
		doors_7 = state['doors_7']
		doors_8 = state['doors_8']
		doors_9 = state['doors_9']
		doors_ezt3 = (doors_7 | doors_8 | doors_9)
		eimp_u1_pf = state['eimp_u1_pf']
		eimp_u1_pr = state['eimp_u1_pr']
		eimp_u2_pf = state['eimp_u2_pf']
		eimp_u2_pr = state['eimp_u2_pr']
		eimp_u3_pf = state['eimp_u3_pf']
		eimp_u3_pr = state['eimp_u3_pr']
		eimp_c1_ms = state['eimp_c1_ms']
		eimp_c2_ms = state['eimp_c2_ms']
		eimp_c3_ms = state['eimp_c3_ms']
		eimp_c1_conv = state['eimp_c1_conv']
		eimp_c2_conv = state['eimp_c2_conv']
		eimp_c3_conv = state['eimp_c3_conv']
		eimp_c1_fuse = state['eimp_c1_fuse']
		eimp_c2_fuse = state['eimp_c2_fuse']
		eimp_c3_fuse = state['eimp_c3_fuse']
		ws_gotowosc = state['main_ready']
		lights_front = state['lights_train_front']
		lights_rear = state['lights_train_rear']		
		sprezarka_pomocnicza = (state['pant_compressor'] == 1)
		went_ft1 = (self.aktywm1m2>=11) and (self.aktywm1m2<13)	
		went_ft2 = (self.aktywm3m4>=11) and (self.aktywm3m4<13)	
		went2_ft1 = (self.aktyw2m1m2>=11) and (self.aktyw2m1m2<13)	
		went2_ft2 = (self.aktyw2m3m4>=11) and (self.aktyw2m3m4<13)		
		went3_ft1 = (self.aktyw3m1m2>=11) and (self.aktyw3m1m2<13)	
		went3_ft2 = (self.aktyw3m3m4>=11) and (self.aktyw3m3m4<13)			
		gotowy_do_jazdy = ((doors_ezt1 == 0)&(doors_ezt2 == 0)&(doors_ezt3 == 0)&(dir_or_indir_brake == 0)&(spring_brake == 0)&((eimp_c1_ms&eimp_c1_conv) == 1)&(eimp_c1_fuse == 0)&(eimp_c2_fuse == 0)&(eimp_c3_fuse == 0)&(direction2 == 1)&((state['pantpress']) > 3.5))
		temp_zew = float(state['air_temperature'])	
		
		# czas
		if seconds != self.last_time_update:
			dt = seconds - self.last_time_update
			if dt < 0:
				dt+=60
			self.kilometry += dt*speed * 0.0002778
			self.last_time_update = seconds
		czas = str(hours) + ":" 
		if minutes<10:
			czas = czas + "0" + str(minutes) + ":"
		else:
			czas = czas + str(minutes) + ":"
		if seconds<10:
			czas = czas + "0" +str(seconds)
		else:
			czas = czas + str(seconds)
			
		# data
		if self.last_hour == 23 and hours == 0:
			self.dzis = self.dzis+1 # wlasnie wybila polnoc
		self.last_hour = hours
		data = datetime(self.rok, 1, 1) + timedelta(self.dzis - 1)
		data = data.strftime("%d/%m/%Y")	

		
		self.klikniete = -1		
		# kopia obrazka na potrzeby tego jednego renderowania
		obrazek = self.podklad.copy()
		# chcemy rysowac po teksturze pulpitu
		draw = ImageDraw.Draw(obrazek)
		if (state['battery'] or state['converter']):
				self.aktyw += dt
				if self.aktyw<21:
					if self.aktyw >= 0:
						obrazek.paste(self.boot1, (0,0), self.boot1)
					if self.aktyw >= 2:
						obrazek.paste(self.boot2, (0,0), self.boot2)
					if self.aktyw >= 3:
						draw.text((5,260), 'GRUB Loading stage1.5', fill=self.bialy, font=self.konsola)
					if self.aktyw >= 4:
						draw.text((5,320), 'GRUB loading, please wait...', fill=self.bialy, font=self.konsola)	
					if self.aktyw >= 5:
						obrazek.paste(self.boot3, (0,0), self.boot3)
					if self.aktyw >= 6:
						draw.rectangle((0, 0, 798, 606), fill=self.czarny)
					if (self.aktyw >= 6 and self.aktyw < 8):
						draw.text((5,70), 'Starting up ...', fill=self.bialy, font=self.konsola)
					if (self.aktyw >= 7 and self.aktyw < 8):
						draw.text((5,100), 'Uncompressing Linux... Ok, booting the kernel.', fill=self.bialy, font=self.konsola)	
					if self.aktyw >= 8:
						obrazek.paste(self.boot4, (0,0), self.boot4)	
						draw.text((5,230), 'Starting up ...', fill=self.bialy, font=self.konsola)
						draw.text((5,245), 'Uncompressing Linux... Ok, booting the kernel.', fill=self.bialy, font=self.konsola)	
					if self.aktyw >= 9:
						self.pasek += dt
						obrazek.paste(self.boot5, (0,0), self.boot5)	
						draw.rectangle((170,331,170 + 89 * self.pasek,358), fill=self.niebieski_boot)
					if self.aktyw >= 14:
						draw.rectangle((0, 0, 798, 606), fill=self.czarny)
						draw.text((5,100), 'Starting up ...', fill=self.bialy, font=self.konsola)
						draw.text((5,115), 'Uncompressing Linux... Ok, booting the kernel.', fill=self.bialy, font=self.konsola)	
						draw.text((5,130), 'INIT: version 2.86 booting', fill=self.bialy, font=self.konsola)	
						draw.text((5,160), 'Please wait: booting...', fill=self.bialy, font=self.konsola)	
						draw.text((5,175), 'Starting the hotplug events dispatcher udevd', fill=self.bialy, font=self.konsola)
						draw.text((5,190), 'Synthesizing the initial hotplug events', fill=self.bialy, font=self.konsola)
						draw.text((5,205), 'Waiting for /dev to be fully populated', fill=self.bialy, font=self.konsola)
						draw.text((5,235), 'Setting up IP spoofing protection: rp_filter.', fill=self.bialy, font=self.konsola)
						draw.text((5,250), 'Configuration network interfaces... done.', fill=self.bialy, font=self.konsola)
						draw.text((5,275), 'Setting watchdog timeout', fill=self.bialy, font=self.konsola)
						draw.text((5,290), 'Setting audio volumes', fill=self.bialy, font=self.konsola)
						draw.text((5,305), 'Setting up CAN-bus drivers', fill=self.bialy, font=self.konsola)
					if self.aktyw >= 15:
						draw.rectangle((0, 0, 798, 606), fill=self.czarny)
					if self.aktyw >= 17:
						draw.line([(392,352),(409,335)], fill=self.bialy, width=3)
						draw.line([(392,335),(409,352)], fill=self.bialy, width=3)
						draw.line([(394,350),(407,340)], fill=self.czarny, width=1)
						draw.line([(394,340),(407,350)], fill=self.czarny, width=1)
					if self.aktyw >= 20:
						draw.rectangle((0, 0, 798, 606), fill=self.szary)
				else:				
					if state['universal1'] != self.stan1:
						self.klikniete = 1
					if state['universal2'] != self.stan2:
						self.klikniete = 2
					if state['universal4'] != self.stan4:
						self.klikniete = 4
					if state['universal5'] != self.stan5:
						self.klikniete = 5
					if state['universal6'] != self.stan6:
						self.klikniete = 6						

					if (self.klikniete == 1): #status glowny skądkolwiek
						self.tryb = 0
					elif (self.tryb == 4) or (self.klikniete == 4): # na drzwi albo z drzwi donikąd
						self.tryb = 4 # drzwi
					elif (self.klikniete == 2): # na alarmy
						self.tryb = 2 # alarmy
					elif (self.klikniete == 5): # na hamulec
						self.tryb = 6 # hamulec					
					elif (self.klikniete == 6) and int(state["zadajnik"]) != 3 and int(state["zadajnik"]) != 2: # na reflektory
						self.tryb = 5 # reflektory
			

					### komunikaty duze

					if state['cab'] > 0:
						prawe = "_r_"
						lewe  = "_l_"
					else:
						lewe  = "_r_"
						prawe = "_l_"

					messages = [
						{"name":u"EZT1: niesprawne wentylatory FT1","color":self.czerwony,"cond":went_ft1},		
						{"name":u"EZT1: niesprawne wentylatory FT2","color":self.czerwony,"cond":went_ft2},	
						{"name":u"EZT2: niesprawne wentylatory FT1","color":self.czerwony,"cond":went2_ft1 and pojazdy > 1},		
						{"name":u"EZT2: niesprawne wentylatory FT2","color":self.czerwony,"cond":went2_ft2 and pojazdy > 1},	
						{"name":u"EZT3: niesprawne wentylatory FT1","color":self.czerwony,"cond":went3_ft1 and pojazdy > 2},		
						{"name":u"EZT3: niesprawne wentylatory FT2","color":self.czerwony,"cond":went3_ft2 and pojazdy > 2},							
						{"name":u"EZT1: błąd aktywacji kabiny","color":self.czerwony,"cond":state['cabactive'] == 1 and state['cab'] == -1 or state['cabactive'] == -1 and state['cab'] == 1},	
						{"name":u"EZT1: niski poziom wody zbiornika WC","color":self.czerwony,"cond":niskie_wc},	
						{"name":u"EZT1: zadziałanie zabezp. nadprąd. zasil. 24V wagonu S","color":self.czerwony,"cond":v24},
						{"name":u"EZT1: zadziałanie zabezp. nadprąd. zasil. 110V wagonu S","color":self.czerwony,"cond":v110},		
						{"name":u"EZT1: brak komunikacji CAN z zasilaczem buforowym 1","color":self.czerwony,"cond":bufor},							
						{"name":u"EZT1: brak kierunku jazdy","color":self.zolty,"cond":direction == 0 and state['eimp_c1_ms'] != 0},
						{"name":u"EZT1: wyzeruj nastawnik kierunku","color":self.zolty,"cond":state['eimp_c1_ms'] == 0 and direction != 0 and speed == 0},
						{"name":u"EZT1: wyzeruj nastawnik jazdy","color":self.zolty,"cond":state['eimp_c1_ms'] == 0 and state["mainctrl_pos"] != 0},						
						{"name":u"EZT1: niskie ciśnienie pantografów","color":self.czerwony,"cond":state["eimp_pn2_cp"] < 2.5},
						{"name":u"EZT2: niskie ciśnienie pantografów","color":self.czerwony,"cond":state["eimp_pn4_cp"] < 2.5 and pojazdy > 1},
						{"name":u"EZT3: niskie ciśnienie pantografów","color":self.czerwony,"cond":state["eimp_pn6_cp"] < 2.5 and pojazdy > 2},
						{"name":u"EZT1: blokada napędu od pneumatyki","color":self.czerwony,"cond":dir_or_indir_brake and velocity < 0.5 and int(state["ipsz"]) == 1},
						{"name":u"EZT1: hamulec postojowy załączony","color":self.czerwony,"cond":spring_brake and int(state["zadajnik"]) == 3},
						#{"name":u"EZT2: blokada napędu od pneumatyki","color":self.czerwony,"cond":dir_or_indir_brake and velocity < 0.5 and pojazdy > 1},
					#	{"name":u"EZT3: blokada napędu od pneumatyki","color":self.czerwony,"cond":dir_or_indir_brake and velocity < 0.5 and pojazdy > 2},
						{"name":u"EZT1: otwarte drzwi - strona prawa","color":self.bialy,"cond":state["doors"+prawe+"1"] or state["doors"+prawe+"2"] or state["doors"+prawe+"3"]},
						{"name":u"EZT2: otwarte drzwi - strona prawa","color":self.bialy,"cond":state["doors"+prawe+"4"] or state["doors"+prawe+"5"] or state["doors"+prawe+"6"]},
						{"name":u"EZT3: otwarte drzwi - strona prawa","color":self.bialy,"cond":state["doors"+prawe+"7"] or state["doors"+prawe+"8"] or state["doors"+prawe+"9"]},
						{"name":u"EZT1: otwarte drzwi - strona lewa","color":self.bialy,"cond":state["doors"+lewe+"1"] or state["doors"+lewe+"2"] or state["doors"+lewe+"3"]},
						{"name":u"EZT2: otwarte drzwi - strona lewa","color":self.bialy,"cond":state["doors"+lewe+"4"] or state["doors"+lewe+"5"] or state["doors"+lewe+"6"]},
						{"name":u"EZT3: otwarte drzwi - strona lewa","color":self.bialy,"cond":state["doors"+lewe+"7"] or state["doors"+lewe+"8"] or state["doors"+lewe+"9"]},
						{"name":u"EZT1: próba szczelności","color":self.czerwony,"cond":state["brake_op_mode_flag"] == 1},
						{"name":u"EZT1: niskie ciśnienie w przewodzie zasilającym","color":self.czerwony,"cond":state["eimp_pn2_sp"] < 5.7},
						{"name":u"EZT2: niskie ciśnienie w przewodzie zasilającym","color":self.czerwony,"cond":state["eimp_pn4_sp"] < 5.7 and pojazdy > 1},
						{"name":u"EZT3: niskie ciśnienie w przewodzie zasilającym","color":self.czerwony,"cond":state["eimp_pn6_sp"] < 5.7 and pojazdy > 2},
						{"name":u"EZT1: tempomat aktywny","color":self.bialy,"cond":state["scndctrl_pos"] > 0},
						{"name":u"EZT1: przekroczona górna granica napięcia trakcji","color":self.czerwony,"cond":napiecie1 > 4500},
						{"name":u"EZT2: przekroczona górna granica napięcia trakcji","color":self.czerwony,"cond":napiecie2 > 4500 and pojazdy > 1},
						{"name":u"EZT3: przekroczona górna granica napięcia trakcji","color":self.czerwony,"cond":napiecie3 > 4500 and pojazdy > 2},
						{"name":u"EZT1: niskie napięcie baterii","color":self.czerwony,"cond":state["eimp_c1_cv"] < 90},
						{"name":u"EZT2: niskie napięcie baterii","color":self.czerwony,"cond":state["eimp_c2_cv"] < 90 and pojazdy > 1},
						{"name":u"EZT3: niskie napięcie baterii","color":self.czerwony,"cond":state["eimp_c3_cv"] < 90 and pojazdy > 2},
						{"name":u"EZT1: odblokuj urządzenia nadmiarowe","color":self.czerwony,"cond":state["eimp_c1_fuse"]},
						{"name":u"EZT2: odblokuj urządzenia nadmiarowe","color":self.czerwony,"cond":state["eimp_c2_fuse"] and pojazdy > 1},
						{"name":u"EZT3: odblokuj urządzenia nadmiarowe","color":self.czerwony,"cond":state["eimp_c3_fuse"] and pojazdy > 1},
						{"name":u"EZT1: Sprężarka pantografowa pracuje","color":self.bialy,"cond":sprezarka_pomocnicza},
						{"name":u"EZT2: Sprężarka pantografowa pracuje","color":self.bialy,"cond":sprezarka_pomocnicza and pojazdy > 1},
						{"name":u"EZT3: Sprężarka pantografowa pracuje","color":self.bialy,"cond":sprezarka_pomocnicza and pojazdy > 2},
						#{"name":u"EZT1: Wyłącznik szybki gotowy do załączenia","color":self.bialy,"cond":(state['main_ready'])},
						#{"name":u"EZT2: Wyłącznik szybki gotowy do załączenia","color":self.bialy,"cond":(state['main_ready']) and pojazdy > 1 and napiecie2 > 2000},
						#{"name":u"EZT3: Wyłącznik szybki gotowy do załączenia","color":self.bialy,"cond":(state['main_ready']) and pojazdy > 2 and napiecie3 > 2000},
						{"name":u"EZT1: Przerwana pętla bezpieczeństwa","color":self.czerwony,"cond":state['door_lock'] == 0},
						{"name":u"EZT1: Przerwana „zielona” pętla drzwi","color":self.czerwony,"cond":(state['door_lock'] == 0)},
						{"name":u"EZT2: Przerwana „zielona” pętla drzwi","color":self.czerwony,"cond":(state['door_lock'] == 0) and pojazdy > 1},
						{"name":u"EZT3: Przerwana „zielona” pętla drzwi","color":self.czerwony,"cond":(state['door_lock'] == 0) and pojazdy > 2},
					]


					for i in range(len(messages)):
						message = messages[i]
						messageActive = message["cond"] # czy powinno byc
						messageActived = -1 # czy jest
						for j in range(len(self.active_messages)):
							if i == self.active_messages[j]["id"]:
								messageActived = j
								break
						if messageActive and messageActived == -1: # dodawanie do listy
							self.active_messages.insert(0, {"id":i, "time":czas}) # dajemy na poczatek listy, poniewaz najnowsze komunikaty pojawiaja sie na gorze
						if (not messageActive) and messageActived > -1: # usuwanie z listy
							del self.active_messages[messageActived]			
			
			
					draw.rectangle((0, 0, 798, 606), fill=self.szary)
					if state['cabactive'] == 1 and state['cab'] == 1 or state['cabactive'] == -1 and state['cab'] == -1:
						if (self.tryb == 0):	
							obrazek.paste(self.podklad, (0,0))
							# kierunek jazdy
							if direction == 1:
								draw.polygon([(285, 79), (296, 42), (286, 44), (299, 18), (312, 44), (302, 42), (312, 79)],fill=self.zielony) # strzalka kierunkowa naprzod

							if direction == -1:
								draw.polygon([(285, 118), (296, 155), (286, 153), (299, 179), (312, 153), (302, 155), (312, 118)],fill=self.zielony) # strzalka kierunkowa w tyl

							# slupek napiecia i jego wartosc
							if napiecie1 < 0:
								napiecie1 = 0
							pos = 176 - (napiecie1 * 152 / 5000)+2
							draw.rectangle((483,pos,465,174), fill=self.bialy)
							napiecie_1 = napiecie1/1000
							draw.text((461, 179), '%.1f' % napiecie_1, fill=self.zolty, font=self.sredni_font)

							# slupek procentu siły zadanej jazdy
							if int(state["zadajnik"]) == 1:
								sila = state['eimp_t_pd']
								pos = 98 - (sila * 76)-2
								draw.rectangle((14,98,32,pos), fill=self.bialy)
								sila=sila*100
								self.print_fixed_with(draw, '%d' % sila, (7, 179), 3, self.sredni_font, self.zolty)
							else:
								sila = state['eimp_t_pdt']
								pos = 176 - (sila * 150)-2
								draw.rectangle((14,176,32,pos), fill=self.bialy)
								sila=sila*100
								self.print_fixed_with(draw, '%d' % sila, (7, 179), 3, self.sredni_font, self.zolty)



							# napięcie NN
							self.print_fixed_with(draw, '%d' % state['eimp_c1_cv'], (718,129), 3, self.sredni_font, self.zolty)

							# prędkość
							self.print_fixed_with(draw, '%d' % speed, (718,173), 3, self.sredni_font, self.zolty)


							draw.text((705,4), czas, fill=self.bialy, font=self.sredni_font)


							draw.text((686,30), data, fill=self.bialy, font=self.sredni_font)

							# seria i model
							self.woz = self.get_vehicle_name(state['car_name1'])	

							self.print_center(draw, self.woz, 712,521, self.font, self.bialy)

							# kabina a aktywna
							cab = state['cab']
							if cab == 1:
								self.print_center(draw, "Kabina A aktywna", 712,424, self.bardzo_maly_font, self.bialy)
							if cab == -1:
								self.print_center(draw, "Kabina B aktywna", 712,424, self.bardzo_maly_font, self.bialy)
							# komunikaty stanu pojazdu
							if (gotowy_do_jazdy&(velocity < 0.5 )):
								komunikat2 = 'Gotowy do jazdy' #dodać warunki na ezt 2 i 3; self.zielony
								komunikat2_kolor = self.zielony
							elif ((dir_brake)&(epfuse)&((state['brake_op_mode_flag']) == 2)) and int(state["zadajnik"]) == 1:
								komunikat2 = u'Hamowanie ED' #żólty
								komunikat2_kolor = self.zolty
							elif ((dir_brake)&(epfuse)&((state['brake_op_mode_flag']) == 8)) and int(state["zadajnik"]) != 1:
								komunikat2 = u'Hamowanie ED' #żólty
								komunikat2_kolor = self.zolty						
							elif (gotowy_do_jazdy&(velocity > 0.5 )&(state['eimp_t_fdt'] == 0)):
								komunikat2 = 'Wybieg' #brak zadanej mocy, brak hamowania, jedzie; zółty
								komunikat2_kolor = self.zolty
							else:
								komunikat2 = ''
								komunikat2_kolor = self.bialy


							if state['eimp_c1_ms'] == 0:
								komunikat = u'Napęd nieaktywny' #brak rozrządu prawdopodobnie; czerowny
								komunikat_kolor = self.czerwony			
								
							elif (((state['door_lock']) == 0) or ((state['eimp_c1_inv1_act']) == 0) or ((state['eimp_c1_inv2_act']) == 0)) or (pojazdy > 1) and ((state['eimp_c2_inv1_act']) == 0) and ((state['eimp_c2_inv2_act']) == 0) or (pojazdy > 2) and ((state['eimp_c3_inv1_act']) == 0) and ((state['eimp_c3_inv2_act']) == 0):
								komunikat = 'Jazda awaryjna' #(door_signaling==false)&(engine_damaged==false); self.czerwony
								komunikat_kolor = self.czerwony
								
								
							elif (dir_or_indir_brake&(velocity < 0.5 ) or spring_brake or (doors_ezt1 or doors_ezt2 or doors_ezt3 != 0) or direction == 0):
								komunikat = u'Blokada napędu' #zahamowany i stoi; self.czerwony
								komunikat_kolor = self.czerwony									

							elif (gotowy_do_jazdy&(velocity > 0.5 )):
								komunikat = u'Napęd sprawny' #jak "gotowy do jazdy" tylko jedzie; self.zielony
								komunikat_kolor = self.zielony

							else:
								komunikat = ''
								komunikat_kolor = self.bialy
							self.print_center(draw, komunikat, 712,449, self.fontv16b, komunikat_kolor)
							self.print_center(draw, komunikat2, 712,483, self.fontv16b, komunikat2_kolor)

							if state['slip_2'] == 1 or state['slip_4'] == 1 or state['slip_6'] == 1:#poslizg
								obrazek.paste(self.poslizg_on,(362,3),self.poslizg_on)
							else:
								obrazek.paste(self.poslizg_off,(362,3),self.poslizg_off)

							if dir_or_indir_brake or spring_brake:#hamulec
								obrazek.paste(self.hamulec_on,(362,69),self.hamulec_on)
							else:
								obrazek.paste(self.hamulec_off,(362,69),self.hamulec_off)

							




							if state['eimp_c1_heat']:#grzanie
								obrazek.paste(self.grzanie_on,(685,58),self.grzanie_on)
							else:
								obrazek.paste(self.grzanie_off,(685,58),self.grzanie_off)

							# if state['']:#klima
								# obrazek.paste(self.klima_on,(747,58),self.klima_on)
							# else:
							obrazek.paste(self.klima_off,(742,57),self.klima_off)


							 # i to tyle jesli chodzi o logike, teraz rysowanie

							i = 0
							for msg in self.active_messages:
								if msg["id"] >= len(messages):
									continue
								message = messages[msg["id"]]
								draw.text((8, 425 + (i * 40)), message["name"], font = self.font_komunikat, fill = message["color"])							
								if i == 2: # po 3 konczymy, wiecej sie nie zmiesci
									break
								i += 1						



							### koniec komunikatow duzych



					 #dla jednego EZT
							if (pojazdy == 1):
								obrazek.paste(self.ramki1,self.ramki1)

								#sila trakcyjna
								#sila = state['eimp_c1_fr']
								sila1 = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c1_pr'] * state['eimp_c1_inv1_act']
								pos1 = 98 - sila1
								sila2 = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c1_pr'] * state['eimp_c1_inv2_act']
								pos2 = 98 - sila2								
								draw.rectangle((114,98,139,pos1), fill=self.bialy)
								draw.rectangle((142,98,167,pos2), fill=self.bialy)

								#prad czlonu
								prad = state['eimp_c1_ihv']
								pos = 98 - (prad * 0.1086)+2
								draw.rectangle((567,98,597,pos), fill=self.bialy)
								self.print_fixed_with(draw, '%d' % prad, (545,179), 4, self.sredni_font, self.zolty)
								
								if state['door_lock'] == 0 or state['eimp_c1_inv1_allow'] == 0 or state['eimp_c1_inv1_error'] == 1 or state['eimp_c1_inv2_allow'] == 0 or state['eimp_c1_inv2_error'] == 1 or went_ft1 or went_ft2: 
									obrazek.paste(self.awaria_on,(362,131),self.awaria_on)
								else:
									obrazek.paste(self.awaria_off,(362,131),self.awaria_off)									

					#dla jednego lub dwóch
							if (2 >= pojazdy >= 1):

								draw.text((1, 286), 'EZT1', fill=self.bialy, font=self.polduzy_font)#NR EZT
							#Pasek ikon
								if (napiecie1 > 2050):#Wysokie napięcie
									obrazek.paste(self.WN_on,(71,273),self.WN_on)
								else:
									obrazek.paste(self.WN_off,(71,273),self.WN_off)



								if eimp_c1_ms: #Wylacznik szybki
									obrazek.paste(self.WS_on,(148,273),self.WS_on)
								elif state['main_ready']: #Gotowość WS
									if ((state['seconds'] % 2) == 1):
										obrazek.paste(self.WS_gotowosc,(148,273),self.WS_gotowosc)
									else:
										obrazek.paste(self.WS_off,(148,273),self.WS_off)							
								else:
									obrazek.paste(self.WS_off,(148,273),self.WS_off)
								if eimp_c1_conv:#Przetwornica
									obrazek.paste(self.przetwornica_on,(224,273),self.przetwornica_on)
								else:
									obrazek.paste(self.przetwornica_off,(224,273),self.przetwornica_off)

								if state['eimp_c1_batt']:#Bateria
									obrazek.paste(self.bateria_on,(301,273),self.bateria_on)
								else:
									obrazek.paste(self.bateria_off,(301,273),self.bateria_off)

								if eimp_c1_conv:#Falownik
									obrazek.paste(self.falownik_on,(377,273),self.falownik_on)
								else:
									obrazek.paste(self.falownik_off,(377,273),self.falownik_off)

								if (state['eimp_u1_comp_w'] & eimp_c1_conv): #Sprezarka
									obrazek.paste(self.sprezarka_on,(454,273),self.sprezarka_on)
								else:
									obrazek.paste(self.sprezarka_idle,(454,273),self.sprezarka_idle)


								obrazek.paste(self.M1M2_off,(530,273),self.M1M2_off)	

								if eimp_c1_ms:								
									self.aktywm1m2 += dt
									if (self.aktywm1m2<6): 										
										obrazek.paste(self.M1M2_gotow,(530,273),self.M1M2_gotow)	
									if (self.aktywm1m2>=6): 	
										if state['eimp_c1_inv1_act'] == 1:
											obrazek.paste(self.M1M2_on,(530,273),self.M1M2_on)
										if state['eimp_c1_inv1_allow'] == 0 or state['eimp_c1_inv1_error'] == 1:
											obrazek.paste(self.M1M2_awaria,(530,273),self.M1M2_awaria)		
								else:
									self.aktywm1m2 = 0	
									

								obrazek.paste(self.M3M4_off,(607,273),self.M3M4_off)									
									
								if eimp_c1_ms:								
									self.aktywm3m4 += dt
									if (self.aktywm3m4<7): 										
										obrazek.paste(self.M3M4_gotow,(607,273),self.M3M4_gotow)	
									if (self.aktywm1m2>=7): 	
										if state['eimp_c1_inv2_act'] == 1:
											obrazek.paste(self.M3M4_on,(607,273),self.M3M4_on)
										if state['eimp_c1_inv2_allow'] == 0 or state['eimp_c1_inv2_error'] == 1:
											obrazek.paste(self.M3M4_awaria,(607,273),self.M3M4_awaria)		
								else:
									self.aktywm3m4 = 0								
								


								#prąd silników 1,2
								im = abs(state['eimp_c1_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (690, 295), 3, self.bardzo_maly_font, self.zolty)

								#temp silników 1,2
								im = abs(state['eimp_c1_im'])								
								self.temp12 = self.temp12 + ((10 - self.temp12 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt			
								self.print_fixed_with(draw, '%i' % self.temp12, (690, 315), 3, self.bardzo_maly_font, self.zolty)

								#prąd silników 3,4
								im = abs(state['eimp_c1_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (751, 295), 3, self.bardzo_maly_font, self.zolty)

								#temp silników 3,4
								im = abs(state['eimp_c1_im'])								
								self.temp34 = self.temp34 + ((10 - self.temp34 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt		
								self.print_fixed_with(draw, '%i' % self.temp34, (751, 315), 3, self.bardzo_maly_font, self.zolty)



					#dla dwóch EZT
							if (pojazdy == 2):
								obrazek.paste(self.ramki2,self.ramki2)
								draw.text((1, 356), 'EZT2', fill=self.bialy, font=self.polduzy_font)#NR EZT

								#sila trakcyjna
								sila1 = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c1_pr'] * state['eimp_c1_inv1_act']
								pos1 = 98 - sila1
								sila2 = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c1_pr'] * state['eimp_c1_inv2_act']
								pos2 = 98 - sila2								
								draw.rectangle((114,98,125,pos1), fill=self.bialy)
								draw.rectangle((128,98,139,pos2), fill=self.bialy)
								sila3 = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c2_pr'] * state['eimp_c2_inv1_act']
								pos3 = 98 - sila3 
								sila4 = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c2_pr'] * state['eimp_c2_inv2_act']
								pos4 = 98 - sila4								
								draw.rectangle((142,98,153,pos3), fill=self.bialy)
								draw.rectangle((156,98,167,pos4), fill=self.bialy)

								#prad czlonu
								prad = state['eimp_c1_ihv']
								pos = 98 - (prad * 0.1086)+2
								draw.rectangle((567,98,580,pos), fill=self.bialy)
								self.print_fixed_with(draw, '%d' % prad, (535,183), 4, self.sredni_font, self.zolty)							
								prad = state['eimp_c2_ihv']
								pos = 98 - (prad * 0.1086)+2
								draw.rectangle((584,98,597,pos), fill=self.bialy)
								self.print_fixed_with(draw, '%d' % prad, (575,183), 4, self.sredni_font, self.zolty)							

								if state['door_lock'] == 0 or state['eimp_c1_inv1_allow'] == 0 or state['eimp_c1_inv1_error'] == 1 or state['eimp_c1_inv2_allow'] == 0 or state['eimp_c1_inv2_error'] == 1 or state['eimp_c2_inv1_allow'] == 0 or state['eimp_c2_inv1_error'] == 1 or state['eimp_c2_inv2_allow'] == 0 or state['eimp_c2_inv2_error'] == 1 or went_ft1 or went_ft2 or went2_ft1 or went2_ft2 : #awaria
									obrazek.paste(self.awaria_on,(362,131),self.awaria_on)
								else:
									obrazek.paste(self.awaria_off,(362,131),self.awaria_off)									

							#Pasek ikon
								if (napiecie2 > 2050):#Wysokie napięcie
									obrazek.paste(self.WN_on,(75,339),self.WN_on)
								else:
									obrazek.paste(self.WN_off,(75,339),self.WN_off)

								if eimp_c1_ms: #Wylacznik szybki
									obrazek.paste(self.WS_on,(148,339),self.WS_on)
								elif state['main_ready']: #Gotowość WS
									if ((state['seconds'] % 2) == 1):
										obrazek.paste(self.WS_gotowosc,(148,339),self.WS_gotowosc)
									else:
										obrazek.paste(self.WS_off,(148,339),self.WS_off)							
								else:
									obrazek.paste(self.WS_off,(148,339),self.WS_off)

								if eimp_c2_conv:#Przetwornica
									obrazek.paste(self.przetwornica_on,(226,339),self.przetwornica_on)
								else:
									obrazek.paste(self.przetwornica_off,(226,339),self.przetwornica_off)

								if state['eimp_c2_batt']:#Bateria
									obrazek.paste(self.bateria_on,(302,339),self.bateria_on)
								else:
									obrazek.paste(self.bateria_off,(302,339),self.bateria_off)

								if eimp_c2_conv:#Falownik
									obrazek.paste(self.falownik_on,(378,339),self.falownik_on)
								else:
									obrazek.paste(self.falownik_off,(378,339),self.falownik_off)

								if (state['eimp_u2_comp_w'] & eimp_c1_conv): #Sprezarka
									obrazek.paste(self.sprezarka_on,(454,339),self.sprezarka_on)
								else:
									obrazek.paste(self.sprezarka_idle,(454,339),self.sprezarka_idle)


																	
								obrazek.paste(self.M1M2_off,(530,339),self.M1M2_off)	

								if eimp_c2_ms:								
									self.aktyw2m1m2 += dt
									if (self.aktyw2m1m2<6): 										
										obrazek.paste(self.M1M2_gotow,(530,339),self.M1M2_gotow)	
									if (self.aktyw2m1m2>=6): 	
										if state['eimp_c2_inv1_act'] == 1:
											obrazek.paste(self.M1M2_on,(530,339),self.M1M2_on)
										if state['eimp_c2_inv1_allow'] == 0 or state['eimp_c2_inv1_error'] == 1:
											obrazek.paste(self.M1M2_awaria,(530,339),self.M1M2_awaria)		
								else:
									self.aktyw2m1m2 = 0	
									

								obrazek.paste(self.M3M4_off,(607,339),self.M3M4_off)									
									
								if eimp_c2_ms:								
									self.aktyw2m3m4 += dt
									if (self.aktyw2m3m4<7): 										
										obrazek.paste(self.M3M4_gotow,(607,339),self.M3M4_gotow)	
									if (self.aktyw2m3m4>=7): 	
										if state['eimp_c2_inv2_act'] == 1:
											obrazek.paste(self.M3M4_on,(607,339),self.M3M4_on)
										if state['eimp_c2_inv2_allow'] == 0 or state['eimp_c2_inv2_error'] == 1:
											obrazek.paste(self.M3M4_awaria,(607,339),self.M3M4_awaria)		
								else:
									self.aktyw2m3m4 = 0											

								#prąd silników 1,2
								im = abs(state['eimp_c2_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (690, 365), 3, self.bardzo_maly_font, self.zolty)

								#temp silników 1,2
								im = abs(state['eimp_c2_im'])								
								self.temp56 = self.temp56 + ((10 - self.temp56 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt		
								self.print_fixed_with(draw, '%i' % self.temp56, (690, 385), 3, self.bardzo_maly_font, self.zolty)

								#prąd silników 3,4
								im = abs(state['eimp_c2_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (751, 365), 3, self.bardzo_maly_font, self.zolty)

								#temp silników 3,4
								im = abs(state['eimp_c2_im'])								
								self.temp78 = self.temp78 + ((10 - self.temp78 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt	
								self.print_fixed_with(draw, '%i' % self.temp78, (751, 385), 3, self.bardzo_maly_font, self.zolty)



							#dla 3 EZT
							if (pojazdy == 3):
								obrazek.paste(self.ramki3,self.ramki3)
								#self.print_center(draw, u"EZT1| 2 | 3" , 142,189, self.sredni_font, self.bialy)

								#sila trakcyjna
								sila = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c1_pr'] 
								pos = 98 - sila 
								draw.rectangle((114,98,120,pos), fill=self.bialy)
								draw.rectangle((123,98,129,pos), fill=self.bialy)
								sila = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c2_pr'] 
								pos = 98 - sila 
								draw.rectangle((132,98,138,pos), fill=self.bialy)
								draw.rectangle((141,98,147,pos), fill=self.bialy)
								sila = ( 1+min( 36, 1800/( speed+0.1) ) ) * state['eimp_c3_pr'] 
								pos = 98 - sila 
								draw.rectangle((150,98,156,pos), fill=self.bialy)
								draw.rectangle((159,98,165,pos), fill=self.bialy)

								#prad czlonu
								prad = state['eimp_c1_ihv']
								pos = 98 - (prad * 0.1086)+2
								draw.rectangle((567,98,575,pos), fill=self.bialy)
								self.print_fixed_with(draw, '%d' % prad, (510,183), 4, self.sredni_font, self.zolty)
								prad = state['eimp_c2_ihv']
								pos = 98 - (prad * 0.1086)+2
								draw.rectangle((578,98,586,pos), fill=self.bialy)
								self.print_fixed_with(draw, '%d' % prad, (550,183), 4, self.sredni_font, self.zolty)
								prad = state['eimp_c3_ihv']
								pos = 98 - (prad * 0.1086)+2
								draw.rectangle((589,98,597,pos), fill=self.bialy)
								self.print_fixed_with(draw, '%d' % prad, (590,183), 4, self.sredni_font, self.zolty)
								
								if state['door_lock'] == 0 or state['eimp_c1_inv1_allow'] == 0 or state['eimp_c1_inv1_error'] == 1 or state['eimp_c1_inv2_allow'] == 0 or state['eimp_c1_inv2_error'] == 1 or state['eimp_c2_inv1_allow'] == 0 or state['eimp_c2_inv1_error'] == 1 or state['eimp_c2_inv2_allow'] == 0 or state['eimp_c2_inv2_error'] == 1 or state['eimp_c3_inv1_allow'] == 0 or state['eimp_c3_inv1_error'] == 1 or state['eimp_c3_inv2_allow'] == 0 or state['eimp_c3_inv2_error'] == 1: #awaria								
									obrazek.paste(self.awaria_on,(362,131),self.awaria_on)	
								else:
									obrazek.paste(self.awaria_off,(362,131),self.awaria_off)									


									#Pasek ikon
								if (napiecie1 > 2050):#Wysokie napięcie
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"3000V" , 98,336, self.maly_font, kolor)

								if (napiecie2 > 2050):#Wysokie napięcie
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"3000V" , 98,365, self.maly_font, kolor)

								if (napiecie3 > 2050):#Wysokie napięcie
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"3000V" , 98,394, self.maly_font, kolor)




										
										
								if eimp_c1_ms: #Wylacznik szybki
										kolor = self.zielony
										self.print_center(draw, u"załączony" , 168,336, self.bardzo_maly_font, kolor)
								elif state['main_ready']: #Gotowość WS
									if ((state['seconds'] % 2) == 1):
										kolor = self.zolty
										self.print_center(draw, u"gotowy" , 168,336, self.maly_font, kolor)
									else:
										kolor = self.czerwony
										self.print_center(draw, u"wyłączony" , 168,336, self.bardzo_maly_font, kolor)										
								else:
									kolor = self.czerwony
									self.print_center(draw, u"wyłączony" , 168,336, self.bardzo_maly_font, kolor)
										

										
								if eimp_c2_ms: #Wylacznik szybki
										kolor = self.zielony
										self.print_center(draw, u"załączony" , 168,365, self.bardzo_maly_font, kolor)
								elif state['main_ready']: #Gotowość WS
									if ((state['seconds'] % 2) == 1):
										kolor = self.zolty
										self.print_center(draw, u"gotowy" , 168,365, self.maly_font, kolor)
									else:
										kolor = self.czerwony
										self.print_center(draw, u"wyłączony" , 168,365, self.bardzo_maly_font, kolor)										
								else:
									kolor = self.czerwony
									self.print_center(draw, u"wyłączony" , 168,365, self.bardzo_maly_font, kolor)										
										

								if eimp_c3_ms: #Wylacznik szybki
										kolor = self.zielony
										self.print_center(draw, u"załączony" , 168,394, self.bardzo_maly_font, kolor)
								elif state['main_ready']: #Gotowość WS
									if ((state['seconds'] % 2) == 1):
										kolor = self.zolty
										self.print_center(draw, u"gotowy" , 168,394, self.maly_font, kolor)
									else:
										kolor = self.czerwony
										self.print_center(draw, u"wyłączony" , 168,394, self.bardzo_maly_font, kolor)										
								else:
									kolor = self.czerwony
									self.print_center(draw, u"wyłączony" , 168,394, self.bardzo_maly_font, kolor)										
										


								if eimp_c1_conv:
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"110V" , 233,336, self.maly_font, kolor)

								if eimp_c2_conv:
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"110V" , 233,365, self.maly_font, kolor)

								if eimp_c3_conv:
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"110V" , 233,394, self.maly_font, kolor)	

								if state['eimp_c1_batt']:#Bateria
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"24V" , 299,336, self.maly_font, kolor)

								if state['eimp_c2_batt']:#Bateria
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"24V" , 299,365, self.maly_font, kolor)

								if state['eimp_c3_batt']:#Bateria
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"24V" , 299,394, self.maly_font, kolor)	


								if eimp_c1_conv:#Falownik
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"3x400V" , 366,336, self.maly_font, kolor)

								if eimp_c2_conv:#Falownik
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"3x400V" , 366,365, self.maly_font, kolor)

								if eimp_c3_conv:#Falownik
									kolor = self.zielony
								else:
									kolor = self.czerwony
								self.print_center(draw, u"3x400V" , 366,394, self.maly_font, kolor)		

								if state['eimp_c1_conv'] == 0:
									kolor = self.czerwony
								else:
									if state['eimp_u1_comp_w']:
										kolor = self.zielony
									else: 
										kolor = self.zolty
								self.print_center(draw, u"Sprężarka" , 434,336, self.bardzo_maly_font, kolor)

								if state['eimp_c2_conv'] == 0:
									kolor = self.czerwony
								else:
									if state['eimp_u2_comp_w']:
										kolor = self.zielony
									else: 
										kolor = self.zolty
								self.print_center(draw, u"Sprężarka" , 434,365, self.bardzo_maly_font, kolor)

								if state['eimp_c3_conv'] == 0:
									kolor = self.czerwony
								else:
									if state['eimp_u3_comp_w']:
										kolor = self.zielony
									else: 
										kolor = self.zolty
								self.print_center(draw, u"Sprężarka" , 434,394, self.bardzo_maly_font, kolor)


								
								
								self.print_center(draw, u"M1, M2" , 500,336, self.maly_font, self.szary)	

								if eimp_c1_ms:								
									self.aktywm1m2 += dt
									if (self.aktywm1m2<6): 										
										self.print_center(draw, u"M1, M2" , 500,336, self.maly_font, self.zolty)	
									if (self.aktywm1m2>=6): 	
										if state['eimp_c1_inv1_act'] == 1:
											self.print_center(draw, u"M1, M2" , 500,336, self.maly_font, self.zielony)	
										if state['eimp_c1_inv1_allow'] == 0 or state['eimp_c1_inv1_error'] == 1:
											self.print_center(draw, u"M1, M2" , 500,336, self.maly_font, self.czerwony)	
								else:
									self.aktywm1m2 = 0	
									

								self.print_center(draw, u"M1, M2" , 566,336, self.maly_font, self.szary)	

								if eimp_c1_ms:								
									self.aktywm3m4 += dt
									if (self.aktywm3m4<7): 										
										self.print_center(draw, u"M3, M4" , 566,336, self.maly_font, self.zolty)	
									if (self.aktywm3m4>=7): 	
										if state['eimp_c1_inv2_act'] == 1:
											self.print_center(draw, u"M3, M4" , 566,336, self.maly_font, self.zielony)	
										if state['eimp_c1_inv2_allow'] == 0 or state['eimp_c1_inv2_error'] == 1:
											self.print_center(draw, u"M3, M4" , 566,336, self.maly_font, self.czerwony)	
								else:
									self.aktywm3m4 = 0										
									

									
								self.print_center(draw, u"M1, M2" , 500,365, self.maly_font, self.szary)	

								if eimp_c2_ms:								
									self.aktyw2m1m2 += dt
									if (self.aktyw2m1m2<6): 										
										self.print_center(draw, u"M1, M2" , 500,365, self.maly_font, self.zolty)	
									if (self.aktyw2m1m2>=6): 	
										if state['eimp_c2_inv1_act'] == 1:
											self.print_center(draw, u"M1, M2" , 500,365, self.maly_font, self.zielony)	
										if state['eimp_c2_inv1_allow'] == 0 or state['eimp_c2_inv1_error'] == 1:
											self.print_center(draw, u"M1, M2" , 500,365, self.maly_font, self.czerwony)	
								else:
									self.aktyw2m1m2 = 0	
									

								self.print_center(draw, u"M1, M2" , 566,365, self.maly_font, self.szary)	

								if eimp_c2_ms:								
									self.aktyw2m3m4 += dt
									if (self.aktyw2m3m4<7): 										
										self.print_center(draw, u"M3, M4" , 566,365, self.maly_font, self.zolty)	
									if (self.aktyw2m3m4>=7): 	
										if state['eimp_c2_inv2_act'] == 1:
											self.print_center(draw, u"M3, M4" , 566,365, self.maly_font, self.zielony)	
										if state['eimp_c2_inv2_allow'] == 0 or state['eimp_c2_inv2_error'] == 1:
											self.print_center(draw, u"M3, M4" , 566,365, self.maly_font, self.czerwony)	
								else:
									self.aktyw2m3m4 = 0											
									


								self.print_center(draw, u"M1, M2" , 500,394, self.maly_font, self.szary)	

								if eimp_c3_ms:								
									self.aktyw3m1m2 += dt
									if (self.aktyw3m1m2<6): 										
										self.print_center(draw, u"M1, M2" , 500,394, self.maly_font, self.zolty)	
									if (self.aktyw3m1m2>=6): 	
										if state['eimp_c3_inv1_act'] == 1:
											self.print_center(draw, u"M1, M2" , 500,394, self.maly_font, self.zielony)	
										if state['eimp_c3_inv1_allow'] == 0 or state['eimp_c3_inv1_error'] == 1:
											self.print_center(draw, u"M1, M2" , 500,394, self.maly_font, self.czerwony)	
								else:
									self.aktyw3m1m2 = 0	
									

								self.print_center(draw, u"M1, M2" , 566,394, self.maly_font, self.szary)	

								if eimp_c3_ms:								
									self.aktyw3m3m4 += dt
									if (self.aktyw3m3m4<7): 										
										self.print_center(draw, u"M3, M4" , 566,394, self.maly_font, self.zolty)	
									if (self.aktyw3m3m4>=7): 	
										if state['eimp_c3_inv2_act'] == 1:
											self.print_center(draw, u"M3, M4" , 566,394, self.maly_font, self.zielony)	
										if state['eimp_c3_inv2_allow'] == 0 or state['eimp_c3_inv2_error'] == 1:
											self.print_center(draw, u"M3, M4" , 566,394, self.maly_font, self.czerwony)	
								else:
									self.aktyw3m3m4 = 0		



								#prąd silników ezt1 1,2
								im = abs(state['eimp_c1_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (601, 327), 3, self.fontv16, self.zolty)

								#temp silników 1,2
								#temp = temp + ((5 - temp) * 0.000329060 + (im * im * im / 3) * 0.000007031)* dt / 2
								im = abs(state['eimp_c1_im'])								
								self.temp12 = self.temp12 + ((10 - self.temp12 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt	
								self.print_fixed_with(draw, '%i' % self.temp12, (646, 327), 3, self.fontv16, self.zolty)

								#prąd silników 3,4
								im = abs(state['eimp_c1_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (701, 327), 3, self.fontv16, self.zolty)

								#temp silników 3,4
								im = abs(state['eimp_c1_im'])								
								self.temp34 = self.temp34 + ((10 - self.temp34 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt	
								self.print_fixed_with(draw, '%i' % self.temp34, (743, 327), 3, self.fontv16, self.zolty)


								#prąd silników ezt2 1,2
								im = abs(state['eimp_c2_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (601, 356), 3, self.fontv16, self.zolty)

								#temp silników 1,2
								im = abs(state['eimp_c2_im'])								
								self.temp56 = self.temp56 + ((10 - self.temp56 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt		
								self.print_fixed_with(draw, '%i' % self.temp56, (646, 356), 3, self.fontv16, self.zolty)

								#prąd silników 3,4
								im = abs(state['eimp_c2_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (701, 356), 3, self.fontv16, self.zolty)

								#temp silników 3,4
								im = abs(state['eimp_c2_im'])								
								self.temp78 = self.temp78 + ((10 - self.temp78 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt	
								self.print_fixed_with(draw, '%i' % self.temp78, (743, 356), 3, self.fontv16, self.zolty)

								#prąd silników ezt3 1,2
								im = abs(state['eimp_c3_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (601, 385), 3, self.fontv16, self.zolty)

								#temp silników 1,2
								#temp = temp + ((5 - temp) * 0.000329060 + (im * im * im / 3) * 0.000007031)* dt / 2
								im = abs(state['eimp_c3_im'])								
								self.temp910 = self.temp910 + ((10 - self.temp910 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt	
								self.print_fixed_with(draw, '%d' % self.temp910, (646, 385), 3, self.fontv16, self.zolty)

								#prąd silników 3,4
								im = abs(state['eimp_c3_im'])
								im = im / 2
								self.print_fixed_with(draw, '%d' % im, (701, 385), 3, self.fontv16, self.zolty)

								#temp silników 3,4
								im = abs(state['eimp_c3_im'])								
								self.temp1112 = self.temp56 + ((10 - self.temp1112 + temp_zew) * 0.000419 + (im * im * 9) * 0.000000691) * dt - 0.0000440 * temp_zew * dt		
								self.print_fixed_with(draw, '%d' % self.temp1112, (743, 385), 3, self.fontv16, self.zolty)

							if (pojazdy > 0):

								#Ikona EZT 1 
								obrazek.paste(self.ezt,(5, 218),self.ezt)
								draw.text((14,238), '1', fill=self.bialy, font=self.bardzo_maly_font)
								#Drzwi EZT1
								#człon a
								x=58
								if doors_ezt1: #wszystkie człony mają pokazywać razem, gdy cokolwiek otwarte
									kolor = self.czerwony
									dx=10
								else:
									kolor = self.bialy
									dx=0
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)
								#człon s
								x=136
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)
								#człon b
								x=214
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)

								#oświetlenie przedziałów
								if state['lights_compartments'] == 1:
									kolor=self.zolty
								else:
									kolor=self.szary
								draw.line([(31,222),(83,222)], fill=kolor, width=3)
								draw.line([(109,222),(163,222)], fill=kolor, width=3)
								draw.line([(187,222),(241,222)], fill=kolor, width=3)

								#pantografy
								if ((eimp_u1_pf & (cab == 1)) | (eimp_u1_pr & (cab == -1))): #przedni
									draw.line([(115,220),(107,213),(115,206),(122,213),(115,220)], fill=self.zolty, width=2)
									draw.line([(115,220),(115,206)], fill=self.zolty, width=2)
								else:
									draw.line([(115,220),(107,216),(115,214),(122,216),(115,220)], fill=self.bialy, width=2)
									draw.line([(115,220),(115,214)], fill=self.bialy, width=2)

								if ((eimp_u1_pf & (cab == -1)) | (eimp_u1_pr & (cab == 1))): #tylny
									draw.line([(155,220),(147,213),(155,206),(162,213),(155,220)], fill=self.zolty, width=2)
									draw.line([(155,220),(155,206)], fill=self.zolty, width=2)
								else:
									draw.line([(155,220),(147,216),(155,214),(162,216),(155,220)], fill=self.bialy, width=2)
									draw.line([(155,220),(155,214)], fill=self.bialy, width=2)

							if (pojazdy > 1):	

										#Ikona EZT 2
								obrazek.paste(self.ezt,(269, 218),self.ezt)
								draw.text((278,238), '2', fill=self.bialy, font=self.bardzo_maly_font)
								#Drzwi EZT2
								#człon a
								x=322
								if doors_ezt2:
									kolor = self.czerwony
									dx=10
								else:
									kolor = self.bialy
									dx=0
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)
								#człon s
								x=400
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)
								#człon b
								x=478
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)

								#oświetlenie przedziałów
								x=264
								if state['lights_compartments'] == 1:
									kolor=self.zolty
								else:
									kolor=self.szary
								draw.line([(x+31,222),(x+83,222)], fill=kolor, width=3)
								draw.line([(x+109,222),(x+163,222)], fill=kolor, width=3)
								draw.line([(x+187,222),(x+241,222)], fill=kolor, width=3)

								#pantografy
								if ((eimp_u2_pf & (cab == 1)) | (eimp_u2_pr & (cab == -1))):
									draw.line([(x+115,220),(x+107,213),(x+115,206),(x+122,213),(x+115,220)], fill=self.zolty, width=2)
									draw.line([(x+115,220),(x+115,206)], fill=self.zolty, width=2)
								else:
									draw.line([(x+115,220),(x+107,216),(x+115,214),(x+122,216),(x+115,220)], fill=self.bialy, width=2)
									draw.line([(x+115,220),(x+115,214)], fill=self.bialy, width=2)

								if ((eimp_u2_pf & (cab == -1)) | (eimp_u2_pr & (cab == 1))):
									draw.line([(x+155,220),(x+147,213),(x+155,206),(x+162,213),(x+155,220)], fill=self.zolty, width=2)
									draw.line([(x+155,220),(x+155,206)], fill=self.zolty, width=2)
								else:
									draw.line([(x+155,220),(x+147,216),(x+155,214),(x+162,216),(x+155,220)], fill=self.bialy, width=2)
									draw.line([(x+155,220),(x+155,214)], fill=self.bialy, width=2)

							if (pojazdy > 2):	

								#Ikona EZT 3
								obrazek.paste(self.ezt,(533, 218),self.ezt)
								draw.text((542,238), '3', fill=self.bialy, font=self.bardzo_maly_font)
								#Drzwi EZT3
								#człon a
								x=586
								if doors_ezt3:
									kolor = self.czerwony
									dx=10
								else:
									kolor = self.bialy
									dx=0
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)
								#człon s
								x=664
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)
								#człon b
								x=742
								draw.line([(x-dx,225),(x-15-dx,225),(x-15-dx,250),(x-dx,250),(x-dx,225)], fill=kolor, width=2)
								draw.line([(x-3-dx,228),(x-11-dx,228),(x-11-dx,239),(x-3-dx,239),(x-3-dx,228)], fill=kolor, width=2)
								draw.line([(x+15+dx,225),(x+dx,225),(x+dx,250),(x+15+dx,250),(x+15+dx,225)], fill=kolor, width=2)
								draw.line([(x+11+dx,228),(x+3+dx,228),(x+3+dx,239),(x+11+dx,239),(x+11+dx,228)], fill=kolor, width=2)

								#oświetlenie przedziałów
								x=528
								if state['lights_compartments'] == 1:
									kolor=self.zolty
								else:
									kolor=self.szary
								draw.line([(x+31,222),(x+83,222)], fill=kolor, width=3)
								draw.line([(x+109,222),(x+163,222)], fill=kolor, width=3)
								draw.line([(x+187,222),(x+241,222)], fill=kolor, width=3)

								#pantografy
								if ((eimp_u3_pf & (cab == 1)) | (eimp_u3_pr & (cab == -1))):
									draw.line([(x+115,220),(x+107,213),(x+115,206),(x+122,213),(x+115,220)], fill=self.zolty, width=2)
									draw.line([(x+115,220),(x+115,206)], fill=self.zolty, width=2)
								else:
									draw.line([(x+115,220),(x+107,216),(x+115,214),(x+122,216),(x+115,220)], fill=self.bialy, width=2)
									draw.line([(x+115,220),(x+115,214)], fill=self.bialy, width=2)

								if ((eimp_u3_pf & (cab == -1)) | (eimp_u3_pr & (cab == 1))):
									draw.line([(x+155,220),(x+147,213),(x+155,206),(x+162,213),(x+155,220)], fill=self.zolty, width=2)
									draw.line([(x+155,220),(x+155,206)], fill=self.zolty, width=2)
								else:
									draw.line([(x+155,220),(x+147,216),(x+155,214),(x+162,216),(x+155,220)], fill=self.bialy, width=2)
									draw.line([(x+155,220),(x+155,214)], fill=self.bialy, width=2)	


						if (self.aktyw>=21) and (self.tryb == 2):
							obrazek.paste(self.terminal_msg, (0, 0))		
							
				
							# rysujemy
							i = 0
							for msg in self.active_messages:
								if msg["id"] >= len(messages):
									continue
								message = messages[msg["id"]]
								time = msg["time"]

								obrazek.paste(self.terminal_msg_slice, (0, 34 + i * 39))
								self.print_left(draw, str(i), 11, 51 + i * 39, self.maly_font, self.bialy)
								self.print_left(draw, message["name"], 37, 50 + i * 39, self.font, message["color"])
								self.print_left(draw, time, 690, 50 + i * 39, self.font, message["color"])
								if i == 12: # wiecej niz 13 sie nie zmiesci
									break
								i += 1		

							

						if (self.aktyw>=21) and (self.tryb == 6):
							cab = state['cab']
							obrazek.paste(self.hamulce, (0, 0))		
							if int(state["ipsz"]) == 0:	
							
							
								#cylindry					
								#obroty wskazówek w radianach
								Ra1 = radians((state['eimp_pn1_bc']*36 - 107.62))
								srodek = (93, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra1)), srodek[1]-(r_s*cos(Ra1)))
								p_s = (srodek[0]+(1*(-sin(Ra1))), srodek[1]-(1*(-cos(Ra1))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zielonastrzalka, width=4)	
			
								self.print_center(draw, str('%.0f' % (state['eimp_pn1_bc'] * 100) ), 54,172, self.bardzo_maly_font, self.zielonastrzalka)															
								Ra2 = radians((state['eimp_pn2_bc']*36 - 107.62))
								srodek = (93, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra2)), srodek[1]-(r_s*cos(Ra2)))
								p_s = (srodek[0]+(1*(-sin(Ra2))), srodek[1]-(1*(-cos(Ra2))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.niebieskastrzalka, width=4)				
								self.print_center(draw, str('%.0f' % (state['eimp_pn2_bc'] * 100) ), 85,172, self.bardzo_maly_font, self.niebieskastrzalka)					
								Ra3 = radians((state['eimp_pn3_bc']*36 - 107.62))
								srodek = (93, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra3)), srodek[1]-(r_s*cos(Ra3)))
								p_s = (srodek[0]+(1*(-sin(Ra3))), srodek[1]-(1*(-cos(Ra3))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zoltastrzalka, width=4)		
								self.print_center(draw, str('%.0f' % (state['eimp_pn3_bc'] * 100) ), 116,172, self.bardzo_maly_font, self.zoltastrzalka)							
							
								#zasilanie					
								#obroty wskazówek w radianach
								Ra1 = radians((state['eimp_pn1_sp']*21.8 - 109.5))
								srodek = (93+399, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra1)), srodek[1]-(r_s*cos(Ra1)))
								p_s = (srodek[0]+(1*(-sin(Ra1))), srodek[1]-(1*(-cos(Ra1))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zielonastrzalka, width=4)				
								self.print_center(draw, str('%.0f' % (state['eimp_pn1_sp'] * 100) ), 54+399,172, self.bardzo_maly_font, self.zielonastrzalka)				
													
								Ra2 = radians((state['eimp_pn2_sp']*21.8 - 109.5))
								srodek = (93+399, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra2)), srodek[1]-(r_s*cos(Ra2)))
								p_s = (srodek[0]+(1*(-sin(Ra2))), srodek[1]-(1*(-cos(Ra2))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.niebieskastrzalka, width=4)	
								draw.ellipse([(75+399, 114), (112, 151)], fill=self.szary2)				
								self.print_center(draw, str('%.0f' % (state['eimp_pn2_sp'] * 100) ), 85+399,172, self.bardzo_maly_font, self.niebieskastrzalka)					
								Ra3 = radians((state['eimp_pn3_sp']*21.8 - 109.5))
								srodek = (93+399, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra3)), srodek[1]-(r_s*cos(Ra3)))
								p_s = (srodek[0]+(1*(-sin(Ra3))), srodek[1]-(1*(-cos(Ra3))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zoltastrzalka, width=4)			
								self.print_center(draw, str('%.0f' % (state['eimp_pn3_sp'] * 100) ), 116+399,172, self.bardzo_maly_font, self.zoltastrzalka)	
								
								
					

								
								#obciazenie								
								
								obcra = ((state['eimp_pn1_mass']) - 13.548) * 7.36			
								obcra2 = round(0.2 * obcra) * 5
								obcra3 = str('%.0f' % obcra2)								

								#obroty wskazówek w radianach
								obc_ra = radians((obcra2*0.36 - 107.62))
								srodek = (93+199, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(obc_ra)), srodek[1]-(r_s*cos(obc_ra)))
								p_s = (srodek[0]+(1*(-sin(obc_ra))), srodek[1]-(1*(-cos(obc_ra))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zielonastrzalka, width=4)		
								self.print_center(draw, obcra3, 54+199,172, self.bardzo_maly_font, self.zielonastrzalka)			
								
								
								obcs = ((state['eimp_pn2_mass']) - 20.122) * 5.69
								obcs2 = round(0.2 * obcs) * 5
								obcs3 = str('%.0f' % obcs2)								

								#obroty wskazówek w radianach
								obc_s = radians((obcs2*0.36 - 107.62))
								srodek = (93+199, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(obc_s)), srodek[1]-(r_s*cos(obc_s)))
								p_s = (srodek[0]+(1*(-sin(obc_s))), srodek[1]-(1*(-cos(obc_s))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.niebieskastrzalka, width=4)		
								self.print_center(draw, obcs3, 85+199,172, self.bardzo_maly_font, self.niebieskastrzalka)										
								
								obcrb = ((state['eimp_pn3_mass']) - 13.548) * 7.36							
								obcrb2 = round(0.2 * obcrb) * 5
								obcrb3 = str('%.0f' % obcrb2)								

								#obroty wskazówek w radianach
								obc_rb = radians((obcrb2*0.36 - 107.62))
								srodek = (93+199, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(obc_rb)), srodek[1]-(r_s*cos(obc_rb)))
								p_s = (srodek[0]+(1*(-sin(obc_rb))), srodek[1]-(1*(-cos(obc_rb))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zoltastrzalka, width=4)		
								self.print_center(draw, obcrb3, 116+199,172, self.bardzo_maly_font, self.zoltastrzalka)			
								
								draw.ellipse([(75+199, 114), (112+199, 151)], fill=self.szary2)					
								
								
								#sprezynka				
								#obroty wskazówek w radianach
								Ra1 = radians((state['eimp_pn1_spring']*21.8 - 109.5))
								srodek = (93+599, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra1)), srodek[1]-(r_s*cos(Ra1)))
								p_s = (srodek[0]+(1*(-sin(Ra1))), srodek[1]-(1*(-cos(Ra1))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zielonastrzalka, width=4)				
								self.print_center(draw, str('%.0f' % (state['eimp_pn1_spring'] * 100) ), 54+599,172, self.bardzo_maly_font, self.zielonastrzalka)				
													
			
								Ra3 = radians((state['eimp_pn3_spring']*21.8 - 109.5))
								srodek = (93+599, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra3)), srodek[1]-(r_s*cos(Ra3)))
								p_s = (srodek[0]+(1*(-sin(Ra3))), srodek[1]-(1*(-cos(Ra3))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zoltastrzalka, width=4)			
								self.print_center(draw, str('%.0f' % (state['eimp_pn3_spring'] * 100) ), 85+599,172, self.bardzo_maly_font, self.zoltastrzalka)			
								
								draw.ellipse([(75+599, 114), (112+599, 151)], fill=self.szary2)
								
								
								#ciezarki
								self.print_left(draw, str('%.1f' % (state['eimp_pn1_mass']) ), 204,483, self.sredni_font, self.zolty)	
								self.print_left(draw, str('%.1f' % (state['eimp_pn3_mass']) ), 740,483, self.sredni_font, self.zolty)									
								self.print_left(draw, str('%.1f' % (state['eimp_pn2_mass']) ), 472,483, self.sredni_font, self.zolty)									
								# siła zadana	
								silka_float = ( 1+min( 36, 1800/( speed+0.1 ) ) ) * min (state['eimp_t_pdb'] / 0.7, min (speed * 0.06, 1) )
								if silka_float < 0:
									silka == silka_float * -1								
								silka = str('%.0f' % silka_float)

								#Fzad
								#S
								self.print_left(draw, silka, 472,443, self.sredni_font, self.zolty)									
								self.print_left(draw, silka, 472,463, self.sredni_font, self.zolty)	

								#Ra
								self.print_left(draw, silka, 204,443, self.sredni_font, self.zolty)									
								self.print_left(draw, silka, 204,463, self.sredni_font, self.zolty)
								#Rb
								self.print_left(draw, silka, 740,443, self.sredni_font, self.zolty)									
								self.print_left(draw, silka, 740,463, self.sredni_font, self.zolty)		
								#% zad
								self.print_left(draw, str('%.0f' % (state['eimp_t_pdb'] * 100)), 204,503, self.sredni_font, self.zolty)					
								self.print_left(draw, str('%.0f' % (state['eimp_t_pdb'] * 100)), 472,503, self.sredni_font, self.zolty)	
								self.print_left(draw, str('%.0f' % (state['eimp_t_pdb'] * 100)), 740,503, self.sredni_font, self.zolty)	
								
								draw.ellipse([(75+399, 114), (112+399, 151)], fill=self.szary2)		
								draw.ellipse([(75, 114), (112, 151)], fill=self.szary2)										
	
							#RA
								#czujniki OK								
								draw.rectangle((7,241+19*2,130,257+19*2), self.zielony)										
								draw.rectangle((7,241+19*3,130,257+19*3), self.zielony)	
								draw.rectangle((7,241+19*4,130,257+19*4), self.zielony)		
								draw.rectangle((7,241+19*5,130,257+19*5), self.zielony)			
								draw.rectangle((7,241+19*6,130,257+19*6), self.zielony)	
								draw.rectangle((7,241+19*7,130,257+19*7), self.zielony)	


							
								#PN 
								if (indir_brake):
									draw.rectangle((7,241+19*8,130,257+19*8), self.zielony)	
								#BCU
								draw.rectangle((7,241+19*9,130,257+19*9), self.zielony)		

								#grzyb
								if (state['emergency_brake']) == 1:
									draw.rectangle((7+128,241,130+128,257), self.zielony)											
									
								#sprezyna
								if (brakes_1_spring_active == 0):
									draw.rectangle((7+128,241+19*3,130+128,257+19*3), self.zielony)		
								#start	
								if (dir_brake):
									draw.rectangle((7+128,241+19*6,130+128,257+19*6), self.zielony)		
									
					#S
								#ED	
								if state['eimp_c1_inv1_act'] == 0 or state['epfuse'] == 0:
									draw.rectangle((7+268,241,130+268,257), self.zielony)	
								if state['eimp_c1_inv2_act'] == 0 or state['epfuse'] == 0:				
									draw.rectangle((7+268,241+19,130+268,257+19), self.zielony)	
					
								#czujniki OK								
								draw.rectangle((7+268,241+19*2,130+268,257+19*2), self.zielony)										
								draw.rectangle((7+268,241+19*3,130+268,257+19*3), self.zielony)	
								draw.rectangle((7+268,241+19*4,130+268,257+19*4), self.zielony)		
								draw.rectangle((7+268,241+19*5,130+268,257+19*5), self.zielony)			
								draw.rectangle((7+268,241+19*6,130+268,257+19*6), self.zielony)	
								draw.rectangle((7+268,241+19*7,130+268,257+19*7), self.zielony)	


							
								#PN 
								if (indir_brake):
									draw.rectangle((7+268,241+19*8,130+268,257+19*8), self.zielony)	
	

								#BCU
								draw.rectangle((7+268,241+19*9,130+268,257+19*9), self.zielony)			
	
								#grzyb
								if (state['emergency_brake']) == 1:
									draw.rectangle((7+268+128,241,130+268+128,257), self.zielony)											
									
	
								#start	
								if (dir_brake):
									draw.rectangle((7+268+128,241+19*6,130+268+128,257+19*6), self.zielony)			
													
				#RB									
													
								#czujniki OK								
								draw.rectangle((7+536,241+19*2,130+536,257+19*2), self.zielony)										
								draw.rectangle((7+536,241+19*3,130+536,257+19*3), self.zielony)	
								draw.rectangle((7+536,241+19*4,130+536,257+19*4), self.zielony)		
								draw.rectangle((7+536,241+19*5,130+536,257+19*5), self.zielony)			
								draw.rectangle((7+536,241+19*6,130+536,257+19*6), self.zielony)	
								draw.rectangle((7+536,241+19*7,130+536,257+19*7), self.zielony)	


							
								#PN 
								if (indir_brake):
									draw.rectangle((7+536,241+19*8,130+536,257+19*8), self.zielony)	
								#BCU

								draw.rectangle((7+536,241+19*9,130+536,257+19*9), self.zielony)		

								#grzyb
								if (state['emergency_brake']) == 1:
									draw.rectangle((7+536+128,241,130+536+128,257), self.zielony)											
									
								#sprezyna
								if (brakes_3_spring_active == 0):
									draw.rectangle((7+536+128,241+19*3,130+536+128,257+19*3), self.zielony)		
								#start	
								if (dir_brake):
									draw.rectangle((7+536+128,241+19*6,130+536+128,257+19*6), self.zielony)										
									
								obrazek.paste(self.knorr, (0, 0), self.knorr)				
							if int(state["ipsz"]) == 1:							
							
								#RA							
								#obroty wskazówek w radianach
								Ra1 = radians((state['eimp_pn1_bc']*36 - 107.62))
								srodek = (93, 133)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra1)), srodek[1]-(r_s*cos(Ra1)))
								p_s = (srodek[0]+(1*(-sin(Ra1))), srodek[1]-(1*(-cos(Ra1))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zielonastrzalka, width=4)			
								self.print_center(draw, str('%.0f' % (state['eimp_pn1_bc'] * 100) ), 54,172, self.bardzo_maly_font, self.zielonastrzalka)							
								if (pojazdy >= 2):								
									Ra2 = radians((state['eimp_pn4_bc']*36 - 107.62))
									srodek = (93, 133)
									#długości wskazówek
									r_s = 82
									#punkty końcowe
									k_s = (srodek[0]+(r_s*sin(Ra2)), srodek[1]-(r_s*cos(Ra2)))
									p_s = (srodek[0]+(1*(-sin(Ra2))), srodek[1]-(1*(-cos(Ra2))))
									#rysowanie wskazówek
									draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.niebieskastrzalka, width=4)			
									self.print_center(draw, str('%.0f' % (state['eimp_pn4_bc'] * 100) ), 85,172, self.bardzo_maly_font, self.niebieskastrzalka)					
									if (pojazdy == 3):	
										Ra3 = radians((state['eimp_pn7_bc']*36 - 107.62))
										srodek = (93, 133)
										#długości wskazówek
										r_s = 82
										#punkty końcowe
										k_s = (srodek[0]+(r_s*sin(Ra3)), srodek[1]-(r_s*cos(Ra3)))
										p_s = (srodek[0]+(1*(-sin(Ra3))), srodek[1]-(1*(-cos(Ra3))))
										#rysowanie wskazówek
										draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zoltastrzalka, width=4)			
										self.print_center(draw, str('%.0f' % (state['eimp_pn7_bc'] * 100) ), 116,172, self.bardzo_maly_font, self.zoltastrzalka)						



								#S						
								#obroty wskazówek w radianach
								Ra1 = radians((state['eimp_pn2_bc']*36 - 107.62))
								srodek = (93, 133+171)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra1)), srodek[1]-(r_s*cos(Ra1)))
								p_s = (srodek[0]+(1*(-sin(Ra1))), srodek[1]-(1*(-cos(Ra1))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zielonastrzalka, width=4)	
		
								self.print_center(draw, str('%.0f' % (state['eimp_pn2_bc'] * 100) ), 54,172+171, self.bardzo_maly_font, self.zielonastrzalka)							
								if (pojazdy >= 2):								
									Ra2 = radians((state['eimp_pn5_bc']*36 - 107.62))
									srodek = (93, 133+171)
									#długości wskazówek
									r_s = 82
									#punkty końcowe
									k_s = (srodek[0]+(r_s*sin(Ra2)), srodek[1]-(r_s*cos(Ra2)))
									p_s = (srodek[0]+(1*(-sin(Ra2))), srodek[1]-(1*(-cos(Ra2))))
									#rysowanie wskazówek
									draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.niebieskastrzalka, width=4)	
		
									self.print_center(draw, str('%.0f' % (state['eimp_pn5_bc'] * 100) ), 85,172+171, self.bardzo_maly_font, self.niebieskastrzalka)					
									if (pojazdy == 3):	
										Ra3 = radians((state['eimp_pn8_bc']*36 - 107.62))
										srodek = (93, 133+171)
										#długości wskazówek
										r_s = 82
										#punkty końcowe
										k_s = (srodek[0]+(r_s*sin(Ra3)), srodek[1]-(r_s*cos(Ra3)))
										p_s = (srodek[0]+(1*(-sin(Ra3))), srodek[1]-(1*(-cos(Ra3))))
										#rysowanie wskazówek
										draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zoltastrzalka, width=4)	
		
										self.print_center(draw, str('%.0f' % (state['eimp_pn8_bc'] * 100) ), 116,172+171, self.bardzo_maly_font, self.zoltastrzalka)	



								#RB					
								#obroty wskazówek w radianach
								Ra1 = radians((state['eimp_pn3_bc']*36 - 107.62))
								srodek = (93, 133+341)
								#długości wskazówek
								r_s = 82
								#punkty końcowe
								k_s = (srodek[0]+(r_s*sin(Ra1)), srodek[1]-(r_s*cos(Ra1)))
								p_s = (srodek[0]+(1*(-sin(Ra1))), srodek[1]-(1*(-cos(Ra1))))
								#rysowanie wskazówek
								draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zielonastrzalka, width=4)	
		
								self.print_center(draw, str('%.0f' % (state['eimp_pn3_bc'] * 100) ), 54,172+341, self.bardzo_maly_font, self.zielonastrzalka)							
								if (pojazdy >= 2):								
									Ra2 = radians((state['eimp_pn6_bc']*36 - 107.62))
									srodek = (93, 133+341)
									#długości wskazówek
									r_s = 82
									#punkty końcowe
									k_s = (srodek[0]+(r_s*sin(Ra2)), srodek[1]-(r_s*cos(Ra2)))
									p_s = (srodek[0]+(1*(-sin(Ra2))), srodek[1]-(1*(-cos(Ra2))))
									#rysowanie wskazówek
									draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.niebieskastrzalka, width=4)	
		
									self.print_center(draw, str('%.0f' % (state['eimp_pn6_bc'] * 100) ), 85,172+341, self.bardzo_maly_font, self.niebieskastrzalka)					
									if (pojazdy == 3):	
										Ra3 = radians((state['eimp_pn9_bc']*36 - 107.62))
										srodek = (93, 133+341)
										#długości wskazówek
										r_s = 82
										#punkty końcowe
										k_s = (srodek[0]+(r_s*sin(Ra3)), srodek[1]-(r_s*cos(Ra3)))
										p_s = (srodek[0]+(1*(-sin(Ra3))), srodek[1]-(1*(-cos(Ra3))))
										#rysowanie wskazówek
										draw.line((p_s[0], p_s[1],k_s[0], k_s[1]),fill=self.zoltastrzalka, width=4)	
			
										self.print_center(draw, str('%.0f' % (state['eimp_pn9_bc'] * 100) ), 116,172+341, self.bardzo_maly_font, self.zoltastrzalka)	

								#zalHAM
								if (dir_or_indir_brake):
									draw.rectangle((248,63,359,79), self.zielony)

								#w0j
								if (dir_or_indir_brake) or spring_brake or (doors_ezt1 or doors_ezt2 or doors_ezt3 != 0):	
									draw.rectangle((248,143,359,159), self.zielony)				

								#clk	
								if ((state['seconds'] % 2) == 1):									
									draw.rectangle((248,204,359,219), self.zielony)												
								#ed1
								if state['eimp_c1_inv1_act'] == 1 and state['epfuse'] == 1:
									draw.rectangle((375,63,485,79), self.zielony)	
								#ed2
								if state['eimp_c1_inv2_act'] == 1 and state['epfuse'] == 1:
									draw.rectangle((375,84,485,100), self.zielony)				

								#med
								if ((dir_brake)&(epfuse)&((state['brake_op_mode_flag']) == 2)) and int(state["zadajnik"]) == 1 or ((dir_brake)&(epfuse)&((state['brake_op_mode_flag']) == 8)) and int(state["zadajnik"]) != 1:
									draw.rectangle((375,103,485,119), self.zielony)	

								obrazek.paste(self.ipsz, (0, 0), self.ipsz)			
								
								#ciezarki							
								self.print_center(draw, str('%.1f' % (state['eimp_pn1_mass']) ), 448,282, self.sredni_font, self.zolty)	
								self.print_center(draw, str('%.1f' % (state['eimp_pn3_mass']) ), 448,308, self.sredni_font, self.zolty)									
								self.print_center(draw, str('%.1f' % (state['eimp_pn2_mass']) ), 448,336, self.sredni_font, self.zolty)	

								
								#Fzad1
							
								self.print_left(draw, str('%.0f' % (state['eimp_t_fdb'] / 2) ), 681,282, self.sredni_font, self.zolty)	
								#Fzad2										
								self.print_left(draw, str('%.0f' % (state['eimp_t_fdb'] * 0.5) ), 681,308, self.sredni_font, self.zolty)		

									
								#silka									
								self.print_left(draw, str('%.2f' % (state['eimp_c1_prb'] * 0.8) ), 681,339, self.sredni_font, self.zolty)										
								
								#Freal1									 
								self.print_left(draw, str('%.0f' % (state['eimp_c1_frb'] * 0.5) ), 681,367, self.sredni_font, self.zolty)	
								#Freal2										 
								self.print_left(draw, str('%.0f' % (state['eimp_c1_frb'] * 0.5) ), 681,395, self.sredni_font, self.zolty)		
								#V
								self.print_left( draw, '%d' % speed, 681,423, self.sredni_font, self.zolty)		


								self.praca = self.praca + self.praca2 + 10 + 1* dt / 2
								if self.praca >= 256:
									self.praca = 0

								self.print_left( draw, str(self.praca), 681,451, self.sredni_font, self.zolty)																   			
								self.print_left( draw, str(self.praca), 681,479, self.sredni_font, self.zolty)		
								
								
								draw.ellipse([(75, 114), (112, 151)], fill=self.szary2)		
								draw.ellipse([(75, 114+171), (112, 151+171)], fill=self.szary2)		
								draw.ellipse([(75, 114+341), (112, 151+341)], fill=self.szary2)									
								
						if (self.aktyw>=21) and (self.tryb == 5) and int(state["zadajnik"]) != 3 and int(state["zadajnik"]) != 2:
							obrazek.paste(self.reflektory, (0, 0))	
							if (lights_front & 1): # lewe
								draw.ellipse((64, 162, 114, 211), fill = self.bialy)
							if (lights_front & 2): # lewe czerwone
								draw.ellipse((251, 162, 301, 211), fill = self.czerwony)
							if (lights_front & 4): # gorne
								draw.ellipse((373, 61, 423, 110), fill = self.bialy)
							if (lights_front & 16): # prawe
								draw.ellipse((688, 162, 737, 211), fill = self.bialy)							
							if (lights_front & 32): # prawe czerwone
								draw.ellipse((502, 162, 550, 211), fill = self.czerwony)		
								
							if (lights_rear & 16): # lewe
								draw.ellipse((64, 162+252, 114, 211+252), fill = self.bialy)
							if (lights_rear & 32): # lewe czerwone
								draw.ellipse((251, 162+252, 301, 211+252), fill = self.czerwony)
							if (lights_rear & 4): # gorne
								draw.ellipse((373, 61+252, 423, 110+252), fill = self.bialy)
							if (lights_rear & 1): # prawe
								draw.ellipse((688, 162+252, 737, 211+252), fill = self.bialy)							
							if (lights_rear & 2): # prawe czerwone
								draw.ellipse((502, 162+252, 550, 211+252), fill = self.czerwony)		

						
								
								
						### ikony na dole ekranu
						

						if int(state["zadajnik"]) == 3:
							self.print_center(draw, u"Status", 34,566, self.fontv16, self.bialy)
							self.print_center(draw, u"pociągu", 36,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Alarmy", 197,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Drzwi", 277,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Falowniki", 357,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Przetwor-", 437,566, self.fontv16, self.bialy)
							self.print_center(draw, u"nice", 437,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Hamulec", 517,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Sterownik", 677,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Data", 757,566, self.fontv16, self.bialy)
							self.print_center(draw, u"godzina", 757,587, self.fontv16, self.bialy)



						if int(state["zadajnik"]) == 2:
							self.print_center(draw, u"Status", 34,566, self.fontv16, self.bialy)
							self.print_center(draw, u"pociągu", 36,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Ogrzew.", 116,566, self.fontv16, self.bialy)
							self.print_center(draw, u"Klima.", 116,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Błędy", 197,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Drzwi", 277,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Falowniki", 357,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Przetwor-", 437,566, self.fontv16, self.bialy)
							self.print_center(draw, u"nice", 437,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Wyłącznik", 517,566, self.fontv16, self.bialy)
							self.print_center(draw, u"szybki", 517,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Hamulec", 597,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Sterownik", 677,575, self.fontv16, self.bialy)	

							self.print_center(draw, u"Ustaw.", 757,566, self.fontv16, self.bialy)
							self.print_center(draw, u"term.", 757,587, self.fontv16, self.bialy)


						if int(state["zadajnik"]) == 0 :
							self.print_center(draw, u"Status", 34,566, self.fontv16, self.bialy)
							self.print_center(draw, u"Pojazdu", 36,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Ogrzew.", 116,566, self.fontv16, self.bialy)
							self.print_center(draw, u"Klima.", 116,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Alarmy", 197,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Drzwi", 277,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Falowniki", 357,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Przetwor-", 437,566, self.fontv16, self.bialy)
							self.print_center(draw, u"nice", 437,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Refle-", 517,566, self.fontv16, self.bialy)
							self.print_center(draw, u"ktory", 517,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Hamulec", 597,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Sterownik", 677,575, self.fontv16, self.bialy)

						if int(state["zadajnik"]) == 1:
							self.print_center(draw, u"Status", 34,566, self.fontv16, self.bialy)
							self.print_center(draw, u"Pojazdu", 36,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Ogrzew.", 116,566, self.fontv16, self.bialy)
							self.print_center(draw, u"Klima.", 116,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Alarmy", 197,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Drzwi", 277,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Falowniki", 357,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Przetwor-", 437,566, self.fontv16, self.bialy)
							self.print_center(draw, u"nice", 437,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Refle-", 517,566, self.fontv16, self.bialy)
							self.print_center(draw, u"ktory", 517,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Hamulec", 597,575, self.fontv16, self.bialy)

							self.print_center(draw, u"Sterownik", 677,575, self.fontv16, self.bialy)						

							if((epfuse)):
								self.print_center(draw, u"Ham.ED", 757,566, self.fontv16, self.bialy)
								self.print_center(draw, u"wyłącz", 757,587, self.fontv16, self.bialy)
							else:
								self.print_center(draw, u"Ham.ED", 757,566, self.fontv16, self.bialy)
								self.print_center(draw, u"załącz", 757,587, self.fontv16, self.bialy)

						### koniec ikon na dole ekranu


						if (self.aktyw>=21) and (self.tryb == 4):	
							obrazek.paste(self.drzwi, (0, 0))
							if int(state["zadajnik"]) == 2 or int(state["zadajnik"]) == 3:
								self.print_center(draw, u"Status", 34,566, self.fontv16, self.bialy)
								self.print_center(draw, u"pociągu", 36,587, self.fontv16, self.bialy)
							else:
								self.print_center(draw, u"Status", 34,566, self.fontv16, self.bialy)
								self.print_center(draw, u"Pojazdu", 36,587, self.fontv16, self.bialy)

							self.print_center(draw, u"Drzwi", 277,575, self.fontv16, self.bialy)
							self.print_center(draw, u"załącz", 677,575, self.fontv16, self.bialy)								

							if state['doors_l_1']:
								draw.rectangle((636,45,646,55), fill=self.czerwony)
								draw.rectangle((658,45,668,55), fill=self.czerwony)			
								draw.rectangle((636-63,45,646-63,55), fill=self.czerwony)
								draw.rectangle((658-63,45,668-63,55), fill=self.czerwony)										
							else:
								draw.rectangle((664,55,640,46), fill=self.zielony)								
								draw.rectangle((664-63,55,640-63,46), fill=self.zielony)
							if state['doors_l_2']:
								draw.rectangle((636-184-89,45,646-184-89,55), fill=self.czerwony)
								draw.rectangle((658-184-89,45,668-184-89,55), fill=self.czerwony)			
								draw.rectangle((636-184,45,646-184,55), fill=self.czerwony)
								draw.rectangle((658-184,45,668-184,55), fill=self.czerwony)										
							else:
								draw.rectangle((664-184-89,55,640-184-89,46), fill=self.zielony)								
								draw.rectangle((664-184,55,640-184,46), fill=self.zielony)	
							if state['doors_l_3']:
								draw.rectangle((636-394-63,45,646-394-63,55), fill=self.czerwony)
								draw.rectangle((658-394-63,45,668-394-63,55), fill=self.czerwony)			
								draw.rectangle((636-394,45,646-394,55), fill=self.czerwony)
								draw.rectangle((658-394,45,668-394,55), fill=self.czerwony)										
							else:
								draw.rectangle((664-394-63,55,640-394-63,46), fill=self.zielony)								
								draw.rectangle((664-394,55,640-394,46), fill=self.zielony)	
								
							if state['doors_r_1']:
								draw.rectangle((636,45+58,646,55+58), fill=self.czerwony)
								draw.rectangle((658,45+58,668,55+58), fill=self.czerwony)			
								draw.rectangle((636-63,45+58,646-63,55+58), fill=self.czerwony)
								draw.rectangle((658-63,45+58,668-63,55+58), fill=self.czerwony)										
							else:
								draw.rectangle((664,55+58,640,46+58), fill=self.zielony)								
								draw.rectangle((664-63,55+58,640-63,46+58), fill=self.zielony)
							if state['doors_r_2']:
								draw.rectangle((636-184-89,45+58,646-184-89,55+58), fill=self.czerwony)
								draw.rectangle((658-184-89,45+58,668-184-89,55+58), fill=self.czerwony)			
								draw.rectangle((636-184,45+58,646-184,55+58), fill=self.czerwony)
								draw.rectangle((658-184,45+58,668-184,55+58), fill=self.czerwony)										
							else:
								draw.rectangle((664-184-89,55+58,640-184-89,46+58), fill=self.zielony)								
								draw.rectangle((664-184,55+58,640-184,46+58), fill=self.zielony)	
							if state['doors_r_3']:
								draw.rectangle((636-394-63,45+58,646-394-63,55+58), fill=self.czerwony)
								draw.rectangle((658-394-63,45+58,668-394-63,55+58), fill=self.czerwony)			
								draw.rectangle((636-394,45+58,646-394,55+58), fill=self.czerwony)
								draw.rectangle((658-394,45+58,668-394,55+58), fill=self.czerwony)										
							else:
								draw.rectangle((664-394-63,55+58,640-394-63,46+58), fill=self.zielony)								
								draw.rectangle((664-394,55+58,640-394,46+58), fill=self.zielony)		
							if (pojazdy >= 2):		
								obrazek.paste(self.drzwiezt2, (0, 157))		
								if state['doors_l_4']:
									draw.rectangle((636,45+157,646,55+157), fill=self.czerwony)
									draw.rectangle((658,45+157,668,55+157), fill=self.czerwony)			
									draw.rectangle((636-63,45+157,646-63,55+157), fill=self.czerwony)
									draw.rectangle((658-63,45+157,668-63,55+157), fill=self.czerwony)										
								else:
									draw.rectangle((664,55+157,640,46+157), fill=self.zielony)								
									draw.rectangle((664-63,55+157,640-63,46+157), fill=self.zielony	)
								if state['doors_l_5']:
									draw.rectangle((636-184-89,45+157,646-184-89,55+157), fill=self.czerwony)
									draw.rectangle((658-184-89,45+157,668-184-89,55+157), fill=self.czerwony)			
									draw.rectangle((636-184,45+157,646-184,55+157), fill=self.czerwony)
									draw.rectangle((658-184,45+157,668-184,55+157), fill=self.czerwony)										
								else:
									draw.rectangle((664-184-89,55+157,640-184-89,46+157), fill=self.zielony)								
									draw.rectangle((664-184,55+157,640-184,46+157), fill=self.zielony)	
								if state['doors_l_6']:
									draw.rectangle((636-394-63,45+157,646-394-63,55+157), fill=self.czerwony)
									draw.rectangle((658-394-63,45+157,668-394-63,55+157), fill=self.czerwony)			
									draw.rectangle((636-394,45+157,646-394,55+157), fill=self.czerwony)
									draw.rectangle((658-394,45+157,668-394,55+157), fill=self.czerwony)										
								else:
									draw.rectangle((664-394-63,55+157,640-394-63,46+157), fill=self.zielony)								
									draw.rectangle((664-394,55+157,640-394,46+157), fill=self.zielony)	

								if state['doors_r_4']:
									draw.rectangle((636,45+58+157,646,55+58+157), fill=self.czerwony)
									draw.rectangle((658,45+58+157,668,55+58+157), fill=self.czerwony)			
									draw.rectangle((636-63,45+58+157,646-63,55+58+157), fill=self.czerwony)
									draw.rectangle((658-63,45+58+157,668-63,55+58+157), fill=self.czerwony)										
								else:
									draw.rectangle((664,55+58+157,640,46+58+157), fill=self.zielony)								
									draw.rectangle((664-63,55+58+157,640-63,46+58+157), fill=self.zielony)
								if state['doors_r_5']:
									draw.rectangle((636-184-89,45+58+157,646-184-89,55+58+157), fill=self.czerwony)
									draw.rectangle((658-184-89,45+58+157,668-184-89,55+58+157), fill=self.czerwony)			
									draw.rectangle((636-184,45+58+157,646-184,55+58+157), fill=self.czerwony)
									draw.rectangle((658-184,45+58+157,668-184,55+58+157), fill=self.czerwony)										
								else:
									draw.rectangle((664-184-89,55+58+157,640-184-89,46+58+157), fill=self.zielony)								
									draw.rectangle((664-184,55+58+157,640-184,46+58+157), fill=self.zielony)	
								if state['doors_r_6']:
									draw.rectangle((636-394-63,45+58+157,646-394-63,55+58+157), fill=self.czerwony)
									draw.rectangle((658-394-63,45+58+157,668-394-63,55+58+157), fill=self.czerwony)			
									draw.rectangle((636-394,45+58+157,646-394,55+58+157), fill=self.czerwony)
									draw.rectangle((658-394,45+58+157,668-394,55+58+157), fill=self.czerwony)										
								else:
									draw.rectangle((664-394-63,55+58+157,640-394-63,46+58+157), fill=self.zielony)								
									draw.rectangle((664-394,55+58+157,640-394,46+58+157), fill=self.zielony)		
							if (pojazdy == 3):		
								obrazek.paste(self.drzwiezt3, (0, 313))									
								if state['doors_l_7']:
									draw.rectangle((636,45+313,646,55+313), fill=self.czerwony)
									draw.rectangle((658,45+313,668,55+313), fill=self.czerwony)			
									draw.rectangle((636-63,45+313,646-63,55+313), fill=self.czerwony)
									draw.rectangle((658-63,45+313,668-63,55+313), fill=self.czerwony)										
								else:
									draw.rectangle((664,55+313,640,46+313), fill=self.zielony)								
									draw.rectangle((664-63,55+313,640-63,46+313), fill=self.zielony)
								if state['doors_l_8']:
									draw.rectangle((636-184-89,45+313,646-184-89,55+313), fill=self.czerwony)
									draw.rectangle((658-184-89,45+313,668-184-89,55+313), fill=self.czerwony)			
									draw.rectangle((636-184,45+313,646-184,55+313), fill=self.czerwony)
									draw.rectangle((658-184,45+313,668-184,55+313), fill=self.czerwony)										
								else:
									draw.rectangle((664-184-89,55+313,640-184-89,46+313), fill=self.zielony)								
									draw.rectangle((664-184,55+313,640-184,46+313), fill=self.zielony)	
								if state['doors_l_9']:
									draw.rectangle((636-394-63,45+313,646-394-63,55+313), fill=self.czerwony)
									draw.rectangle((658-394-63,45+313,668-394-63,55+313), fill=self.czerwony)			
									draw.rectangle((636-394,45+313,646-394,55+313), fill=self.czerwony)
									draw.rectangle((658-394,45+313,668-394,55+313), fill=self.czerwony)										
								else:
									draw.rectangle((664-394-63,55+313,640-394-63,46+313), fill=self.zielony	)								
									draw.rectangle((664-394,55+313,640-394,46+313), fill=self.zielony)	

								if state['doors_r_7']:
									draw.rectangle((636,45+58+313,646,55+58+313), fill=self.czerwony)
									draw.rectangle((658,45+58+313,668,55+58+313), fill=self.czerwony)			
									draw.rectangle((636-63,45+58+313,646-63,55+58+313), fill=self.czerwony)
									draw.rectangle((658-63,45+58+313,668-63,55+58+313), fill=self.czerwony)										
								else:
									draw.rectangle((664,55+58+313,640,46+58+313), fill=self.zielony)								
									draw.rectangle((664-63,55+58+313,640-63,46+58+313), fill=self.zielony)
								if state['doors_r_8']:
									draw.rectangle((636-184-89,45+58+313,646-184-89,55+58+313), fill=self.czerwony)
									draw.rectangle((658-184-89,45+58+313,668-184-89,55+58+313), fill=self.czerwony)			
									draw.rectangle((636-184,45+58+313,646-184,55+58+313), fill=self.czerwony)
									draw.rectangle((658-184,45+58+313,668-184,55+58+313), fill=self.czerwony)										
								else:
									draw.rectangle((664-184-89,55+58+313,640-184-89,46+58+313), fill=self.zielony)								
									draw.rectangle((664-184,55+58+313,640-184,46+58+313), fill=self.zielony	)	
								if state['doors_r_9']:
									draw.rectangle((636-394-63,45+58+313,646-394-63,55+58+313), fill=self.czerwony)
									draw.rectangle((658-394-63,45+58+313,668-394-63,55+58+313), fill=self.czerwony)			
									draw.rectangle((636-394,45+58+313,646-394,55+58+313), fill=self.czerwony)
									draw.rectangle((658-394,45+58+313,668-394,55+58+313), fill=self.czerwony)										
								else:
									draw.rectangle((664-394-63,55+58+313,640-394-63,46+58+313), fill=self.zielony)								
									draw.rectangle((664-394,55+58+313,640-394,46+58+313), fill=self.zielony	)		

					else:
						self.tryb = 0
				tlo.paste(obrazek, (0,1440))
		else:
			self.aktyw = 0
			self.pasek = 0
		self.stan1 = state['universal1']
		self.stan2 = state['universal2']
		self.stan4 = state['universal4']
		self.stan5 = state['universal5']			
		self.stan6 = state['universal6']				
		return tlo
	
	
	def get_vehicle_name(self, name):
		# zasada dzialania: ucinamy wszystkie literki na koncu (zostaje tylko to co jest do ostatniej cyfry)
		digits = "0123456789"
		n = 0
		for i in range(len(name)):
			if name[i] in digits:
				n = i
		return name[:n+1]

# globale do komunikatow
activeMessages = []