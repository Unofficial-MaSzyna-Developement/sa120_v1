#encoding: UTF-8

from PIL import ImageDraw, ImageFont, Image
from random import random
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
pomarancz = (195,63,42)
niebieski = (51,198,247)
niebieski_pixy = (62,129,179)
monitoring1 = (81,82,73)
monitoring2 = (98,188,77)
monitoring3 = (255,0,0)
monitoring4 = (204,204,204)
bladcan = (0,128,255)
szary = (128,128,128)

class skm_renderer(abstractscreenrenderer):
	def __init__(self, lookup_path):
		# wczytanie obrazka
		self.moj_obrazek = self.openimage(lookup_path + "ekran/ekran")
		# wczytanie czcionki
		czcionka = "arial.ttf"
		self.font = ImageFont.truetype('./fonts/' + czcionka, 22)		
		self.maly_font = ImageFont.truetype('./fonts/' + czcionka, 17)	
		self.bardzo_maly_font = ImageFont.truetype('./fonts/' + czcionka, 11)	
		self.polduzy_font = ImageFont.truetype('./fonts/' + czcionka, 30)
		self.duzy_font = ImageFont.truetype('./fonts/' + czcionka, 60)
		self.srg_arial = ImageFont.truetype('./fonts/arialbd.ttf', 36)
		self.srg_arial2 = ImageFont.truetype('./fonts/arialbd.ttf', 27)
		self.srg_arial3 = ImageFont.truetype('./fonts/arialbd.ttf', 24)
		self.arialbold16 = ImageFont.truetype('./fonts/arialbd.ttf', 16)
		self.arialbold14 = ImageFont.truetype('./fonts/arialbd.ttf', 14)
		self.konsola = ImageFont.truetype('./fonts/unifont.ttf', 14)

		self.last_time_update = 0
		self.dzis = datetime.now().timetuple().tm_yday
		self.rok = datetime.now().year
		self.last_hour = 10
		self.temp = (random()*30) + 20

		self.prawy = Image.open(lookup_path +"ekran/prawy3.png")
		self.tacho = Image.open(lookup_path +"ekran/tacho.png")
		self.monitoring = Image.open(lookup_path +"ekran/monitoring.png")


		self.ws_d = Image.open(lookup_path +"ekran/ws_d.png")
		self.lewe_drzwi_a = Image.open(lookup_path +"ekran/lewe_drzwi_d.png")
		self.pozar = Image.open(lookup_path +"ekran/pozar.png")
		self.uziom = Image.open(lookup_path +"ekran/uziom.png")
		self.prawe_drzwi_a = Image.open(lookup_path +"ekran/prawe_drzwi_d.png")
		self.a = Image.open(lookup_path +"ekran/a.png")
		self.osw = Image.open(lookup_path +"ekran/osw.png")
		self.p = Image.open(lookup_path +"ekran/p.png")
		self.r = Image.open(lookup_path +"ekran/r.png")
		self.pantografowa = Image.open(lookup_path +"ekran/sprezarka_pomocnicza.png")
		self.inw = Image.open(lookup_path +"ekran/inw.png")
		self.piorun = Image.open(lookup_path +"ekran/piorun.png")
		self.piach = Image.open(lookup_path +"ekran/piach.png")
		self.poslizg_s = Image.open(lookup_path +"ekran/poslizg_s.png")
		self.u400v = Image.open(lookup_path +"ekran/400v.png")
		self.sos = Image.open(lookup_path +"ekran/sos.png")
		self.kier_P = Image.open(lookup_path +"ekran/kier_p.png")
		self.kier_t = Image.open(lookup_path +"ekran/kier_t.png")
		self.panto_m_a = Image.open(lookup_path +"ekran/panto_m.png")
		self.uziom_m_a = Image.open(lookup_path +"ekran/uziom_m.png")
		self.ws_m_a = Image.open(lookup_path +"ekran/ws_m.png")
		self.kompresor_a = Image.open(lookup_path +"ekran/kompresor.png")
		self.u400v_m_a = Image.open(lookup_path +"ekran/400v_m.png")
		self.bat_m_a = Image.open(lookup_path +"ekran/bat_m.png")
		self.przetwornica = Image.open(lookup_path +"ekran/przetwornica.png")
		self.odl_s_1_a = Image.open(lookup_path +"ekran/odl_s_1.png")
		self.odl_s_2_a = Image.open(lookup_path +"ekran/odl_s_2.png")
		self.ham_pos_a = Image.open(lookup_path +"ekran/ham_pos.png")
		self.cisnienie_a = Image.open(lookup_path +"ekran/cisnienie.png")
		self.inw_m_a = Image.open(lookup_path +"ekran/inw_m.png")
		self.a_m_a = Image.open(lookup_path +"ekran/a_m.png")
		self.sos_m_a = Image.open(lookup_path +"ekran/sos_m.png")
		self.awaria_a = Image.open(lookup_path +"ekran/awaria.png")
		self.ukrotnienie = Image.open(lookup_path +"ekran/ukrotnienie.png")
		self.ukrotnienie_master = Image.open(lookup_path +"ekran/ukrotnienie_master.png")
		self.ukrotnienie_slave = Image.open(lookup_path +"ekran/ukrotnienie_slave.png")	
		self.oswietlenie_czola = Image.open(lookup_path +"ekran/oswietlenie.png")	
		self.brak_can = Image.open(lookup_path +"ekran/brak_can.png")
		self.bootowanie = Image.open(lookup_path +"ekran/bootowanie.png")		
		self.brak_ladowania = Image.open(lookup_path +"ekran/brak_ladowania.png")		
		self.podwojne = Image.open(lookup_path +"ekran/podwojne.png")
		self.blokada = Image.open(lookup_path +"ekran/blokadadrzwi.png")		
		self.brak_konfigu = Image.open(lookup_path +"ekran/brak_konfigu.png")
		self.jest_konfigu = Image.open(lookup_path +"ekran/jest_konfig.png")
		self.przelaczanie = Image.open(lookup_path +"ekran/przelaczanie.png")	
		self.zaduzo = Image.open(lookup_path +"ekran/zaduzo.png")			
		self.aktyw = 0
		
		self.lookup_path = lookup_path
		self.kilometry = (random()*1000)+(self.rok-2017)*140000+self.dzis*450
		self.kilometry_z = 0
		self.read_tacho = False
		
		self.awaria = False
		
		self.tryb = 0
		self.stan1 = False
		self.stan2 = False
		self.stan4 = False
		self.stan5 = False
		self.stan6 = False
		self.klikniete = -1		

	def _render(self, state):
		self.klikniete = -1		
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
				data = data.strftime("%d/%m/%Y")


				# symulacja zepsucia ekranu
				# 0.0000002 szansy co odswiezenie daje nam znikoma szanse na kazdej sluzbie, ale to moze sie stac
				# kazde zresetowanie daje nam 40% szansy na "zbicie zepsucia"
				if self.awaria:
					draw.rectangle((136,219,485,261), fill=bladcan)
					self.print_center(draw, u"Oczekiwanie na komunikacje..." , 320,240, self.arialbold14, monitoring4)
					self.aktyw = 1 # gdy reset sie nie udal, musimy recznie przestawic aktywacje by byla znowu szansa na zbicie awarii
					return obrazek # koniec
				
				# losuj zepsucie
				self.awaria = self.aktyw >= 60 and random() < 0.0000005
				
				# Liczenie pojazdow
				pojazdy = 1
				unit_no = state['unit_no']
				car_no = state['car_no']
				if (unit_no == 2) and (car_no == 12):
					pojazdy = 2
				if (unit_no == 2) and (car_no == 18):
					pojazdy = 3
				if (unit_no == 2) and (car_no == 24):
					pojazdy = 4			
				if (unit_no >= 3):
					pojazdy = 5	
					

				mr1 = float(state['eimp_c1_fr'])
				mr2 = float(state['eimp_c2_fr'])
				mr3 = float(state['eimp_c3_fr'])				
				mr4 = float(state['eimp_c4_fr'])
				mr5 = float(state['eimp_c5_fr'])				
				mr6 = float(state['eimp_c6_fr'])
				mz = float(state['eimp_t_pd'])

				if state["mainctrl_pos"] == 0:	
					mz = -1

				#draw.text((272,6), czas, fill=bialy, font=self.font)

				war_cab = state['cab']
				lights_front = state['lights_train_front']
				lights_rear = state['lights_train_rear']
				if self.aktyw<60:
					war_tacho = False
				else:
					war_tacho = True
					
				war_monitoring = True
				war_pozar = False
				war_uziom = False
				war_a = False
				war_a2 = False
				war_pozar2 = False
				war_uziom2 = False
				war_a = False
				if (state['lights_compartments'] == 1):
					war_osw = True
				else:
					war_osw = False
				war_p = state["brake_delay_flag"] == 2
				war_r = state["brake_delay_flag"] == 4
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
				if (war_cab == 1):
					war_panto_m_a = state['eimp_u1_pf']
					war_panto_m_a2 = state['eimp_u2_pf']
				else:
					war_panto_m_a = state['eimp_u1_pr']
					war_panto_m_a2 = state['eimp_u2_pr']
				war_uziom_m_a = False
				war_uziom_m_a2 = False
				war_ws_m_a = state['eimp_c1_ms']
				war_ws_m_a2 = state['eimp_c3_ms']
				war_kompresor_a = state['eimp_u1_comp_w']
				war_kompresor_a2 = state['eimp_u2_comp_w']
				war_400v_m_a = False
				war_400v_m_a2 = False
				war_bat_m_a = (state['eimp_c1_batt'] == 1) & (state['eimp_c1_conv'] == 0)
				war_bat_m_a2 = (state['eimp_c3_batt'] == 1) & (state['eimp_c3_conv'] == 0)
				war_przetwornica_a = (state['eimp_c1_inv1_act'] == 0) & (state['eimp_c1_inv2_act'] == 0)
				war_odl_s_1_a = state['eimp_c1_inv1_act'] == 0
				war_odl_s_2_a = state['eimp_c1_inv2_act'] == 0
				
				if (pojazdy > 1):
					war_odl_s_1_a2 = state['eimp_c3_inv1_act'] == 0
					war_odl_s_2_a2 =  state['eimp_c3_inv2_act'] == 0
					war_przetwornica_a2 = (state['eimp_c3_inv1_act'] == 0) & (state['eimp_c3_inv2_act'] == 0)
				war_ham_pos_a = state['brakes_1_spring_active']
				war_ham_pos_b = state['brakes_2_spring_active']
				war_ham_pos_c = state['brakes_3_spring_active']
				war_ham_pos_d = state['brakes_4_spring_active']
				war_ham_pos_e = state['brakes_5_spring_active']
				war_ham_pos_f = state['brakes_6_spring_active']
				war_ham_pos_c2 = state['brakes_7_spring_active']
				war_ham_pos_d2 = state['brakes_8_spring_active']
				war_cisnienie_a = state['eimp_pn1_bc'] > 0.1
				war_inw_m_a = False
				war_a_m_a = False
				war_sos_m_a = False
				war_awaria_a = False
				war_inw_m_a2 = False
				war_a_m_a2 = False
				war_sos_m_a2 = False
				war_awaria_a2= False
				war_ladowanie = state['converter'] == 0
				
				war_cisnienie_b = state['eimp_pn2_bc'] > 0.1
				war_cisnienie_c = state['eimp_pn3_bc'] > 0.1
				war_cisnienie_d = state['eimp_pn4_bc'] > 0.1
				war_cisnienie_e = state['eimp_pn5_bc'] > 0.1
				war_cisnienie_f = state['eimp_pn6_bc'] > 0.1
				
				if (war_cab == 1):
					war_panto_m_d = state['eimp_u1_pr']
					war_panto_m_d2 = state['eimp_u2_pr']
				else:
					war_panto_m_d = state['eimp_u1_pf']
					war_panto_m_d2 = state['eimp_u2_pf']
				war_uziom_m_d = False
				war_uziom_m_d2 = False
				war_ws_m_d = state['eimp_c4_ms']
				war_ws_m_d2 = state['eimp_c4_ms']
				war_kompresor_d = state['eimp_u1_comp_w']
				war_kompresor_d2 = state['eimp_u2_comp_w']
				war_400v_m_d = False
				war_400v_m_d2 = False
				war_bat_m_d = (state['eimp_c4_batt'] == 1) & (state['eimp_c4_conv'] == 0)
				war_bat_m_d2 = (state['eimp_c4_batt'] == 1) & (state['eimp_c4_conv'] == 0)
				war_przetwornica_d = (state['eimp_c4_inv1_act'] == 0) & (state['eimp_c4_inv2_act'] == 0)
				war_odl_s_1_d = state['eimp_c4_inv1_act'] == 0
				war_odl_s_2_d = state['eimp_c4_inv2_act'] == 0
				war_odl_s_1_d2 = state['eimp_c4_inv1_act'] == 0
				war_odl_s_2_d2 = state['eimp_c4_inv2_act'] == 0
				war_przetwornica_d2 = (state['eimp_c4_inv1_act'] == 0) & (state['eimp_c4_inv2_act'] == 0)
				war_inw_m_d = False
				war_a_m_d = False
				war_sos_m_d = False
				war_awaria_d = False
				war_inw_m_d2 = False
				war_a_m_d2 = False
				war_sos_m_d2 = False
				war_awaria_b2 = False
				war_awaria_c = False								
				war_awaria_d2 = False

				war_400v = war_400v_m_a | war_400v_m_d
				war_ws_d = war_ws_m_a | war_ws_m_d
				
				war_400v2 = war_400v_m_a2 | war_400v_m_d2
				war_ws_d2 = war_ws_m_a2 | war_ws_m_d2

				war_c1_d1P = state['doors_r_1']
				war_c1_d1L = state['doors_l_1']
				
				war_c2_d2P = state['doors_r_2']
				war_c2_d2L = state['doors_l_2']
				
				war_c3_d3P = state['doors_r_3']
				war_c3_d3L = state['doors_l_3']
				
				war_c4_d4P = state['doors_r_4']
				war_c4_d4L = state['doors_l_4']

				war_c1_ds1P = state['doorstep_r_1']
				war_c1_ds1L = state['doorstep_l_1']
				
				war_c2_ds2P = state['doorstep_r_2']
				war_c2_ds2L = state['doorstep_l_2']
				
				war_c3_ds3P = state['doorstep_r_3']
				war_c3_ds3L = state['doorstep_l_3']
				
				war_c4_ds4P = state['doorstep_r_4']
				war_c4_ds4L = state['doorstep_l_4']
				
				war_c5_d5P = state['doors_r_5']
				war_c5_d5L = state['doors_l_5']
				
				war_c6_d6P = state['doors_r_6']
				war_c6_d6L = state['doors_l_6']
				
				war_c7_d7P = state['doors_r_7']
				war_c7_d7L = state['doors_l_7']
				
				war_c8_d8P = state['doors_r_8']
				war_c8_d8L = state['doors_l_8']

				war_c5_ds5P = state['doorstep_r_5']
				war_c5_ds5L = state['doorstep_l_5']
				
				war_c6_ds6P = state['doorstep_r_6']
				war_c6_ds6L = state['doorstep_l_6']
				
				war_c7_ds7P = state['doorstep_r_7']
				war_c7_ds7L = state['doorstep_l_7']
				
				war_c8_ds8P = state['doorstep_r_8']
				war_c8_ds8L = state['doorstep_l_8']

				war_lewe_drzwi_a = war_c1_d1L | war_c1_d1L
				war_prawe_drzwi_a = war_c1_d1P | war_c1_d1P
				
				war_lewe_drzwi_b = war_c2_d2L | war_c2_d2L
				war_prawe_drzwi_b = war_c2_d2P | war_c2_d2P
				
				war_lewe_drzwi_c = war_c3_d3L | war_c3_d3L
				war_prawe_drzwi_c = war_c3_d3P | war_c3_d3P
				
				
				war_lewe_drzwi_d = war_c4_d4L | war_c4_d4L
				war_prawe_drzwi_d = war_c4_d4P | war_c4_d4P
				
				war_lewe_drzwi_e = war_c5_d5L | war_c5_d5L
				war_prawe_drzwi_e = war_c5_d5P | war_c5_d5P
				
				war_lewe_drzwi_f = war_c6_d6L | war_c6_d6L
				war_prawe_drzwi_f = war_c6_d6P | war_c6_d6P
				
				war_lewe_drzwi_c2 = war_c7_d7L | war_c7_d7L
				war_prawe_drzwi_c2 = war_c7_d7P | war_c7_d7P
				
				war_lewe_drzwi_d2 = war_c8_d8L | war_c8_d8L
				war_prawe_drzwi_d2 = war_c8_d8P | war_c8_d8P
				
				mainctrl_pos = state['mainctrl_pos']
				war_awaria_a = ((war_lewe_drzwi_a | war_prawe_drzwi_a) | (state['eimp_pn1_bp'] < 4.9) ) & ((mainctrl_pos != 2 )&(mainctrl_pos != 3 ))
				war_awaria_b= ((war_lewe_drzwi_b | war_prawe_drzwi_b) | (state['eimp_pn2_bp'] < 4.9) ) & ((mainctrl_pos != 2 )&(mainctrl_pos != 3 ))
				war_awaria_c = ((war_lewe_drzwi_c | war_prawe_drzwi_c) | (state['eimp_pn3_bp'] < 4.9) ) & ((mainctrl_pos != 2 )&(mainctrl_pos != 3 ))				
				war_awaria_d = ((war_lewe_drzwi_d | war_prawe_drzwi_d) | (state['eimp_pn4_bp'] < 4.9) ) & ((mainctrl_pos != 2 )&(mainctrl_pos != 3 ))
				war_awaria_e = ((war_lewe_drzwi_e | war_prawe_drzwi_e) | (state['eimp_pn5_bp'] < 4.9) ) & ((mainctrl_pos != 2 )&(mainctrl_pos != 3 ))
				war_awaria_f = ((war_lewe_drzwi_f | war_prawe_drzwi_f) | (state['eimp_pn6_bp'] < 4.9) ) & ((mainctrl_pos != 2 )&(mainctrl_pos != 3 ))

				
				war_speedctrl = state['speedctrl']
				war_speedctrlpower = state['speedctrlpower']
				
				war_pomocnicza = (state['pant_compressor'] == 1)

			#TŁA
			
				if (war_monitoring):
					draw.rectangle((1469,564,2044,1022), fill=czarny)
					if self.aktyw >= 0:
						self.print_center(draw, "Uruchamianie rejestratora" , 1757,620, self.arialbold14, monitoring1)
						self.print_center(draw, data, 1707,640, self.arialbold14, monitoring2)
						self.print_center(draw, czas, 1797,640, self.arialbold14, monitoring2)
						self.print_center(draw, u"Nawiązywanie połączenia" , 1757,660, self.arialbold14, monitoring3)	
					if self.aktyw >= 60:
						obrazek.paste(self.monitoring, (1469, 564))
					
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
						
				if state['universal1'] != self.stan1:
					self.klikniete = 1
				if state['universal2'] != self.stan2:
					self.klikniete = 2
				if state['universal4'] != self.stan4:
					self.klikniete = 4
				if state['universal5'] != self.stan5:
					self.klikniete = 5				
					
				if (self.tryb == 0) and (self.klikniete == 1) and (pojazdy < 3): #konfig pociagu
					self.tryb = 1
				elif (self.tryb == 1) and (self.klikniete == 1): #zrzut konfigu
					self.tryb = 0 	
				elif (self.tryb == 1) and (self.klikniete == 2) and (pojazdy < 3): #widok wozu
					self.tryb = 2 	
				elif (self.tryb == 2) and (pojazdy == 1) and (self.klikniete == 4): #widok na drugi woz
					self.tryb = 3
				elif (self.tryb == 3) and (pojazdy == 1) and (self.klikniete == 4): #z drugiego na 1 woz
					self.tryb = 2		
				elif (self.tryb == 3) and (self.klikniete == 5): #z wozu do konfigu
					self.tryb = 1 							
				elif (self.tryb == 2) and (self.klikniete == 5): #z wozu do konfigu
					self.tryb = 1 						
			#TACHOMETR
				if (war_tacho == True):
					obrazek.paste(self.tacho, (664, 0))
					rotate = speed * 360 / 260 + 55.4
					rad = radians(rotate)
					srodek_tacho = (267+664, 314)
					point = (-2,215)
					rotated_point = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (2,215)
					rotated_point2 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (4,10)
					rotated_base_one = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (-4,10)
					rotated_base_two = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					# rysujemy 
					draw.polygon([rotated_base_one,rotated_base_two,rotated_point,rotated_point2],fill=pomarancz)
					dtach = 28
					draw.pieslice((srodek_tacho[0]-dtach,srodek_tacho[1]-dtach,srodek_tacho[0]+dtach,srodek_tacho[1]+dtach), 0, 360, fill=pomarancz)

					# duzy tekst z predkoscia w srodku = READY
					msg = '%d' % speed
					self.print_center(draw, msg, srodek_tacho[0],srodek_tacho[1], self.polduzy_font, bialy)
					#zegarek i datownik
					draw.text((1260,62), czas2, fill=bialy, font=self.srg_arial3)
					draw.text((1250,90), data, fill=bialy, font=self.srg_arial3)
					if (self.read_tacho == False):
						try:
							tempkm = 0
							with open(self.lookup_path + "/kilometry/" + state['name'][:-1] + "_przebieg.txt", "r") as self.tacho_file:
								tempkm = self.tacho_file.read()
								if tempkm == "":
									raise IOError
						except IOError:
							tempkm = (random()*1000)+(self.rok-2017)*140000+self.dzis*450
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
					self.print_center(draw, tekst + " km", 934,458, self.font, bialy)
					
				if self.aktyw<60:
					obrazek.paste(self.bootowanie, (0, 0))
				if self.aktyw>60:					
					draw.rectangle((0, 0, 640, 480), fill=czarny)	
					self.print_center(draw, u"Pulpit nieaktywny" , 320,240, self.font, niebieski_pixy)
				if self.aktyw>60 and state['cabactive'] == 1 and state['cab'] == 1 or state['cabactive'] == -1 and state['cab'] == -1:
								
					if self.tryb == 0:
						obrazek.paste(self.brak_konfigu, (0, 0))
					if self.tryb == 1:
						obrazek.paste(self.jest_konfigu, (0, 0))							
						
					if self.tryb == 2:					
						obrazek.paste(self.prawy, (0, 0))		
					if self.tryb == 3:					
						obrazek.paste(self.prawy, (0, 0))			
					if (pojazdy > 2):		
						
						obrazek.paste(self.ukrotnienie_slave,(338, 270))	
						obrazek.paste(self.brak_can,(1184, 240))
						draw.text((250,275), u'7,8,9', font=self.bardzo_maly_font, fill=czerwony)		
						draw.text((250,290), u'x,x,x', font=self.bardzo_maly_font, fill=czerwony)
						draw.text((400,275), u'10,11,12', font=self.bardzo_maly_font, fill=czerwony)		
						draw.text((410,290), u'x,x,x', font=self.bardzo_maly_font, fill=czerwony)									
						obrazek.paste(self.zaduzo, (0, 0))	
					if self.tryb == 0 or self.tryb == 1:						
						if (pojazdy >= 1):
							if (4 >= pojazdy >= 1):

								obrazek.paste(self.oswietlenie_czola,(26, 351))


								if (lights_front & 1):
									draw.ellipse([54,381,57,383],fill=bialy)
								if (lights_front & 16): 
									draw.ellipse([26,381,29,383],fill=bialy)
								if (lights_front & 4):
									draw.ellipse([41,359,43,361],fill=bialy)
								if (lights_front & 2):
									draw.ellipse([51,381,53,383],fill=czerwony)
								if (lights_front & 32):
									draw.ellipse([31,381,33,383],fill=czerwony)	
									


							draw.rectangle((15,260,625,325), fill=czarny)							
							obrazek.paste(self.ukrotnienie_master,(26, 270))
							draw.text((90,275), u'1,2,3', font=self.bardzo_maly_font, fill=bialy)		
							draw.text((90,290), u'x,x,x', font=self.bardzo_maly_font, fill=bialy)							


							if (war_panto_m_a):
								obrazek.paste(self.panto_m_a, (13, 231))
							if (war_uziom_m_a):
								obrazek.paste(self.uziom_m_a, (34, 231))
							if (war_ws_m_a):
								obrazek.paste(self.ws_m_a, (57, 231))
							if (war_kompresor_a):
								obrazek.paste(self.kompresor_a, (79, 231))
							if (war_pomocnicza):
								obrazek.paste(self.pantografowa, (104, 231))
							if (war_400v_m_a):
								obrazek.paste(self.u400v_m_a, (125, 231))
							if (war_bat_m_a):
								obrazek.paste(self.bat_m_a, (149, 231))
							if (war_przetwornica_a):
								obrazek.paste(self.przetwornica, (174, 235))
							if (war_odl_s_1_a):
								obrazek.paste(self.odl_s_1_a, (14, 317))
							if (war_odl_s_2_a):
								obrazek.paste(self.odl_s_2_a, (38, 317))
							if (war_ham_pos_a) or (war_ham_pos_b) or (war_ham_pos_c):
								obrazek.paste(self.ham_pos_a, (62, 317))
							if (war_cisnienie_a) or (war_cisnienie_b) or (war_cisnienie_c):
								obrazek.paste(self.cisnienie_a, (85, 317))
							if (war_inw_m_a):
								obrazek.paste(self.inw_m_a, (109, 317))
							if (war_a_m_a):
								obrazek.paste(self.a_m_a, (130, 317))
							if (war_sos_m_a):
								obrazek.paste(self.sos_m_a, (144, 317))
							if (war_awaria_a) or (war_awaria_b) or (war_awaria_c):
								obrazek.paste(self.awaria_a, (36, 279))		


							if (war_panto_m_d):
								obrazek.paste(self.panto_m_a, (189, 231))
							if (war_uziom_m_d): 
								obrazek.paste(self.uziom_m_a, (210, 231))
							if (war_ws_m_d):
								obrazek.paste(self.ws_m_a, (233, 231))
							if (war_kompresor_d):
								obrazek.paste(self.kompresor_a, (255, 231))
							if (war_pomocnicza):
								obrazek.paste(self.pantografowa, (285, 231))
							if (war_400v_m_d):
								obrazek.paste(self.u400v_m_a, (301, 231))
							if (war_bat_m_d):
								obrazek.paste(self.bat_m_a, (326, 231))
							if (war_przetwornica_d):
								obrazek.paste(self.przetwornica, (351, 235))
							if (war_odl_s_1_d):
								obrazek.paste(self.odl_s_1_a, (190, 317))
							if (war_odl_s_2_d):
								obrazek.paste(self.odl_s_2_a, (214, 317))
							if (war_inw_m_d):
								obrazek.paste(self.inw_m_a, (285, 317))
							if (war_a_m_d):
								obrazek.paste(self.a_m_a, (306, 317))
							if (war_sos_m_d):
								obrazek.paste(self.sos_m_a, (320, 317))	

							obrazek.paste(self.ukrotnienie_slave,(182, 270))						

							draw.text((250,275), u'4,5,6', font=self.bardzo_maly_font, fill=bialy)		
							draw.text((250,290), u'x,x,x', font=self.bardzo_maly_font, fill=bialy)

							if (war_awaria_d) or (war_awaria_e) or (war_awaria_f):
								obrazek.paste(self.awaria_a, (212, 279))	

							if (war_ham_pos_d) or (war_ham_pos_e) or (war_ham_pos_f):
								obrazek.paste(self.ham_pos_a, (238, 317))

							if (war_cisnienie_d) or (war_cisnienie_e) or (war_cisnienie_f):
								obrazek.paste(self.cisnienie_a, (261, 317))	
							obrazek.paste(self.oswietlenie_czola,(306, 351))								
							if (lights_rear & 1):
								draw.ellipse([334,381,337,383],fill=bialy)
							if (lights_rear & 16):
								draw.ellipse([306,383,309,383],fill=bialy)
							if (lights_rear & 4):
								draw.ellipse([321,359,323,361],fill=bialy)
							if (lights_rear & 2):
								draw.ellipse([331,381,333,383],fill=czerwony)
							if (lights_rear & 32):
								draw.ellipse([311,381,313,383],fill=czerwony)								
							
						
					if self.tryb == 2:	
						self.print_center(draw, "1", 97,281, self.bardzo_maly_font, bialy)
						self.print_center(draw, "2", 245,281, self.bardzo_maly_font, bialy)
						self.print_center(draw, "3", 392,281, self.bardzo_maly_font, bialy)
						
						draw.ellipse([31,353,51,373],fill=szary)						
						if  state['cab'] == 1:
							self.print_center(draw, "A", 41,362, self.bardzo_maly_font, bialy)
						if  state['cab'] == -1:
							self.print_center(draw, "F", 41,362, self.bardzo_maly_font, bialy)
								
					
						obrazek.paste(self.przelaczanie, (488, 195))
						self.print_center(draw, "4,5,6", 546,210, self.maly_font, bialy)									
				
					#CZŁON A
						if (war_panto_m_a):
							obrazek.paste(self.panto_m_a, (13, 231))
						if (war_uziom_m_a):
							obrazek.paste(self.uziom_m_a, (34, 231))
						if (war_ws_m_a):
							obrazek.paste(self.ws_m_a, (57, 231))
						if (war_kompresor_a):
							obrazek.paste(self.kompresor_a, (79, 231))
						if (war_pomocnicza):
							obrazek.paste(self.pantografowa, (104, 231))	
						if (war_400v_m_a):
							obrazek.paste(self.u400v_m_a, (129, 231))
						if (war_bat_m_a):
							obrazek.paste(self.bat_m_a, (154, 231))
						if (war_przetwornica_a):
							obrazek.paste(self.przetwornica, (179, 235))
						if (war_odl_s_1_a):
							obrazek.paste(self.odl_s_1_a, (14, 317))
						if (war_odl_s_2_a):
							obrazek.paste(self.odl_s_2_a, (38, 317))
						if (war_ham_pos_a):
							obrazek.paste(self.ham_pos_a, (62, 317))
						if (war_cisnienie_a):
							obrazek.paste(self.cisnienie_a, (85, 317))
						if (war_inw_m_a):
							obrazek.paste(self.inw_m_a, (109, 317))
						if (war_a_m_a):
							obrazek.paste(self.a_m_a, (130, 317))
						if (war_sos_m_a):
							obrazek.paste(self.sos_m_a, (144, 317))
						if (war_awaria_a):
							obrazek.paste(self.awaria_a, (36, 279))

					#CZŁON B
						if (war_ham_pos_b):
							obrazek.paste(self.ham_pos_a, (209, 317))
						if (war_cisnienie_b):
							obrazek.paste(self.cisnienie_a, (232, 317))
					#CZŁON C
						if (war_ham_pos_c):
							obrazek.paste(self.ham_pos_a, (356, 317))
						if (war_cisnienie_c):
							obrazek.paste(self.cisnienie_a, (379, 317))	



					#RYSOWANIE DRZWI
						if (war_cab == 1):
							#człon A
							if (war_c1_d1P):
								draw.rectangle((52,260,53,271), fill=zolty)
								draw.rectangle((70,260,71,271), fill=zolty)
								draw.rectangle((122,260,123,271), fill=zolty)
								draw.rectangle((140,260,141,271), fill=zolty)
							else:	
								draw.rectangle((52,270,71,271), fill=zolty)
								draw.rectangle((122,270,141,271), fill=zolty)
							if (war_c1_ds1P):
								draw.rectangle((56,262,67,271), fill=zolty)
								draw.rectangle((126,262,137,271), fill=zolty)

							if (war_c1_d1L):	
								draw.rectangle((52,305,53,316), fill=zolty)
								draw.rectangle((70,305,71,316), fill=zolty)
								draw.rectangle((122,305,123,316), fill=zolty)
								draw.rectangle((140,305,141,316), fill=zolty)
							else:	
								draw.rectangle((52,305,71,306), fill=zolty)
								draw.rectangle((122,305,141,306), fill=zolty)
							if (war_c1_ds1L):
								draw.rectangle((56,305,67,314), fill=zolty)
								draw.rectangle((126,305,137,314), fill=zolty)

							#człon B
							if (war_c2_d2P):	
								draw.rectangle((199,260,200,271), fill=zolty)
								draw.rectangle((217,260,218,271), fill=zolty)
								draw.rectangle((269,260,270,271), fill=zolty)
								draw.rectangle((287,260,288,271), fill=zolty)
							else:	
								draw.rectangle((199,270,218,271), fill=zolty)
								draw.rectangle((269,270,288,271), fill=zolty)
							if (war_c2_ds2P):
								draw.rectangle((203,262,214,271), fill=zolty)
								draw.rectangle((273,262,284,271), fill=zolty)

							if (war_c2_d2L):	
								draw.rectangle((199,305,200,316), fill=zolty)
								draw.rectangle((217,305,218,316), fill=zolty)
								draw.rectangle((269,305,270,316), fill=zolty)
								draw.rectangle((287,305,288,316), fill=zolty)
							else:	
								draw.rectangle((199,305,218,306), fill=zolty)
								draw.rectangle((269,305,288,306), fill=zolty)
							if (war_c2_ds2L):
								draw.rectangle((203,305,214,314), fill=zolty)
								draw.rectangle((273,305,284,314), fill=zolty)

							#człon C
							if (war_c3_d3P):	
								draw.rectangle((346,260,347,271), fill=zolty)
								draw.rectangle((364,260,365,271), fill=zolty)
								draw.rectangle((416,260,417,271), fill=zolty)
								draw.rectangle((434,260,435,271), fill=zolty)
							else:	
								draw.rectangle((346,270,365,271), fill=zolty)
								draw.rectangle((416,270,435,271), fill=zolty)
							if (war_c3_ds3P):
								draw.rectangle((350,262,361,271), fill=zolty)
								draw.rectangle((420,262,431,271), fill=zolty)

							if (war_c3_d3L):	
								draw.rectangle((346,305,347,316), fill=zolty)
								draw.rectangle((364,305,365,316), fill=zolty)
								draw.rectangle((416,305,417,316), fill=zolty)
								draw.rectangle((434,305,435,316), fill=zolty)
							else:	
								draw.rectangle((346,305,365,306), fill=zolty)
								draw.rectangle((416,305,435,306), fill=zolty)
							if (war_c3_ds3L):
								draw.rectangle((350,305,361,314), fill=zolty)
								draw.rectangle((420,305,431,314), fill=zolty)



						#druga kabina
						else:
							#człon A
							if (war_c1_d1L):
								draw.rectangle((52,260,53,271), fill=zolty)
								draw.rectangle((70,260,71,271), fill=zolty)
								draw.rectangle((122,260,123,271), fill=zolty)
								draw.rectangle((140,260,141,271), fill=zolty)
							else:	
								draw.rectangle((52,270,71,271), fill=zolty)
								draw.rectangle((122,270,141,271), fill=zolty)
							if (war_c1_ds1L):
								draw.rectangle((56,262,67,271), fill=zolty)
								draw.rectangle((126,262,137,271), fill=zolty)

							if (war_c1_d1P):	
								draw.rectangle((52,305,53,316), fill=zolty)
								draw.rectangle((70,305,71,316), fill=zolty)
								draw.rectangle((122,305,123,316), fill=zolty)
								draw.rectangle((140,305,141,316), fill=zolty)
							else:	
								draw.rectangle((52,305,71,306), fill=zolty)
								draw.rectangle((122,305,141,306), fill=zolty)
							if (war_c1_ds1P):
								draw.rectangle((56,305,67,314), fill=zolty)
								draw.rectangle((126,305,137,314), fill=zolty)

							#człon B
							if (war_c2_d2L):	
								draw.rectangle((199,260,200,271), fill=zolty)
								draw.rectangle((217,260,218,271), fill=zolty)
								draw.rectangle((269,260,270,271), fill=zolty)
								draw.rectangle((287,260,288,271), fill=zolty)
							else:	
								draw.rectangle((199,270,218,271), fill=zolty)
								draw.rectangle((269,270,288,271), fill=zolty)
							if (war_c2_ds2L):
								draw.rectangle((203,262,214,271), fill=zolty)
								draw.rectangle((273,262,284,271), fill=zolty)

							if (war_c2_d2P):	
								draw.rectangle((199,305,200,316), fill=zolty)
								draw.rectangle((217,305,218,316), fill=zolty)
								draw.rectangle((269,305,270,316), fill=zolty)
								draw.rectangle((287,305,288,316), fill=zolty)
							else:	
								draw.rectangle((199,305,218,306), fill=zolty)
								draw.rectangle((269,305,288,306), fill=zolty)
							if (war_c2_ds2P):
								draw.rectangle((203,305,214,314), fill=zolty)
								draw.rectangle((273,305,284,314), fill=zolty)

							#człon C
							if (war_c3_d3L):	
								draw.rectangle((346,260,347,271), fill=zolty)
								draw.rectangle((364,260,365,271), fill=zolty)
								draw.rectangle((416,260,417,271), fill=zolty)
								draw.rectangle((434,260,435,271), fill=zolty)
							else:	
								draw.rectangle((346,270,365,271), fill=zolty)
								draw.rectangle((416,270,435,271), fill=zolty)
							if (war_c3_ds3L):
								draw.rectangle((350,262,361,271), fill=zolty)
								draw.rectangle((420,262,431,271), fill=zolty)

							if (war_c3_d3P):	
								draw.rectangle((346,305,347,316), fill=zolty)
								draw.rectangle((364,305,365,316), fill=zolty)
								draw.rectangle((416,305,417,316), fill=zolty)
								draw.rectangle((434,305,435,316), fill=zolty)
							else:	
								draw.rectangle((346,305,365,306), fill=zolty)
								draw.rectangle((416,305,435,306), fill=zolty)
							if (war_c3_ds3P):
								draw.rectangle((350,305,361,314), fill=zolty)
								draw.rectangle((420,305,431,314), fill=zolty)

								

					if self.tryb == 3 and pojazdy == 1:	
						self.print_center(draw, "6", 97,281, self.bardzo_maly_font, bialy)
						self.print_center(draw, "5", 245,281, self.bardzo_maly_font, bialy)
						self.print_center(draw, "4", 392,281, self.bardzo_maly_font, bialy)					
						obrazek.paste(self.przelaczanie, (488, 195))	
						self.print_center(draw, "1,2,3", 546,210, self.maly_font, bialy)							
						
					#CZŁON F
						if (war_panto_m_d):
							obrazek.paste(self.panto_m_a, (13, 231))
						if (war_uziom_m_d):
							obrazek.paste(self.uziom_m_a, (34, 231))
						if (war_ws_m_d):
							obrazek.paste(self.ws_m_a, (57, 231))
						if (war_kompresor_d):
							obrazek.paste(self.kompresor_a, (79, 231))
						if (war_pomocnicza):
							obrazek.paste(self.pantografowa, (104, 231))	
						if (war_400v_m_d):
							obrazek.paste(self.u400v_m_a, (129, 231))
						if (war_bat_m_d):
							obrazek.paste(self.bat_m_a, (154, 231))
						if (war_przetwornica_d):
							obrazek.paste(self.przetwornica, (179, 235))
						if (war_odl_s_1_d):
							obrazek.paste(self.odl_s_1_a, (14, 317))
						if (war_odl_s_2_d):
							obrazek.paste(self.odl_s_2_a, (38, 317))
						if (war_ham_pos_f):
							obrazek.paste(self.ham_pos_a, (62, 317))
						if (war_cisnienie_f):
							obrazek.paste(self.cisnienie_a, (85, 317))
						if (war_inw_m_d):
							obrazek.paste(self.inw_m_a, (109, 317))
						if (war_a_m_d):
							obrazek.paste(self.a_m_a, (130, 317))
						if (war_sos_m_d):
							obrazek.paste(self.sos_m_a, (144, 317))
						if (war_awaria_d):
							obrazek.paste(self.awaria_a, (36, 279))

					#CZŁON E
						if (war_ham_pos_e):
							obrazek.paste(self.ham_pos_a, (209, 317))
						if (war_cisnienie_e):
							obrazek.paste(self.cisnienie_a, (232, 317))
					#CZŁON D
						if (war_ham_pos_d):
							obrazek.paste(self.ham_pos_a, (356, 317))
						if (war_cisnienie_d):
							obrazek.paste(self.cisnienie_a, (379, 317))	



					#RYSOWANIE DRZWI
						if (war_cab == 1):
							#człon F
							if (war_c6_d6P):
								draw.rectangle((52,260,53,271), fill=zolty)
								draw.rectangle((70,260,71,271), fill=zolty)
								draw.rectangle((122,260,123,271), fill=zolty)
								draw.rectangle((140,260,141,271), fill=zolty)
							else:	
								draw.rectangle((52,270,71,271), fill=zolty)
								draw.rectangle((122,270,141,271), fill=zolty)
							if (war_c6_ds6P):
								draw.rectangle((56,262,67,271), fill=zolty)
								draw.rectangle((126,262,137,271), fill=zolty)

							if (war_c6_d6L):	
								draw.rectangle((52,305,53,316), fill=zolty)
								draw.rectangle((70,305,71,316), fill=zolty)
								draw.rectangle((122,305,123,316), fill=zolty)
								draw.rectangle((140,305,141,316), fill=zolty)
							else:	
								draw.rectangle((52,305,71,306), fill=zolty)
								draw.rectangle((122,305,141,306), fill=zolty)
							if (war_c6_ds6L):
								draw.rectangle((56,305,67,314), fill=zolty)
								draw.rectangle((126,305,137,314), fill=zolty)

							#człon E
							if (war_c5_d5P):	
								draw.rectangle((199,260,200,271), fill=zolty)
								draw.rectangle((217,260,218,271), fill=zolty)
								draw.rectangle((269,260,270,271), fill=zolty)
								draw.rectangle((287,260,288,271), fill=zolty)
							else:	
								draw.rectangle((199,270,218,271), fill=zolty)
								draw.rectangle((269,270,288,271), fill=zolty)
							if (war_c5_ds5P):
								draw.rectangle((203,262,214,271), fill=zolty)
								draw.rectangle((273,262,284,271), fill=zolty)

							if (war_c5_d5L):	
								draw.rectangle((199,305,200,316), fill=zolty)
								draw.rectangle((217,305,218,316), fill=zolty)
								draw.rectangle((269,305,270,316), fill=zolty)
								draw.rectangle((287,305,288,316), fill=zolty)
							else:	
								draw.rectangle((199,305,218,306), fill=zolty)
								draw.rectangle((269,305,288,306), fill=zolty)
							if (war_c5_ds5L):
								draw.rectangle((203,305,214,314), fill=zolty)
								draw.rectangle((273,305,284,314), fill=zolty)

							#człon D
							if (war_c4_d4P):	
								draw.rectangle((346,260,347,271), fill=zolty)
								draw.rectangle((364,260,365,271), fill=zolty)
								draw.rectangle((416,260,417,271), fill=zolty)
								draw.rectangle((434,260,435,271), fill=zolty)
							else:	
								draw.rectangle((346,270,365,271), fill=zolty)
								draw.rectangle((416,270,435,271), fill=zolty)
							if (war_c4_ds4P):
								draw.rectangle((350,262,361,271), fill=zolty)
								draw.rectangle((420,262,431,271), fill=zolty)

							if (war_c4_d4L):	
								draw.rectangle((346,305,347,316), fill=zolty)
								draw.rectangle((364,305,365,316), fill=zolty)
								draw.rectangle((416,305,417,316), fill=zolty)
								draw.rectangle((434,305,435,316), fill=zolty)
							else:	
								draw.rectangle((346,305,365,306), fill=zolty)
								draw.rectangle((416,305,435,306), fill=zolty)
							if (war_c4_ds4L):
								draw.rectangle((350,305,361,314), fill=zolty)
								draw.rectangle((420,305,431,314), fill=zolty)



						#druga kabina
						else:
							#człon F
							if (war_c6_d6L):
								draw.rectangle((52,260,53,271), fill=zolty)
								draw.rectangle((70,260,71,271), fill=zolty)
								draw.rectangle((122,260,123,271), fill=zolty)
								draw.rectangle((140,260,141,271), fill=zolty)
							else:	
								draw.rectangle((52,270,71,271), fill=zolty)
								draw.rectangle((122,270,141,271), fill=zolty)
							if (war_c6_ds6L):
								draw.rectangle((56,262,67,271), fill=zolty)
								draw.rectangle((126,262,137,271), fill=zolty)

							if (war_c6_d6P):	
								draw.rectangle((52,305,53,316), fill=zolty)
								draw.rectangle((70,305,71,316), fill=zolty)
								draw.rectangle((122,305,123,316), fill=zolty)
								draw.rectangle((140,305,141,316), fill=zolty)
							else:	
								draw.rectangle((52,305,71,306), fill=zolty)
								draw.rectangle((122,305,141,306), fill=zolty)
							if (war_c6_ds6P):
								draw.rectangle((56,305,67,314), fill=zolty)
								draw.rectangle((126,305,137,314), fill=zolty)

							#człon E
							if (war_c5_d5L):	
								draw.rectangle((199,260,200,271), fill=zolty)
								draw.rectangle((217,260,218,271), fill=zolty)
								draw.rectangle((269,260,270,271), fill=zolty)
								draw.rectangle((287,260,288,271), fill=zolty)
							else:	
								draw.rectangle((199,270,218,271), fill=zolty)
								draw.rectangle((269,270,288,271), fill=zolty)
							if (war_c5_ds5L):
								draw.rectangle((203,262,214,271), fill=zolty)
								draw.rectangle((273,262,284,271), fill=zolty)

							if (war_c5_d5P):	
								draw.rectangle((199,305,200,316), fill=zolty)
								draw.rectangle((217,305,218,316), fill=zolty)
								draw.rectangle((269,305,270,316), fill=zolty)
								draw.rectangle((287,305,288,316), fill=zolty)
							else:	
								draw.rectangle((199,305,218,306), fill=zolty)
								draw.rectangle((269,305,288,306), fill=zolty)
							if (war_c5_ds5P):
								draw.rectangle((203,305,214,314), fill=zolty)
								draw.rectangle((273,305,284,314), fill=zolty)

							#człon D
							if (war_c4_d4L):	
								draw.rectangle((346,260,347,271), fill=zolty)
								draw.rectangle((364,260,365,271), fill=zolty)
								draw.rectangle((416,260,417,271), fill=zolty)
								draw.rectangle((434,260,435,271), fill=zolty)
							else:	
								draw.rectangle((346,270,365,271), fill=zolty)
								draw.rectangle((416,270,435,271), fill=zolty)
							if (war_c4_ds4L):
								draw.rectangle((350,262,361,271), fill=zolty)
								draw.rectangle((420,262,431,271), fill=zolty)

							if (war_c4_d4P):	
								draw.rectangle((346,305,347,316), fill=zolty)
								draw.rectangle((364,305,365,316), fill=zolty)
								draw.rectangle((416,305,417,316), fill=zolty)
								draw.rectangle((434,305,435,316), fill=zolty)
							else:	
								draw.rectangle((346,305,365,306), fill=zolty)
								draw.rectangle((416,305,435,306), fill=zolty)
							if (war_c4_ds4P):
								draw.rectangle((350,305,361,314), fill=zolty)
								draw.rectangle((420,305,431,314), fill=zolty)



		
					#tempomat
					if state['speedctrlactive']:
						if (((state['seconds'] % 2) == 1) or (state['speedctrlstandby']==False)):
							draw.text((253,1), 'UPZ', fill=niebieski, font=self.arialbold16)
							self.print_right(draw, '%d' % (war_speedctrlpower * 100) + '%', 284, 26, self.arialbold16, niebieski)
						draw.text((292,10), 'Vz =', fill=bialy, font=self.arialbold16)
						self.print_right(draw, '%d' % war_speedctrl , 370, 18, self.srg_arial2, niebieski)
						draw.text((372,12), 'km/h', fill=bialy, font=self.bardzo_maly_font)

		#GÓRNE
					if (war_ws_d):
						obrazek.paste(self.ws_d, (444, 37))
					if (war_lewe_drzwi_a):
						if (war_cab == 1):
							obrazek.paste(self.lewe_drzwi_a, (486, 37))
						else:
							obrazek.paste(self.prawe_drzwi_a, (486, 70))
					if (war_prawe_drzwi_a):
						if (war_cab == 1):
							obrazek.paste(self.prawe_drzwi_a, (486, 70))
						else:
							obrazek.paste(self.lewe_drzwi_a, (486, 37))
					if (war_pozar):
						obrazek.paste(self.pozar, (539, 37))
					if (war_uziom):
						obrazek.paste(self.uziom, (444, 70))
					if (war_a):
						obrazek.paste(self.a, (539, 70))
					if (war_osw):
						obrazek.paste(self.osw, (444, 105))
						obrazek.paste(self.ukrotnienie, (520, 3))	
					if (war_p):
						obrazek.paste(self.p, (486, 105))
					if (war_r):
						obrazek.paste(self.r, (486, 105))
					if (war_inw):
						obrazek.paste(self.inw, (539, 105))
					if (war_piorun):
						obrazek.paste(self.piorun, (444, 135))
					if (war_piach):
						obrazek.paste(self.piach, (486, 135))
					if (war_poslizg_s):
						obrazek.paste(self.poslizg_s, (539, 135))
					if (war_400v):
						obrazek.paste(self.u400v, (486, 164))
					if (war_sos):
						obrazek.paste(self.sos, (539, 164))
					if (war_kier_P):
						obrazek.paste(self.kier_P, (13, 70))
					if (war_kier_t):
						obrazek.paste(self.kier_t, (13, 106))
					if (war_ladowanie):
						obrazek.paste(self.brak_ladowania, (539, 135))
					if state['door_lock'] == 0:
						obrazek.paste(self.blokada, (1, 1))								
							

				#SŁUPKI
					# slupek MZ i jego wartosc = READY
					draw.rectangle((41,101-(mz*60),81,101), fill=pomarancz) #PrZ
					prad = 100 * mz
					self.print_fixed_with(draw, '%d' % prad, (25, 166), 5, self.arialbold16, pomarancz)
					self.print_fixed_with(draw, '%', (80, 166), 1, self.arialbold16, bialy)
							
					# slupek MR i jego wartosc = READY
					#prad = mr4+mr5+mr6
					#self.print_fixed_with(draw, '%d kN' % prad, (170, 179), 7, self.bardzo_maly_font, pomarancz)
					prad = mr1
					self.print_fixed_with(draw, '%d kN' % prad, (170, 166), 7, self.bardzo_maly_font, pomarancz)
					if prad > 100:
						prad = 100
					if prad < -100:
						prad = -100
					draw.rectangle((170,101-((prad)*0.60),190,101), fill=pomarancz) #Siła

					# slupek pradu i jego wartosc = READY
					prad1 = state['eimp_c1_ihv'] + state['eimp_c2_ihv'] + state['eimp_c3_ihv']
					prad2 = state['eimp_c4_ihv'] + state['eimp_c5_ihv'] + state['eimp_c6_ihv']	
					slupek = prad1 + prad2
					self.print_fixed_with(draw, '%d A' % slupek, (265, 166), 6, self.bardzo_maly_font, pomarancz)					
					if slupek > 700:
						slupek = 700
					if slupek < -700:
						slupek = -700					
					pos = 102 - (slupek * 60 / 700)
					draw.rectangle((266,pos,285,102), fill=pomarancz)

					#self.print_fixed_with(draw, '%d A' % prad2, (265, 177), 6, self.bardzo_maly_font, pomarancz)


					# slupek napiecia i jego wartosc = READY
					prad = state['voltage']
					if prad < 0:
						prad = 0
					pos = (max(min(prad,4000),2000)-2000)*120/2000
					draw.rectangle((363,161-pos,382,161), fill=pomarancz)
					prad = prad * 0.001
					self.print_fixed_with(draw, '%1.2f kV' % prad, (362, 166), 7, self.bardzo_maly_font, pomarancz)
				else:
					self.tryb = 0 	

			
		else:
			# szansa na zbicie zepsucia jesli wlasnie wylaczono baterie
			if self.awaria and self.aktyw > 0 and random() < 0.4:
				self.awaria = False
			
			self.aktyw = 0
			
		self.stan1 = state['universal1']
		self.stan2 = state['universal2']
		self.stan4 = state['universal4']
		self.stan5 = state['universal5']
		self.stan6 = state['universal6']			
			
		return obrazek


