import requests
import optparse
import urllib
import urllib.request
import os
import time
acik=""
parse = optparse.OptionParser()
parse.add_option("-u","--url",dest="url",help="Enter the url (required) (Url Giriniz gerekli)")
cevap,arguman=parse.parse_args()
url = cevap.url
os.system("pip install requests")
os.system("pip install colorama")
from colorama import Fore, Back, Style, init
os.system("pkg install figlet")
os.system("clear")
os.system("figlet BASIC WEB SCANNER")
print(Back.BLUE+"""Bu Araç Yakup Eroğlu Tarafından Yapılan Temel Sql İnjection ve XSS(Cross Site Scripting) Açıklarının""")
print(Style.RESET_ALL)
print("                 "+Back.BLUE+"""Tespit Edilmesi Amacıyla Yazılmış Bir Web Tarayıcısıdır """)
print(Style.RESET_ALL)
print(f"[*] Url:{url} ")
i=0
while i<5:
	time.sleep(0.2)
	print("\r[*] Scanning Url",end=""+".")
	time.sleep(0.2)
	print("\r[*] Scanning Url",end=""+"..")
	time.sleep(0.2)
	print("\r[*] Scanning Url",end=""+"...")
	time.sleep(0.2)
	print("\r[*] Scanning Url",)
	i+=1
try:
	request=urllib.request.urlopen(url+"'")
	#except:
	requestt=request.read()
	requesttt=requestt.decode("utf-8")
	#print(Fore.GREEN+requesttt)
	#print(Style.RESET_ALL)
	if ("SQL syntax") or ("mysql_fetch_array()") in requesttt:
		acik=acik+"a"
	else:
		acik=acik
	if(acik=="a"):
		print(Fore.RED+"\n[*]KRITIK ACIK (SQL INJECTION) TESPIT EDILDI")
		print(Style.RESET_ALL)
	else:
		print(Fore.GREEN+"\n[*] SQL INJECTION TESPIT EDILEMEDI")
except:
	print(Fore.GREEN+"\n[*] SQL INJECTION TESPIT EDILEMEDI")
	print(Style.RESET_ALL)
    


















