#encoding: UTF-8

from PIL import ImageDraw, ImageFont, Image
from random import random, randint
from datetime import datetime, timedelta
from time import gmtime, strftime

# definicje kolorow
zolty = (180,170,110)
bialy = (245,245,245)
bialysrg = (245,245,245)
zielony = (115,170,92)
czarny = (0,0,0)
czarnysrg = (0,0,0)
czerwony = (175,100,70)
czerwony2 = (227,30,36)
pomarancz = (248,153,3)
niebieski = (51,198,247)
monitoring1 = (81,82,73)
monitoring2 = (98,188,77)
monitoring3 = (255,0,0)
monitoring4 = (204,204,204)
bladcan = (0,128,255)
szare = (71,71,71)

class web_renderer(abstractscreenrenderer):
	def __init__(self, lookup_path):
		# wczytanie obrazka
		self.moj_obrazek = self.openimage(lookup_path + "ekran/ekran")
		# wczytanie czcionki
		czcionka = "arial.ttf"
		czcionka2 = "dejavusans.ttf"
		czcionka2b = "dejavusans-bold.ttf"
		self.font = ImageFont.truetype('./fonts/' + czcionka, 22)
		self.font2 = ImageFont.truetype('./fonts/' + czcionka2, 22)
		self.font2a = ImageFont.truetype('./fonts/' + czcionka2, 14)	
		self.font2c = ImageFont.truetype('./fonts/' + czcionka2, 10)	
		self.font2b = ImageFont.truetype('./fonts/' + czcionka2b, 22)
		self.font2d = ImageFont.truetype('./fonts/' + czcionka2b, 34)
		self.maly_font = ImageFont.truetype('./fonts/' + czcionka, 17)
		self.maly_font2b = ImageFont.truetype('./fonts/' + czcionka2b, 17)
		self.bardzo_maly_font = ImageFont.truetype('./fonts/' + czcionka, 11)
		self.polduzy_font = ImageFont.truetype('./fonts/' + czcionka, 30)
		self.duzy_font = ImageFont.truetype('./fonts/' + czcionka, 60)
		self.duzy_font2b = ImageFont.truetype('./fonts/' + czcionka2b, 48)
		self.srg_arial = ImageFont.truetype('./fonts/arialbd.ttf', 36)
		self.srg_arial2 = ImageFont.truetype('./fonts/arialbd.ttf', 27)
		self.srg_arial3 = ImageFont.truetype('./fonts/arialbd.ttf', 24)
		self.arialbold16 = ImageFont.truetype('./fonts/arialbd.ttf', 16)
		self.arialbold14 = ImageFont.truetype('./fonts/arialbd.ttf', 14)
		self.arialbold9 = ImageFont.truetype('./fonts/arialbd.ttf', 9)		
		self.konsola = ImageFont.truetype('./fonts/unifont.ttf', 14)

		self.last_time_update = 0
		self.dzis = datetime.now().timetuple().tm_yday
		self.rok = datetime.now().year
		self.last_hour = 10
		self.temp = (random()*30) + 20

		self.prawy = Image.open(lookup_path +"ekran/27web/ekranboczny.png")
		self.tacho = Image.open(lookup_path +"ekran/27web/ekranglowny.png")
		self.lista = Image.open(lookup_path +"ekran/27web/lista.png")		
		self.monitoring = Image.open(lookup_path +"ekran/27web/monitoring.png") 
		#self.bootowanie_ente = Image.open("./textures/tabor/python/ente_boot.png")
		self.tacho_opt = Image.open(lookup_path +"ekran/27web/opt.png")
		self.temp_aktyw = Image.open(lookup_path +"ekran/27web/temp_aktyw.png")
		self.komunikaty = Image.open(lookup_path +"ekran/27web/komunikaty.png")		
		
		bootowanie2 = Image.open("./textures/tabor/python/ente_boot.png")
		self.boot2 = bootowanie2.resize((574, 459), Image.ANTIALIAS)			
		#jest:
		self.kier_P = Image.open(lookup_path + "ekran/27web/kier_przod.png")
		self.kier_t = Image.open(lookup_path + "ekran/27web/kier_tyl.png")
		self.kier_0 = Image.open(lookup_path + "ekran/27web/kier_0.png")		
		self.panto_m_a = Image.open(lookup_path + "ekran/27web/pantograf.png")
		self.panto_dol = Image.open(lookup_path + "ekran/27web/pantograf_dol.png")
		self.hamulec_tarcza2 = self.openimage(lookup_path + "ekran/27web/zahamowane_zestawy")
		self.stopien_gora = self.openimage(lookup_path + "ekran/27web/stopien_gora")
		self.ikonka_ws = Image.open(lookup_path + "ekran/27web/ws_zalaczony.png")
		self.stopien_dol = self.openimage(lookup_path + "ekran/27web/stopien_dol")
		self.stopien_gora = self.openimage(lookup_path + "ekran/27web/stopien_gora")
		self.drzwi_gora = Image.open(lookup_path + "ekran/27web/drzwi_gora.png")
		self.drzwi_dol = Image.open(lookup_path + "ekran/27web/drzwi_dol.png")
		self.ludzik_akt = Image.open(lookup_path + "ekran/27web/ludzik_akt.png")				
		self.hamulec = Image.open(lookup_path + "ekran/27web/hamulec.png")
		self.piasek = Image.open(lookup_path + "ekran/27web/piasek.png")
		self.sprezarka_pomocnicza = Image.open(lookup_path + "ekran/27web/sprezarka_pomocnicza.png")
		self.ladowanie = Image.open(lookup_path + "ekran/27web/ladowanie.png")
		self.osie = Image.open(lookup_path + "ekran/27web/osie.png")
		self.grzybek = Image.open(lookup_path + "ekran/27web/grzybek.png")		
		self.oswietlenie = Image.open(lookup_path + "ekran/27web/oswietlenie.png")	
		self.hamulec_nastawa_p = Image.open(lookup_path + "ekran/27web/hamulec_nastawa_p.png")
		self.reflektory_przyc = Image.open(lookup_path + "ekran/27web/reflektory_przyc.png")
		self.ikonka_sprezarka = Image.open(lookup_path + "ekran/27web/ikonka_sprezarka.png")
		self.ikonka_przetwornica = self.openimage(lookup_path + "ekran/27web/ikonka_przetwornica")
		self.ikonka_przetwornica_pom = self.openimage(lookup_path + "ekran/27web/przetwornica_pom")		
		self.osw_przyc = self.openimage(lookup_path + "ekran/27web/osw_przycisk")			
		self.bootowanie = Image.open(lookup_path +"ekran/bootowanie.png")	
		self.tempomat_klaw = Image.open(lookup_path + "ekran/27web/klawiatura_tempomat.png")
		self.brak_kabiny = Image.open(lookup_path + "ekran/27web/brak_kabiny.png")
		self.drzwi_zgoda = Image.open(lookup_path + "ekran/27web/drzwi_zgoda.png")
		self.aktyw = 0
		
						
		self.lookup_path = lookup_path
		self.kilometry = (random()*1000)+(self.rok-2019)*35000+self.dzis*250
		self.kilometry_z = 0
		self.read_tacho = False
		
		self.awaria = False
		
		self.woda = randint(5, 95)	
		self.fekalia = randint(0, 95)		
		self.rejestrator = randint(800, 2500)	
		self.tryb = 0
		self.stan6 = False
		self.stan7 = False
		self.stan8 = False
		self.klikniete = -1
		
		
		self.awaria1 = randint(0, 400)				
		self.awaria2 = randint(0, 350)
		self.awaria3 = randint(0, 250)
		self.awaria4 = randint(0, 1000)
		self.awaria5 = randint(0, 800)
		self.awaria6 = randint(0, 200)
		self.awaria7 = randint(0, 450)
		self.awaria8 = randint(0, 750)
		self.awaria9 = randint(0, 850)		
		self.awaria10 = randint(0, 500)		
		self.awaria11 = randint(0, 500)		
		self.awaria12 = randint(0, 500)				
		self.awaria13 = randint(0, 500)				
		self.awaria14 = randint(0, 500)				
		self.awaria15 = randint(0, 500)		
		self.awaria16 = randint(0, 500)	
		
		
	def _render(self, state):
		awaria1 = (self.awaria1 < 10)		
		awaria2 = (self.awaria2 < 10)		
		awaria3 = (self.awaria3 < 10)				
		awaria4 = (self.awaria4 < 10)				
		awaria5 = (self.awaria5 < 10)				
		awaria6 = (self.awaria6 < 10)				
		awaria7 = (self.awaria7 < 10)				
		awaria8 = (self.awaria8 < 10)				
		awaria9 = (self.awaria9 < 10)				
		awaria10 = (self.awaria10 < 10)			
		awaria11 = (self.awaria11 < 10)			
		awaria12 = (self.awaria12 < 10)			
		awaria13 = (self.awaria13 < 10)	
		awaria14 = (self.awaria14 < 10)	
		awaria15 = (self.awaria15 < 10)	
		awaria16 = (self.awaria16 < 10)			
		
		dt = 0
		speed = float(state['velocity'])
		if speed > 180:
			speed = 180
		# czas = READY
		if state['seconds'] != self.last_time_update:
			dt = state['seconds'] - self.last_time_update
			if dt < 0:
				dt+=60
			self.kilometry += dt*speed * 0.0002778
			self.last_time_update = state['seconds']
		# kopia obrazka na potrzeby tego jednego renderowania
		obrazek = self.moj_obrazek.copy()
		# chcemy rysowac po teksturze pulpitu
		draw = ImageDraw.Draw(obrazek)
		if (state['battery'] + state['converter']):
				self.aktyw += dt
				# czas = READY
				seconds = state['seconds']
				minutes = state['minutes']
				hours = state['hours']
				czas = str(hours) + ":" 
				if minutes<10:
					czas = czas + "0" + str(minutes) + ":"
				else:
					czas = czas + str(minutes) + ":"
				if seconds<10:
					czas = czas + "0" +str(seconds)
				else:
					czas = czas + str(seconds)
				#RG 5000P
				if hours<10:
					czas2 = "0" + czas
				else:
					czas2 = czas
				if self.last_hour == 23 and hours == 0:
					self.dzis = self.dzis+1 # wlasnie wybila polnoc
				self.last_hour = hours
				data = datetime(self.rok, 1, 1) + timedelta(self.dzis - 1)
				data2 = data.strftime("%d-%m-%y")
				data = data.strftime("%d/%m/%Y")

				war_odl_s_1_a = state['eimp_c1_inv1_allow'] == 0
				war_odl_s_2_a = state['eimp_c1_inv2_allow'] == 0
				war_odl_s_3_c = state['eimp_c2_inv1_allow'] == 0
				war_odl_s_4_c = state['eimp_c2_inv2_allow'] == 0
				war_odl_s_5_f = state['eimp_c3_inv1_allow'] == 0
				war_odl_s_6_f = state['eimp_c3_inv2_allow'] == 0
				war_odl_a_1_a = state['eimp_c1_inv1_error'] == 1
				war_odl_a_2_a = state['eimp_c1_inv2_error'] == 1
				war_odl_a_3_c = state['eimp_c2_inv1_error'] == 1
				war_odl_a_4_c = state['eimp_c2_inv2_error'] == 1
				war_odl_a_5_f = state['eimp_c3_inv1_error'] == 1
				war_odl_a_6_f = state['eimp_c3_inv2_error'] == 1				

				# symulacja zepsucia ekranu
				# 0.0000002 szansy co odswiezenie daje nam znikoma szanse na kazdej sluzbie, ale to moze sie stac
				# kazde zresetowanie daje nam 40% szansy na "zbicie zepsucia"
				if self.awaria:
					obrazek.paste(self.brak_kabiny, (0, 0))	
					draw.text((131, 5),"-100", font = self.maly_font2b, fill = bialy)
					draw.text((135, 38), "0", font = self.maly_font2b, fill = bialy)
					draw.text((203, 5), "0", font = self.maly_font2b, fill = bialy)
					draw.text((210, 38), "0", font = self.maly_font2b, fill = bialy)
					draw.text((297, 5), "0.00", font = self.maly_font2b, fill = bialy)
					draw.text((296, 38), "0.00", font = self.maly_font2b, fill = bialy)	
					draw.text((387, 5), "0", font = self.maly_font2b, fill = bialy)				
					self.aktyw = 1 # gdy reset sie nie udal, musimy recznie przestawic aktywacje by byla znowu szansa na zbicie awarii
				else:
					
					# losuj zepsucie
					self.awaria = self.aktyw >= 60 and random() < 0.000003
					
					# Liczenie pojazdow
					pojazdy = 1
					unit_no = state['unit_no']
					car_no = state['car_no']
					if (unit_no == 2) and (car_no == 7):
						pojazdy = 2
					if (unit_no == 2) and (car_no == 6):
						pojazdy = 3
					if (unit_no == 2) and (car_no == 5):
						pojazdy = 4			
					if (unit_no >= 3):
						pojazdy = 5	
						
						

					mr1 = float(state['eimp_c1_fr'])
					mr2 = float(state['eimp_c2_fr'])
					mr3 = float(state['eimp_c3_fr'])
					mr4 = float(state['eimp_c4_fr'])
					mz = float(state['eimp_t_pd'])


					#draw.text((272,6), czas, fill=bialy, font=self.font)

					war_cab = state['cab']
					lights_front = state['lights_train_front']
					lights_rear = state['lights_train_rear']
					if self.aktyw<60:
						war_prawy = False
						war_tacho = False
					else:
						war_prawy = True
						war_tacho = True
					war_monitoring = True
					war_pozar = False
					war_uziom = False
					war_a = False
					awaria = False					
					war_a2 = False
					war_pozar2 = False
					war_uziom2 = False
					war_a = False
					if (state['light_level']<0.35):
						war_osw = True
					else:
						war_osw = False
					war_p = False
					war_inw = False
					war_piorun = False 
					war_p2 = False
					war_inw2 = False
					war_piorun2 = False 
					war_piach = state['sanding']
					war_poslizg_s = state['slip_1']
					war_sos = False
					war_sos2 = False
					war_kier_P = state['direction'] == 1
					war_kier_t = state['direction'] == -1
					war_kier_0 = state['direction'] == 0				
					if (war_cab == 1):
						war_panto_m_a = state['eimp_u1_pf']
						war_panto_m_a2 = state['eimp_u2_pf']
					else:
						war_panto_m_a = state['eimp_u1_pr']
						war_panto_m_a2 = state['eimp_u2_pr']
					war_uziom_m_a = False
					war_ws_m_a = state['eimp_c1_ms']
					war_ws_m_a2 = state['eimp_c3_ms']
					war_wylacznik_szybki = war_ws_m_a or war_ws_m_a2 
					war_kompresor_a = state['eimp_u1_comp_w']
					war_400v_m_a = False
					war_bat_m_a = (state['eimp_c1_conv'] == 1)
					war_przetwornica_a = (state['eimp_c1_inv1_act'] == 0) & (state['eimp_c1_inv2_act'] == 0) & (state['eimp_c2_inv1_act'] == 0) & (state['eimp_c2_inv2_act'] == 0) & (state['eimp_c3_inv1_act'] == 0) & (state['eimp_c3_inv2_act'] == 0)
					war_ham_pos_a = state['brakes_1_spring_active']
					war_ham_pos_b = state['brakes_2_spring_active']
					war_ham_pos_c = state['brakes_3_spring_active']
					war_ham_pos_d = state['brakes_4_spring_active']
					war_ham_pos_e = state['brakes_5_spring_active']
					war_ham_pos_f = state['brakes_6_spring_active']					
					war_hamulec_1 = state['eimp_pn1_bc'] > 0.1
					war_hamulec_2 = state['eimp_pn2_bc'] > 0.1
					war_hamulec_3 = state['eimp_pn3_bc'] > 0.1
					war_hamulec_4 = state['eimp_pn4_bc'] > 0.1
					war_hamulec_5 = state['eimp_pn5_bc'] > 0.1
					war_hamulec_6 = state['eimp_pn6_bc'] > 0.1
			
					war_hamulec = war_hamulec_1 or war_hamulec_2 or war_hamulec_3 or war_hamulec_4 or war_hamulec_5 or war_hamulec_6
					war_inw_m_a = False
					war_hamulec_sprezynowy = war_ham_pos_a or war_ham_pos_b or war_ham_pos_c or war_ham_pos_d or war_ham_pos_e or war_ham_pos_f
					war_a_m_a = False
					war_sos_m_a = False
					war_awaria_a = False

					
					war_cisnienie_b = state['eimp_pn2_bc'] > 0.1
					war_cisnienie_c = state['eimp_pn3_bc'] > 0.1
					war_cisnienie_d = state['eimp_pn4_bc'] > 0.1
					
					if (war_cab == 1):
						war_panto_m_d = state['eimp_u1_pr']
					else:
						war_panto_m_d = state['eimp_u1_pf']
					war_uziom_m_d = False
					war_kompresor_d = state['eimp_u1_comp_w']
					war_400v_m_d = False
					war_bat_m_d = (state['eimp_c2_batt'] == 1) & (state['eimp_c2_conv'] == 0)
					war_przetwornica_d = (state['eimp_c2_inv1_act'] == 0) & (state['eimp_c2_inv2_act'] == 0)
					war_odl_s_1_d = False
					war_odl_s_2_d = False
					war_inw_m_d = False
					war_a_m_d = False
					war_sos_m_d = False
					war_awaria_d = False

					war_400v = war_400v_m_a | war_400v_m_d

					war_c1_d1P = state['doors_r_1']
					war_c1_d2L = state['doors_l_1']
					war_c1_d3P = state['doors_r_2']
					war_c1_d4L = state['doors_l_2']
					war_c2_d5P = state['doors_r_3']
					war_c2_d6L = state['doors_l_3']
					war_c2_d7P = state['doors_r_4']
					war_c2_d8L = state['doors_l_4']
					war_c3_d9P = state['doors_r_5']
					war_c3_d10L = state['doors_l_5']
					war_c3_d11P = state['doors_r_6']
					war_c3_d12L = state['doors_l_6']	
					war_c4_d13P = state['doors_r_7']
					war_c4_d14L = state['doors_l_7']
					war_c4_d15P = state['doors_r_8']
					war_c4_d16L = state['doors_l_8']
					war_c5_d17P = state['doors_r_9']
					war_c5_d18L = state['doors_l_9']
					war_c5_d19P = state['doors_r_10']
					war_c5_d20L = state['doors_l_10']
					war_c6_d21P = state['doors_r_11']
					war_c6_d22L = state['doors_l_11']
					war_c6_d23P = state['doors_r_12']
					war_c6_d24L = state['doors_l_12']	


					war_c1_ds1P = state['doorstep_r_1']
					war_c1_ds2L = state['doorstep_l_1']
					war_c1_ds3P = state['doorstep_r_2']
					war_c1_ds4L = state['doorstep_l_2']
					war_c2_ds5P = state['doorstep_r_3']
					war_c2_ds6L = state['doorstep_l_3']
					war_c2_ds7P = state['doorstep_r_4']
					war_c2_ds8L = state['doorstep_l_4']
					war_c3_ds9P = state['doorstep_r_5']
					war_c3_ds10L = state['doorstep_l_5']
					war_c3_ds11P = state['doorstep_r_6']
					war_c3_ds12L = state['doorstep_l_6']	
					war_c4_ds13P = state['doorstep_r_7']
					war_c4_ds14L = state['doorstep_l_7']
					war_c4_ds15P = state['doorstep_r_8']
					war_c4_ds16L = state['doorstep_l_8']
					war_c5_ds17P = state['doorstep_r_9']
					war_c5_ds18L = state['doorstep_l_9']
					war_c5_ds19P = state['doorstep_r_10']
					war_c5_ds20L = state['doorstep_l_10']
					war_c6_ds21P = state['doorstep_r_11']
					war_c6_ds22L = state['doorstep_l_11']
					war_c6_ds23P = state['doorstep_r_12']
					war_c6_ds24L = state['doorstep_l_12']	
					
					mainctrl_pos = state['mainctrl_pos']
					
					war_speedctrl = state['speedctrl']
					war_speedctrlpower = state['speedctrlpower']

				#TŁA
					if (war_tacho == False):
						draw.rectangle((664,0,1464,800), fill=czarny)
						if self.aktyw >= 0:
							draw.text((670,1), 'EXT FS on hda1, internal journal', fill=bialy, font=self.konsola)
						if self.aktyw >= 1:
							draw.text((1370,1), '[    OK    ]', fill=zielony, font=self.konsola)
							draw.text((670,15), 'Recording existing mounts in /etc/mtab...', fill=bialy, font=self.konsola)
						if self.aktyw >= 2:
							draw.text((1370,15), '[    OK    ]', fill=zielony, font=self.konsola)
						if self.aktyw >= 4:
							draw.text((670,29), 'Mounting remaining file systems...', fill=bialy, font=self.konsola)
						if self.aktyw >= 6:
							draw.text((670,44), 'kjournald starting. Commit interval 5 seconds', fill=bialy, font=self.konsola)	
						if self.aktyw >= 11:
							draw.text((670,58), 'EXT3 FS on hda2, internal journal', fill=bialy, font=self.konsola)	
						if self.aktyw >= 12:
							draw.text((670,72), 'EXT3-fs: recovery complete', fill=bialy, font=self.konsola)
							draw.text((670,86), 'EXT3-fs: mounted filesystem with ordeded data mode', fill=bialy, font=self.konsola)	
						if self.aktyw >= 13:
							draw.text((670,100), 'kjournald starting. Commit interval 5 seconds', fill=bialy, font=self.konsola)
						if self.aktyw >= 18:
							draw.text((670,114), 'EXT3 FS on hda3, internal journal', fill=bialy, font=self.konsola)	
						if self.aktyw >= 19:
							draw.text((670,128), 'EXT3-fs: recovery complete', fill=bialy, font=self.konsola)
							draw.text((670,142), 'EXT3-fs: mounted filesystem with ordeded data mode', fill=bialy, font=self.konsola)
						if self.aktyw >= 20:
							draw.text((670,156), 'Remounting root file system in read-only mode...', fill=bialy, font=self.konsola)	
						if self.aktyw >= 21:
							draw.text((670,170), 'Activating all swap files/partitions...', fill=bialy, font=self.konsola)	
						if self.aktyw >= 23:
							draw.text((1370,170), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,184), 'Cleaning file system: /tmp /var/lock /var/run', fill=bialy, font=self.konsola)
						if self.aktyw >= 27:
							draw.text((1370,184), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,198), 'Setting system clock...', fill=bialy, font=self.konsola)
							draw.text((1370,198), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,212), 'Loading keymap: /lib/kbd/keymaps/i386/qwerty/us.map.gz...', fill=bialy, font=self.konsola)
							draw.text((1370,212), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,226), 'Setting screen font to lat1-16...', fill=bialy, font=self.konsola)
							draw.text((1370,226), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,240), 'Bringing up the loopback interface...', fill=bialy, font=self.konsola)	
							draw.text((1370,240), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,254), 'Setting hostname to pixy...', fill=bialy, font=self.konsola)
							draw.text((1370,254), '[    OK    ]', fill=zielony, font=self.konsola)	
						if self.aktyw >= 28:
							draw.text((670,268), 'INIT: Entering runlevel: 3', fill=bialy, font=self.konsola)							
						if self.aktyw >= 30:
							draw.text((670,282), 'Starting system lg daemon...', fill=bialy, font=self.konsola)	
						if self.aktyw >= 33:
							draw.text((1370,282), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,296), 'Starting kernel lg daemon...', fill=bialy, font=self.konsola)	
						if self.aktyw >= 35:
							draw.text((1370,296), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,310), 'Bringing up the eth0 interface...', fill=bialy, font=self.konsola)
							draw.text((670,324), 'e100: eth0: e100 watchdog: link up, 100MBps, half-duplex', fill=bialy, font=self.konsola)	
						if self.aktyw >= 36:
							draw.text((670,338), 'Adding IPv4 address 10.1.1.15 to the eth0 interface...', fill=bialy, font=self.konsola)	
						if self.aktyw >= 37:
							draw.text((1370,338), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,352), 'Setting up default gateway...', fill=bialy, font=self.konsola)
						if self.aktyw >= 38:
							draw.text((1370,352), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,366), 'Adding IPv4 address 192.168.1.2 to the eth0 interface....', fill=bialy, font=self.konsola)
						if self.aktyw >= 39:
							draw.text((1370,366), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,380), 'Gateway already setup: skipping.', fill=zolty, font=self.konsola)	
							draw.text((1370,380), '[   WARN   ]', fill=zolty, font=self.konsola)	
						if self.aktyw >= 40:
							draw.text((670,394), 'configure eth0', fill=bialy, font=self.konsola)	
							draw.text((670,408), 'Insert pcan module...', fill=bialy, font=self.konsola)
						if self.aktyw >= 42:
							draw.text((670,422), 'pcan: Release_20080220_n', fill=bialy, font=self.konsola)	
							draw.text((670,436), 'pcan: driver config [mod] [isa]', fill=bialy, font=self.konsola)
							draw.text((670,450), 'pcan: isa device minor 8 expected (io=0x0340, irq=5)', fill=bialy, font=self.konsola)	
							draw.text((670,464), 'pcan: major 254.', fill=bialy, font=self.konsola)
						if self.aktyw >= 43:
							draw.text((670,480), 'Make pcan device nodes...', fill=bialy, font=self.konsola)
						if self.aktyw >= 45:
							draw.text((1370,480), '[    OK    ]', fill=zielony, font=self.konsola)	
							draw.text((670,494), 'Starting SSH server', fill=bialy, font=self.konsola)
							draw.text((670,508), '_', fill=bialy, font=self.konsola)	
					if (war_monitoring) and state['universal4'] == 0:
						draw.rectangle((1469,564,2044,1022), fill=czarny)
						if self.aktyw >= 0:
							obrazek.paste(self.boot2, (1469, 564))
						if self.aktyw >= 95:
							obrazek.paste(self.monitoring, (1469, 564))
					if self.aktyw>60:					
						obrazek.paste(self.tacho, (664, 0))			
					#TACHOMETR
						rotate = speed * 360 / 289
						rad = radians(rotate)
						srodek_tacho = (203+664, 254)
						point = (0,66)
						rotated_point = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
						point = (0,175)
						rotated_point2 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
						# rysujemy 
						draw.line(rotated_point + rotated_point2, fill = czerwony2, width = 7)

						# duzy tekst z predkoscia w srodku = READY
						msg = '%d' % speed
						self.print_center(draw, msg, srodek_tacho[0],srodek_tacho[1]-15, self.duzy_font2b, bialy)
						#zegarek i datownik
						self.print_center(draw, data2, 520+664, 15, self.font2d, bialy)
						self.print_center(draw, czas2, 312+664, 15, self.font2d, bialy)
						if (self.read_tacho == False):
							try:
								tempkm = 0
								with open(self.lookup_path + "/kilometry/" + state['name'][:-1] + "_przebieg.txt", "r") as self.tacho_file:
									tempkm = self.tacho_file.read()
									if tempkm == "":
										raise IOError
							except IOError:
								tempkm = (random()*1000)+(self.rok-2018)*16500+self.dzis*450
							finally:
								self.kilometry = float(tempkm)
								self.kilometry_z = self.kilometry
								with open(self.lookup_path + "/kilometry/" + state['name'][:-1] + "_przebieg.txt", "w") as self.tacho_file:
									self.tacho_file.write(str(tempkm))
							#zapis przebiegu
							self.read_tacho = True
						else:

							if self.kilometry>(self.kilometry_z + (0.1+0.005*speed)):
								with open(self.lookup_path + "/kilometry/" + state['name'][:-1] + "_przebieg.txt", 'w') as tacho_file:
									tacho_file.write(str(self.kilometry))
									self.kilometry_z = self.kilometry

						#przebieg
						tekst = str(int(self.kilometry))
						self.print_center(draw, tekst + " km", 306+664, 411, self.font2a, bialy)
						self.print_center(draw, "65535", 470+664, 411, self.font2a, bialy)
						nazwa = state['car_name1']
						self.print_center(draw, str(int(nazwa[5:8])), 600+664, 411, self.font2a, bialy)
						self.print_center(draw, str(self.rejestrator)+" h", 722+664, 411, self.font2a, bialy)

						sila1 = state['eimp_c1_fr']
						if sila1 > 0:
							slupek1 = (51,198,247)
						else:
							slupek1 = (255,100,100)
						pos = 190 - (sila1 * 280 / 700)
						draw.rectangle((384+664,pos,404+664,190), fill=slupek1)
						
						sila2 = state['eimp_c2_fr']
						if sila2 > 0:
							slupek2 = (51,198,247)
						else:
							slupek2 = (255,100,100)
						pos = 190 - (sila2 * 280 / 700)
						draw.rectangle((438+664,pos,458+664,190), fill=slupek2)
						
						sila3 = state['eimp_c3_fr']
						if sila3 > 0:
							slupek3 = (51,198,247)
						else:
							slupek3 = (255,100,100)						
						pos = 190 - (sila3 * 280 / 700)
						draw.rectangle((494+664,pos,514+664,190), fill=slupek3)				
													
						# slupek procentu siły zadanej jazdy
						procent = state['eimp_t_pd']
						if procent > 0:
							slupek4 = (51,198,247)
						else:
							slupek4 = (255,100,100)						
						pos = 190 - (procent * 85)
						draw.rectangle((548+664,190,568+664,pos), fill=slupek4)						
						procent=procent*100

						napiecie = state['eimp_c1_uhv']
						if napiecie < 0:
							napiecie = 0					
						if napiecie > 0:
							slupek5 = (51,198,247)
						else:
							slupek5 = (255,100,100)																
						pos = 275 - (napiecie * 169 / 5000)-2
						draw.rectangle((615+664,pos,635+664,275), fill=slupek5)
						
						prad = state['eimp_c1_ihv']
						if prad > 0:
							slupek6 = (51,198,247)
						else:
							slupek6 = (255,100,100)								
						pos = 190 - (prad * 56 / 700)
						draw.rectangle((665+664,pos,685+664,190), fill=slupek6)						
						
						#mierniki
						m_data = [
							{"v":abs(state["eimp_c1_fr"]),"vmin":0,"vmax":200,"x":392},
							{"v":abs(state["eimp_c2_fr"]),"vmin":0,"vmax":200,"x":450},
							{"v":abs(state["eimp_c3_fr"]),"vmin":0,"vmax":200,"x":504},
							{"v":state["eimp_t_pd"] * 100,"vmin":-100,"vmax":100,"x":563},
							{"v":state["voltage"],"vmin":0,"vmax":5000,"x":622},
							{"v":abs(state["eimp_c1_ihv"]),"vmin":0,"vmax":1000,"x":680}
						]
						for d in m_data:
							p = (d["v"] - d["vmin"]) / (d["vmax"] - d["vmin"])
							y = 108 + (1 - p) * 170
							x = d["x"]+664
							x1 = x-12
							x2 = x+12
							self.print_center(draw, str(int(round(d["v"]))), x, 330, self.font, bialy)
							#draw.line((x1, y, x2, y), fill = czerwony2, width = 10)
							# wyoblenia
						#	draw.ellipse((x1-5, y-4, x1+5, y+5), fill = czerwony2)
						#	draw.ellipse((x2-5, y-4, x2+5, y+5), fill = czerwony2)
							
											
						#tempomat
						if state['speedctrlactive']:
							# OPT 218, 442
							obrazek.paste(self.temp_aktyw, (259+664, 544))
							obrazek.paste(self.tacho_opt, (18+664, 71), self.tacho_opt)
							self.print_center(draw, '%d' % (war_speedctrlpower * 100), 54+664, 102, self.font2b, bialy)
							# V ASC 261, 246
							self.print_center(draw, '%d' % war_speedctrl, 310+664, 290, self.font2, bialy)
							self.print_center(draw, '%d' % war_speedctrl, 54+664, 400, self.font2b, bialy)		
							if state['universal5']:
								obrazek.paste(self.tempomat_klaw, (0+664, 447))								
						else:
							self.print_center(draw, "160", 310+664, 290, self.font2, bialy)		
							
							
					obrazek.paste(self.brak_kabiny, (0, 0))	
					draw.text((131, 5),"-100", font = self.maly_font2b, fill = bialy)
					draw.text((135, 38), "0", font = self.maly_font2b, fill = bialy)
					draw.text((203, 5), "0", font = self.maly_font2b, fill = bialy)
					draw.text((210, 38), "0", font = self.maly_font2b, fill = bialy)
					draw.text((297, 5), "0.00", font = self.maly_font2b, fill = bialy)
					draw.text((296, 38), "0.00", font = self.maly_font2b, fill = bialy)	
					draw.text((387, 5), "0", font = self.maly_font2b, fill = bialy)	
					
					
					if self.aktyw<60:
						obrazek.paste(self.bootowanie, (0, 0))	
											
					if self.aktyw>60 and state['cabactive'] == 1 and state['cab'] == 1 or state['cabactive'] == -1 and state['cab'] == -1 and state['universal7'] == 0:
						obrazek.paste(self.prawy, (0, 0))		
					#EKRAN BOCZNY
					# GÓRA
						draw.text((131, 5), str(int(round(state["eimp_t_pd"] * 100))), font = self.maly_font2b, fill = bialy)
						draw.text((135, 38), str(int(round(state["eimp_c1_fr"]))), font = self.maly_font2b, fill = bialy)
						if state["eimp_c1_ihv"] < 100:
							draw.text((203, 5), str(int(round(state["eimp_c1_ihv"] * 10)) / 10.0), font = self.maly_font2b, fill = bialy)
						else:
							draw.text((203, 5), str(int(round(state["eimp_c1_ihv"]))), font = self.maly_font2b, fill = bialy)
						draw.text((210, 38), str(int(round(state["voltage"]))), font = self.maly_font2b, fill = bialy)
						draw.text((297, 5), str(int(round(state["eimp_pn1_bp"] * 10)) / 10.0), font = self.maly_font2b, fill = bialy)
						draw.text((296, 38), str(int(round(state["eimp_pn1_sp"] * 10)) / 10.0), font = self.maly_font2b, fill = bialy)
						if state['speedctrlactive']:
							draw.text((387, 5), str(int(round(war_speedctrl))), font = self.maly_font2b, fill = bialy)	
							self.print_center(draw, str(int(round(war_speedctrl))), 227, 371, self.font2c, czarny)						
						else:
							draw.text((387, 5), "160", font = self.maly_font2b, fill = bialy)
							self.print_center(draw, "160", 227, 371, self.font2c, czarny)	

						self.print_center(draw, str(self.woda)+"%", 539,388, self.font2c, bialy)						
						self.print_center(draw, str(self.fekalia)+"%", 554,404, self.font2c, szare)						
					# POJAZD
						if (war_kier_P):
							obrazek.paste(self.kier_P, (15, 76), self.kier_P)
						if (war_kier_t):
							obrazek.paste(self.kier_t, (15, 76), self.kier_t)
						if (war_kier_0):
							obrazek.paste(self.kier_0, (15, 76), self.kier_0)							

						# gora
						if (war_cab == 1):
							if (war_panto_m_a):
								obrazek.paste(self.panto_m_a, (137, 95), self.panto_m_a)
							else:
								obrazek.paste(self.panto_dol, (137, 95), self.panto_dol)
							if (war_panto_m_d):
								obrazek.paste(self.panto_m_a, (397, 95), self.panto_m_a)
							else:
								obrazek.paste(self.panto_dol, (397, 95), self.panto_dol)								
						else: 
							if (war_panto_m_d):
								obrazek.paste(self.panto_m_a, (137, 95), self.panto_m_a)
							else:
								obrazek.paste(self.panto_dol, (137, 95), self.panto_dol)								
							if (war_panto_m_a):
								obrazek.paste(self.panto_m_a, (397, 95), self.panto_m_a)
							else:
								obrazek.paste(self.panto_dol, (397, 95), self.panto_dol)	
						

							

						
						if war_hamulec_1:
							obrazek.paste(self.hamulec_tarcza2, (50, 230), self.hamulec_tarcza2)	
						if war_hamulec_2:
							obrazek.paste(self.hamulec_tarcza2, (122, 230), self.hamulec_tarcza2)
							obrazek.paste(self.hamulec_tarcza2, (194, 230), self.hamulec_tarcza2)								
						if war_hamulec_3:
							obrazek.paste(self.hamulec_tarcza2, (241, 230), self.hamulec_tarcza2)	
						if war_hamulec_4:
							obrazek.paste(self.hamulec_tarcza2, (295, 230), self.hamulec_tarcza2)	
							obrazek.paste(self.hamulec_tarcza2, (341, 230), self.hamulec_tarcza2)
						if war_hamulec_5:
							obrazek.paste(self.hamulec_tarcza2, (414, 230), self.hamulec_tarcza2)
						if war_hamulec_6:
							obrazek.paste(self.hamulec_tarcza2, (482, 230), self.hamulec_tarcza2)		
						
						# ikonki
						if war_hamulec_sprezynowy:
							obrazek.paste(self.hamulec, (400, 358), self.hamulec)
						if state["brake_delay_flag"] == 2:
							obrazek.paste(self.hamulec_nastawa_p, (222, 389), self.hamulec_nastawa_p)
						
						if state["emergency_brake"] == 1:
							obrazek.paste(self.grzybek, (304, 360), self.grzybek)
						if war_poslizg_s:
							obrazek.paste(self.osie, (457, 356), self.osie)
						if war_piach:
							obrazek.paste(self.piasek, (195, 391), self.piasek)
						if state["pant_compressor"]:
							obrazek.paste(self.sprezarka_pomocnicza, (299, 387), self.sprezarka_pomocnicza)
						if state["compressors_1_work"]:
							obrazek.paste(self.ikonka_sprezarka, (254, 387), self.ikonka_sprezarka)
						if state["compressors_2_work"]:
							obrazek.paste(self.ikonka_sprezarka, (280, 387), self.ikonka_sprezarka)							
						if war_bat_m_a:
							obrazek.paste(self.ladowanie, (330, 388), self.ladowanie)
						if lights_front > 0 or lights_rear > 0:
							obrazek.paste(self.reflektory_przyc, (454, 388), self.reflektory_przyc)
						if state["lights_compartments"]:
							obrazek.paste(self.oswietlenie, (486, 390), self.oswietlenie)
							obrazek.paste(self.osw_przyc, (593, 56), self.osw_przyc)							
						if war_wylacznik_szybki:
							obrazek.paste(self.ikonka_ws, (224, 115), self.ikonka_ws)								
							
						if war_przetwornica_a and war_przetwornica_d:
							obrazek.paste(self.ikonka_przetwornica, (43, 352), self.ikonka_przetwornica)
						
						if state["converter"] == 0:
							obrazek.paste(self.ikonka_przetwornica_pom, (6, 352), self.ikonka_przetwornica_pom)

						# reflektory
						if (war_cab == 1):
							obrazek.paste(self.ludzik_akt, (38, 165), self.ludzik_akt)
						else:
							obrazek.paste(self.ludzik_akt, (523, 165), self.ludzik_akt)
						
						# czolo 1
						if (lights_front & 1): # lewe
							draw.ellipse((63, 318, 67, 322), fill = bialy)
						if (lights_front & 2): # lewe czerwone
							draw.ellipse((56, 320, 60, 324), fill = czerwony2)
						if (lights_front & 4): # gorne
							draw.ellipse((38, 277, 42, 281), fill = bialy)
						if (lights_front & 16): # prawe
							draw.ellipse((13, 318, 17, 322), fill = bialy)							
						if (lights_front & 32): # prawe czerwone
							draw.ellipse((20, 319, 24, 323), fill = czerwony2)							
						
						# czolo 2
						if (lights_rear & 1): # lewe
							draw.ellipse((562, 318, 566, 322), fill = bialy)
						if (lights_rear & 2): # lewe czerwone
							draw.ellipse((555, 320, 559, 324), fill = czerwony2)
						if (lights_rear & 4): # gorne
							draw.ellipse((537, 277, 541, 281), fill = bialy)
						if (lights_rear & 16): # prawe
							draw.ellipse((512, 318, 516, 322), fill = bialy)
						if (lights_rear & 32): # prawe czerwone
							draw.ellipse((519, 319, 523, 323), fill = czerwony2)
						
			#RYSOWANIE DRZWI
						d = [False] * 24
						s = [False] * 24
						# 0 1 2 3 4 5 6 7 8 9 10 11 
						#<=|=|=>
						# 12 13 14 15 16 17 18 19 20 21 22 23 

						if state ['door_permit_right'] == 1:
							obrazek.paste(self.drzwi_zgoda, (77, 150), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (117, 150), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (150, 150), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (190, 150), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (222, 150), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (263, 150), self.drzwi_zgoda)							
							obrazek.paste(self.drzwi_zgoda, (295, 150), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (336, 150), self.drzwi_zgoda)							
							obrazek.paste(self.drzwi_zgoda, (368, 150), self.drzwi_zgoda)				
							obrazek.paste(self.drzwi_zgoda, (408, 150), self.drzwi_zgoda)							
							obrazek.paste(self.drzwi_zgoda, (441, 150), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (482, 150), self.drzwi_zgoda)

	
						

						if state ['door_permit_left'] == 1:
							obrazek.paste(self.drzwi_zgoda, (77, 200), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (117, 200), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (150, 200), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (190, 200), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (222, 200), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (263, 200), self.drzwi_zgoda)							
							obrazek.paste(self.drzwi_zgoda, (295, 200), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (336, 200), self.drzwi_zgoda)							
							obrazek.paste(self.drzwi_zgoda, (368, 200), self.drzwi_zgoda)				
							obrazek.paste(self.drzwi_zgoda, (408, 200), self.drzwi_zgoda)							
							obrazek.paste(self.drzwi_zgoda, (441, 200), self.drzwi_zgoda)
							obrazek.paste(self.drzwi_zgoda, (482, 200), self.drzwi_zgoda)

						d[0] = war_c1_d1P
						d[1] = war_c1_d3P
						d[2] = war_c2_d5P
						d[3] = war_c2_d7P
						d[4] = war_c3_d9P
						d[5] = war_c3_d11P
						d[6] = war_c4_d13P
						d[7] = war_c4_d15P
						d[8] = war_c5_d17P
						d[9] = war_c5_d19P
						d[10] = war_c6_d21P
						d[11] = war_c6_d23P				
						d[12] = war_c1_d2L
						d[13] = war_c1_d4L
						d[14] = war_c2_d6L
						d[15] = war_c2_d8L
						d[16] = war_c3_d10L
						d[17] = war_c3_d12L
						d[18] = war_c4_d14L
						d[19] = war_c4_d16L
						d[20] = war_c5_d18L
						d[21] = war_c5_d20L
						d[22] = war_c6_d22L
						d[23] = war_c6_d24L
						


						s[0] = war_c1_ds1P
						s[1] = war_c1_ds3P
						s[2] = war_c2_ds5P
						s[3] = war_c2_ds7P
						s[4] = war_c3_ds9P
						s[5] = war_c3_ds11P
						s[6] = war_c4_ds13P
						s[7] = war_c4_ds15P
						s[8] = war_c5_ds17P
						s[9] = war_c5_ds19P
						s[10] = war_c6_ds21P
						s[11] = war_c6_ds23P				
						s[12] = war_c1_ds2L
						s[13] = war_c1_ds4L
						s[14] = war_c2_ds6L
						s[15] = war_c2_ds8L
						s[16] = war_c3_ds10L
						s[17] = war_c3_ds12L
						s[18] = war_c4_ds14L
						s[19] = war_c4_ds16L
						s[20] = war_c5_ds18L
						s[21] = war_c5_ds20L
						s[22] = war_c6_ds22L
						s[23] = war_c6_ds24L
							

						
						if d[0]:
							obrazek.paste(self.drzwi_gora, (77, 150), self.drzwi_gora)
							obrazek.paste(self.drzwi_gora, (117, 150), self.drzwi_gora)
						if d[1]:
							obrazek.paste(self.drzwi_gora, (150, 150), self.drzwi_gora)
							obrazek.paste(self.drzwi_gora, (190, 150), self.drzwi_gora)
						if d[2]:
							obrazek.paste(self.drzwi_gora, (222, 150), self.drzwi_gora)
							obrazek.paste(self.drzwi_gora, (263, 150), self.drzwi_gora)							
						if d[3]:
							obrazek.paste(self.drzwi_gora, (295, 150), self.drzwi_gora)
							obrazek.paste(self.drzwi_gora, (336, 150), self.drzwi_gora)							
						if d[4]:
							obrazek.paste(self.drzwi_gora, (368, 150), self.drzwi_gora)				
							obrazek.paste(self.drzwi_gora, (408, 150), self.drzwi_gora)							
						if d[5]:
							obrazek.paste(self.drzwi_gora, (441, 150), self.drzwi_gora)
							obrazek.paste(self.drzwi_gora, (482, 150), self.drzwi_gora)							
						#if d[6]:

						#if d[7]:

					#	if d[8]:

						#if d[9]:

						#if d[10]:

						#if d[11]:

			
						
						if d[12]:
							obrazek.paste(self.drzwi_dol, (77, 200), self.drzwi_dol)
							obrazek.paste(self.drzwi_dol, (117, 200), self.drzwi_dol)							
						if d[13]:
							obrazek.paste(self.drzwi_dol, (150, 200), self.drzwi_dol)
							obrazek.paste(self.drzwi_dol, (190, 200), self.drzwi_dol)							
						if d[14]:
							obrazek.paste(self.drzwi_dol, (222, 200), self.drzwi_dol)
							obrazek.paste(self.drzwi_dol, (263, 200), self.drzwi_dol)
						if d[15]:
							obrazek.paste(self.drzwi_dol, (295, 200), self.drzwi_dol)
							obrazek.paste(self.drzwi_dol, (336, 200), self.drzwi_dol)							
						if d[16]:
							obrazek.paste(self.drzwi_dol, (368, 200), self.drzwi_dol)
							obrazek.paste(self.drzwi_dol, (408, 200), self.drzwi_dol)							
						if d[17]:
							obrazek.paste(self.drzwi_dol, (441, 200), self.drzwi_dol)
							obrazek.paste(self.drzwi_dol, (482, 200), self.drzwi_dol)							
					#	if d[18]:

					#	if d[19]:

						#if d[20]:

					#	if d[21]:

						#if d[22]:

						#if d[23]:
							

						if s[0]:
							obrazek.paste(self.stopien_gora, (77, 140), self.stopien_gora)
							obrazek.paste(self.stopien_gora, (117, 140), self.stopien_gora)							
						if s[1]:
							obrazek.paste(self.stopien_gora, (150, 140), self.stopien_gora)
							obrazek.paste(self.stopien_gora, (190, 140), self.stopien_gora)							
						if s[2]:
							obrazek.paste(self.stopien_gora, (222, 140), self.stopien_gora)
							obrazek.paste(self.stopien_gora, (263, 140), self.stopien_gora)							
						if s[3]:
							obrazek.paste(self.stopien_gora, (295, 140), self.stopien_gora)
							obrazek.paste(self.stopien_gora, (336, 140), self.stopien_gora)							
						if s[4]:
							obrazek.paste(self.stopien_gora, (368, 140), self.stopien_gora)
							obrazek.paste(self.stopien_gora, (408, 140), self.stopien_gora)							
						if s[5]:
							obrazek.paste(self.stopien_gora, (441, 140), self.stopien_gora)
							obrazek.paste(self.stopien_gora, (482, 140), self.stopien_gora)							
						#if s[6]:

					#	if s[7]:

					#	if s[8]:
#
					#	if s[9]:

					#	if s[10]:

						#if s[11]:

			
						
						if s[12]:
							obrazek.paste(self.stopien_dol, (77, 210), self.stopien_dol)
							obrazek.paste(self.stopien_dol, (117, 210), self.stopien_dol)							
						if s[13]:
							obrazek.paste(self.stopien_dol, (150, 210), self.stopien_dol)
							obrazek.paste(self.stopien_dol, (190, 210), self.stopien_dol)							
						if s[14]:
							obrazek.paste(self.stopien_dol, (222, 210), self.stopien_dol)
							obrazek.paste(self.stopien_dol, (263, 210), self.stopien_dol)							
						if s[15]:
							obrazek.paste(self.stopien_dol, (295, 210), self.stopien_dol)
							obrazek.paste(self.stopien_dol, (336, 210), self.stopien_dol)							
						if s[16]:
							obrazek.paste(self.stopien_dol, (368, 210), self.stopien_dol)
							obrazek.paste(self.stopien_dol, (408, 210), self.stopien_dol)							
						if s[17]:
							obrazek.paste(self.stopien_dol, (441, 210), self.stopien_dol)
							obrazek.paste(self.stopien_dol, (482, 210), self.stopien_dol)								
						#if s[18]:

						#if s[19]:

						#if s[20]:

						#if s[21]:

						#if s[22]:

						#if s[23]:

				###========= SEKCJA KOMUNIKATOW - WYSWIETLANIE ============

						messages0 = [
							# Alarmy
							{"name":u"B              651           Błąd uchwytu rączki awaryjnego otwierania przednich prawych drzwi - człon A (drzwi 2)","cond":awaria1},		
							{"name":u"B              731           Błąd uchwytu rączki awaryjnego otwierania przednich prawych drzwi - człon C (drzwi 2)","cond":awaria2},		
							{"name":u"B              871           Błąd uchwytu rączki awaryjnego otwierania przednich prawych drzwi - człon E (drzwi 1)","cond":awaria3},
							{"name":u"B              651           Błąd uchwytu rączki awaryjnego otwierania przednich lewych drzwi - człon A (drzwi 1)","cond":awaria4},		
							{"name":u"B              691           Błąd uchwytu rączki awaryjnego otwierania tylnych prawych drzwi - człon A (drzwi 4)","cond":awaria5},
							{"name":u"B              871           Błąd uchwytu rączki awaryjnego otwierania przednich lewych drzwi - człon E (drzwi 1)","cond":awaria6},	
							{"name":u"B              931           Błąd uchwytu rączki awaryjnego otwierania tylnych prawych drzwi - człon E (drzwi 1)","cond":awaria7},							
							{"name":u"B              831           Błąd uchwytu rączki awaryjnego otwierania tylnych lewych drzwi - człon D (drzwi 3)","cond":awaria8},	
							{"name":u"C              713           Błąd silnika/pozycji enkodera stopnia przednich lewych drzwi - człon B (drzwi 1)","cond":awaria9},	
							{"name":u"A              21             Niewyluzowany hamulec postojowy wózka członu A1","cond":awaria10},																	
							{"name":u"A              21             Niewyluzowany hamulec postojowy wózka członu A2","cond":awaria11},		
							{"name":u"A              106           Niewyluzowany hamulec postojowy wózka - człon D","cond":awaria12},	
							{"name":u"D              1493          Uszkodzony czujnik pożaru 1 (przestrzeń pasażerska) - człon D","cond":awaria13},				
							{"name":u"B              237           Wysoka temperatura radiatora - falownik 1","cond":awaria14},	
							{"name":u"B              193           Błąd pomiaru temperatury dławika - falownik 1","cond":awaria15},	
							{"name":u"B              247           Błąd pomiaru temperatury dławika - falownik 2","cond":awaria16},									
							{"name":u"C              150           Odizolowany silnik 1","cond":war_odl_s_1_a},	
							{"name":u"C              151           Odizolowany silnik 2","cond":war_odl_s_2_a},	
							{"name":u"C              152           Odizolowany silnik 3","cond":war_odl_s_3_c},	
							{"name":u"C              153           Odizolowany silnik 4","cond":war_odl_s_4_c},	
							{"name":u"C              154           Odizolowany silnik 5","cond":war_odl_s_5_f},	
							{"name":u"C              155           Odizolowany silnik 6","cond":war_odl_s_6_f},	
							{"name":u"B              1050          Falownik niegotowy do pracy - falownik TCU 1","cond":war_odl_a_1_a},		
							{"name":u"B              1051          Falownik niegotowy do pracy - falownik TCU 2","cond":war_odl_a_2_a},		
							{"name":u"B              1052          Falownik niegotowy do pracy - falownik TCU 3","cond":war_odl_a_3_c},
							{"name":u"B              1053          Falownik niegotowy do pracy - falownik TCU 4","cond":war_odl_a_4_c},	
							{"name":u"B              1054          Falownik niegotowy do pracy - falownik TCU 5","cond":war_odl_a_5_f},		
							{"name":u"B              1055          Falownik niegotowy do pracy - falownik TCU 6","cond":war_odl_a_6_f},			
							{"name":u"B              58             Jazda awaryjna pojazdu aktywna","cond":((state['door_lock']) == 0)},										
							# Informacja

							# Inne, na podstawie obserwacji

						]

						messages = messages0

						global activeMessages

						for i in range(len(messages)):
							message = messages[i]
							messageActive = message["cond"] # czy powinno byc
							messageActived = i in activeMessages # czy jest
							if messageActive and (not messageActived): # dodawanie do listy
								activeMessages.insert(0, i) # dajemy na poczatek listy, poniewaz najnowsze komunikaty pojawiaja sie na gorze
							if (not messageActive) and messageActived: # usuwanie z listy
								activeMessages.remove(i)

							 # i to tyle jesli chodzi o logike, teraz rysowanie
							
							
						if len(activeMessages) != 0:
							obrazek.paste(self.komunikaty, (593, 248), self.komunikaty)
						if state['universal6']:
							obrazek.paste(self.lista, (0, 0))		
							i = 0
							for messageId in activeMessages:
								if messageId >= len(messages):
									continue
								message = messages[messageId]
								color = bialy
								if i == 0:
									color = czarny
								else: 
									color = bialy
								draw.text((34, 105 + (i * 24)), message["name"], font = self.arialbold9, fill = color)																
								if i == 12: # po 12 konczymy, wiecej sie nie zmiesci
									break
								i += 1			
							draw.text((131, 5), str(int(round(state["eimp_t_pd"] * 100))), font = self.maly_font2b, fill = bialy)
							draw.text((135, 38), str(int(round(state["eimp_c1_fr"]))), font = self.maly_font2b, fill = bialy)
							if state["eimp_c1_ihv"] < 100:
								draw.text((203, 5), str(int(round(state["eimp_c1_ihv"] * 10)) / 10.0), font = self.maly_font2b, fill = bialy)
							else:
								draw.text((203, 5), str(int(round(state["eimp_c1_ihv"]))), font = self.maly_font2b, fill = bialy)
							draw.text((210, 38), str(int(round(state["voltage"]))), font = self.maly_font2b, fill = bialy)
							draw.text((297, 5), str(int(round(state["eimp_pn1_bp"] * 10)) / 10.0), font = self.maly_font2b, fill = bialy)
							draw.text((296, 38), str(int(round(state["eimp_pn1_sp"] * 10)) / 10.0), font = self.maly_font2b, fill = bialy)
							if state['speedctrlactive']:
								draw.text((387, 5), str(int(round(war_speedctrl))), font = self.maly_font2b, fill = bialy)					
							else:
								draw.text((387, 5), "160", font = self.maly_font2b, fill = bialy)	



		else:
			# szansa na zbicie zepsucia jesli wlasnie wylaczono baterie
			if self.awaria and self.aktyw > 0 and random() < 0.4:
				self.awaria = False
			
			self.aktyw = 0
			self.tryb = 0
			state['universal6'] == 0
		return obrazek

		

# globale do komunikatow
activeMessages = []