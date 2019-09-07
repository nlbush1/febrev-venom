import os
if os.path.isfile("/bin/febrev"):
  os.system("rm /bin/febrev")
else:
  print("........................................................................................................")
print("""
███████╗███████╗██████╗ ██████╗ ███████╗██╗   ██╗                     
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║   ██║                     
█████╗  █████╗  ██████╔╝██████╔╝█████╗  ██║   ██║                     
██╔══╝  ██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ╚██╗ ██╔╝                     
██║     ███████╗██████╔╝██║  ██║███████╗ ╚████╔╝                      
╚═╝     ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝  ╚═══╝                       
                                                                      
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                      
""")
os.system("sudo apt-get install python3-pip")
os.system("sudo apt-get install zenity")
os.system("python3 -m pip install zenipy")
os.system("python3 -m pip install click")
metasploit=input("IS METASPLOIT-FRAMEWORK ALREADY INSTALLED IN YOUR SYSTEM ? [Y/n] : ")
if metasploit=="n" or metasploit=="N":
            print("Installing Metasploit.........")
            os.sytem("sudo apt-get install metasploit -y  > /dev/null")
else:
     print("NICE ......!")

apksign=input("IS APKSIGNER ALREADY INSTALLED IN YOUR SYSTEM? [Y/n]? : ")
if apksign=="n" or apksign=="N":
           print("INSTALLING APKSIGNER....")
           os.system("sudo apt-get install apksigner -y > /dev/null")
else: 
     print("NICE .....")
     

openssh=input("IS openssh INSTALLED IN YOUR SYSTEM? [Y/n] : ")
if openssh=="n" or openssh=="N":
           print("Installing ssh")
           os.system("sudo apt-get install openssh -y > /dev/null")

apache=input("IS APACHE2 SERVER IS INSTALLED IN YOUR SYSTEM? [Y/n] : ")
if apache=="n" or apache=="N":
          os.system("sudo apt-get install apache2 -y > /dev/null")
else:
     print("HURRAY....")

path=os.getcwd()
with open("febrev.sh","w+") as fr:
      fr.write(f"python3 {path}/febrev-venom.py")
os.system(f"cp {path}/febrev.sh /bin/febrev")
os.system("chmod +x /bin/febrev")
print("")
print("NOW YOU CAN RUN FEBREV-VENOM FROM ANYWERE BY TYPING COMMAND  >>  febrev")
exiting=input("ENTER ANY KEY TO CONTINUE.......!!!!! ")
print(" ")
print(" ")
print(" ")




print("STARTING FEBREV VENOM......#######################")
os.system("chmod +x *")
os.system("sudo python3 febrev-venom.py")
