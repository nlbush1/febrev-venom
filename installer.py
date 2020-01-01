import os
metasploit=os.path.exists("/usr/bin/msfvenom")
if metasploit is True:
	print("\033[1;32m METASPLOIT IS INSTALLED =====> [ok]")
else:
	print("\033[1;31m METASPLOIT IS NOT INSTALLED =====> [x]")
	os.system("sudo apt-get install metasploit-framework")
openssh=os.path.exists("/usr/bin/ssh")
if openssh is True:
	print("\033[1;32m OPENSSH IS INSTALLED =====> [ok]")
else:
	print("\033[1;31m OPENSSH IS NOT INSTALLED =====> [x]")
	os.system("sudo apt-get install openssh")
zenity=os.path.exists("/usr/bin/zenity")
if zenity is True:
	print("\033[1;32m ZENITY IS INSTALLED =====> [ok]")
else:
	print("\033[1;31m ZENITY IS NOT INSTALLED =====> [x]")
	os.system("sudo apt-get install zenity")
print("\033[1;32m Installing Support libraries")
os.system("sudo python3 -m pip install click")
os.system("sudo apt-get install apache2")
os.system("sudo apt-get install espeak")
