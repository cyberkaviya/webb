import subprocess
import webbrowser
from urllib.request import Request, urlopen


subprocess.run('clear')

print ("\033[1;33;40m           _  __           _")
print ("\033[1;33;40m          | |/ /__ ___   _(_)_   _  __ _")
print ("\033[1;33;40m          | ' // _` \ \ / / | | | |/ _` |")
print ("\033[1;33;40m          | . \ (_| |\ V /| | |_| | (_| |")
print ("\033[1;33;40m          |_|\_\__,_| \_/ |_|\__, |\__,_|")
print ("\033[1;33;40m                             |___/         ")
print ("\033[1;37;40mmy blog  -  cyberkaviya.blogspot.com")
print ("\033[1;36;40m***********************************************")
print ("\033[1;36;40m|  "+"\033[1;33;40m            Welcome to my Area  "+"\033[1;36;40m           |")
print ("\033[1;36;40m***********************************************")

print ("\n")

print ("\033[1;33;40m[1] "+"\033[1;32;40m Webbrouser")
print ("\033[1;33;40m[2] "+"\033[1;32;40m See web source")
print ("\033[1;33;40m[3] "+"\033[1;32;40m Download web source")

print ("\n")
print ("\n")

q1=int(input("\033[1;31;40mEnter Number : "))
print ("""\033[1;36;40m°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°""")
print ("\n")



if q1==1:
	q2=input("\033[1;33;40m[*]"+"\033[1;32;40m Enter URL"+"\033[1;36;40m: ")
	def url():
	        print ("First install w3m...." +"type "+"\033[1;37;40m apt install w3m "+"\033[1;36;40m and Enter after run this script again....")
        	webbrowser.open_new(q2);
	url()

elif q1==2:
	q3=input("\033[1;33;40m[*]"+"\033[1;32;40m Enter URL"+"\033[1;36;40m: ")
	s=Request(q3, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(s).read()
	a=webpage.decode("utf-8")
	print (a)

elif q1==3:
	import os
	q3=input("\033[1;33;40m[*]"+"\033[1;32;40m Enter URL"+"\033[1;36;40m: ")
	s=Request(q3, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(s).read()
	a=webpage.decode("utf-8")
	q=input('\033[1;33;40m[*]'+'\033[1;32;40m Enter file path'+'\033[1;36;40m: ')
	os.chdir(q)
	q1=input('[*]Enter file name: ')
	o=open(q1,"w+")
	o.write(a)

else:	print ('Incorect!')
