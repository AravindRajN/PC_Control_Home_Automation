import pyttsx3
import speech_recognition as sr
#gui import
from tkinter import *
def color():
    import os
    os.system("color a")
color()
print('''
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
*    C C C C         A             L             L           *
*   C               A A            L             L           *
*  C               A   A           L             L           *
* C               A     A          L             L           *
*  C             AAAAAAAAA         L             L           *
*   C           A         A        L             L           *
*    C C C C   A           A       LLLLLLLLLL    LLLLLLLLLL  *
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
''')
#1
def ipaddress():
    from num2words import num2words
    import socket
    from plyer import notification
    import os
    import pyperclip as pc
    i= str(os.getcwd()+ '\\callls.ico')
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    speak(f"IP address of Hostname: {hostname} is")
    print(hostname)
    print(ip_address)
    pc.copy(ip_address)
    a=str(ip_address).replace(".","")
    notification.notify(title="Your IP Address", message=str(ip_address),app_icon = i,timeout = 5)
    for i in range(0,len(a)):
        c=a[i]
        speak(num2words(c))
#2        
def battery():
    from plyer import notification
    import psutil
    from num2words import num2words
    import os
    i= str(os.getcwd()+ '\\callls.ico')
    try:
        battery=psutil.sensors_battery()
        percent=battery.percent
        notification.notify(title="Battery Percentage", message=str(percent)+ "%Percent Remaining",app_icon = i,timeout = 5)
        a=num2words(percent, to='ordinal')+'percentage sir'
        speak(a)
    except:
        notification.notify(title="Battery Percentage", message="No Battery Found",app_icon = i,timeout = 5)
        speak("your device as no battery")
#3
def shutdown(c):
    import os
    try:
        from num2words import num2words
        numbers = [int(word) for word in c.split() if word.isdigit()]
        numbertowords=str(num2words(numbers[0]))
        speak("shutting down the computer in "+numbertowords+" seconds")
        code="shutdown /s /t "+str(numbers[0])
        os.system(code)
        print(code)
    except:
        speak("shutting the computer")
        os.system("shutdown /s /t 1")
#4
def deviceconfig():
    import wmi
    c = wmi.WMI( )
    my_system = c.Win32_ComputerSystem()[0]
    print(f"Manufacturer: {my_system.Manufacturer}")
    print(f"Model: {my_system. Model}")
    print(f"Name: {my_system.Name}")
    print(f"NumberOfProcessors:{my_system.NumberOfProcessors}")
    print(f"SystemType: {my_system. SystemType}")
    print(f"SystemFamily: {my_system. SystemFamily}")
    speak(f"Manufacturer: {my_system.Manufacturer}")
    speak(f"Model: {my_system. Model}")
    speak(f"Name: {my_system.Name}")
    speak(f"NumberOfProcessors:{my_system.NumberOfProcessors}")
    speak(f"SystemType: {my_system. SystemType}")
    speak(f"SystemFamily: {my_system. SystemFamily}")
#5
def opens(c):
    def notepad():
        import os
        speak("opening notepad")
        os.system("Notepad")
    def whatsapp():
        import webbrowser
        webbrowser.open('https://web.whatsapp.com/')
        speak("opening Whatsapp")
    def chrome():
        import webbrowser
        webbrowser.open('chrome')
        speak("opening chrome")
    def facebook():
        import webbrowser
        webbrowser.open('https://www.facebook.com/login/web/')
        speak("opening Facebook")
    def instgram():
        import webbrowser
        webbrowser.open('https://www.instagram.com/')
        speak("opening Instagram")
    def youtube():
        import webbrowser
        webbrowser.open('https://www.youtube.com/')
        speak("opening Youtube")
    def twitter():
        import webbrowser
        webbrowser.open('https://twitter.com/login')
        speak("opening Twitter")
    def controlpanel():
        import os
        os.system("control panel")
        speak("opening control panel")
    def systemsetting():
        import os
        os.system("start ms-settings:")
        speak("opening system settings")
    def cmd():
        import subprocess
        subprocess.call(['cmd.exe'])
        speak("opening command prompt")
    def taskmanger():
        import os
        os.system("taskmgr")
    def mail():
        import webbrowser
        webbrowser.open("https://mail.google.com/")
    if "chrome" in c:
        chrome()
    if "whatsapp" in c:
        whatsapp()
    if "mail" in c:
        mail()
    if "controlpanel" in c.replace(" ",""):
        controlpanel()
    if "systemsetting" in c.replace(" ",""):
        systemsetting()
    if "cmd" in c or "command prompt" in c or "terminal" in c:
        cmd()
    if "facebook" in c:
        facebook()
    if "instagram" in c:
        instgram()
    if "youtube" in c:
        youtube()
    if "notepad" in c:
        notepad()
    if "taskmanager" in c.replace(" ",""):
        taskmanger()
    if "twitter" in c:
        twitter()
#6
def instagram(c):
    
    def profile():
        from PIL import ImageTk, Image
        from instagramy import InstagramUser
        import instaloader
    #fuction defining
        
        def accountverfication():
            
            try:
                dp=link.get()
                user=InstagramUser(dp,from_cache=True)
                if user.is_verified ==True:
                    root.update()
                    ink.set("It is a Verified account")
                    speak("It is a Verified account")
                else:
                    root.update()
                    link.set("It is not a Verified account")
                    speak("It is not a Verified account")
            except Exception as e:
                myVar.set("Invalid Username")
                speak("Invalid Username")
                root.update()
                link.set("Enter the correct Username")
                speak("Enter the correct Username")
        def profilephoto():
            
            try:
                myVar.set("Downloading...")
                speak("Downloading...")
                root.update()
                ig=instaloader.Instaloader()
                dp=link.get()
                ig.download_profile(dp, profile_pic_only=True)
                myVar.set("Downloaded")
                speak("Downloaded")
                link.set("Profile photo downloaded successfully")
                speak("Profile photo downloaded successfully")
            except Exception as e:
                myVar.set("Invalid Username")
                speak("Invalid Username")
                root.update()
                link.set("Enter the correct username")
                speak("Enter the correct username")
        #window
        root = Tk()
        root.geometry("400x400")
        root.title("Instagram scraber")
        
        #entry
        myVar = StringVar()
        myVar.set("Enter the Instagram Username below")
        Entry(root, textvariable=myVar, width=40).pack(pady=10)
        link = StringVar()
        Entry(root, textvariable=link, width=40).pack(pady=10)
        #button
        speak("Enter   the    Instagram Username below")
        speak("Then   click ok profile photo button")
        Label(root, text="INSTAGRAM SCRABER", font="calibri 20 bold" ,fg='deeppink').pack()
        Button(root, text="profile photo", command=profilephoto).pack(pady=10)
        Button(root, text="verification", command=accountverfication).pack(pady=10)
        root.mainloop()
        
    if "profile" in c:
        profile()
#7
def dateandtime(c):
    from datetime import datetime
    from num2words import num2words
    from plyer import notification
    import os
    i= str(os.getcwd()+ '\\callls.ico')
    def date():
        now=datetime.now()
        date=now.strftime("%d/%m/%Y")
        a=str(date).replace("/","")
        y=a[4]+a[5]+a[6]+a[7]
        m=a[2]+a[3]
        d=a[0]+a[1]
        notification.notify(title="Date", message=str(date),app_icon = i,timeout = 10)
        speak(num2words(d) + num2words(m) + num2words(y))
    def time():
        now = datetime.now()
        time=now.strftime("%H:%M:%S")
        a=str(time).replace(":","")
        h=a[0]+a[1]
        m=a[2]+a[3]
        notification.notify(title="Time", message=str(time),app_icon = i,timeout = 10)
        speak(num2words(h) + num2words(m))
    def day():
        day=datetime.today().strftime('%A')
        notification.notify(title="Day", message=str(day),app_icon = i,timeout = 10)
        speak(day)
    if "date" in c:
        date()
    if "time" in c:
        time()
    if "day" in c:
        day()
#8
def wifi(c):
    def passwordchecker():
        import pyperclip
        root = Tk()
        root.geometry("400x400")
        pass_details = StringVar()
        def see_wifi_pass():
            import subprocess
            global myList
            myList=[]
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for i in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    myList.append(i)
                    myList.append("--")
                    myList.append(results[0])
                    myList.append("|")
                except IndexError:
                    myList.append(i)
                    myList.append("--")
                    myList.append("")
        def show_wifi_pass():
            pass_details.set(myList)
        def copytoclipboard():
            password = pass_details.get()
            pyperclip.copy(password)
        if 1==1:
            see_wifi_pass()
        Label(root, text="\nWIFI SCRABER\n", font="calibri 30 bold" ,fg='deeppink').pack()
        Entry(root, textvariable=pass_details, width=50).pack(pady=10)
        speak("sir please click on Show wifi pass details button to show all your saved password")
        Button(root, text="Show wifi pass details", command=show_wifi_pass).pack(pady=10)
        Button(root, text="Copy to clipbord", command=copytoclipboard).pack(pady=10)
        root.mainloop()
    def disconnectwifi():
        import os
        from plyer import notification
        i= str(os.getcwd()+ '\\callls.ico')
        os.system("netsh wlan disconnect")
        notification.notify(title="WI-FI", message="Wi-Fi disconnected",app_icon = i,timeout = 10)
        speak("Wi-Fi is disconnected")
    def wifidetail():
        import subprocess
        devices = subprocess.check_output(['netsh','wlan','show','interface'])
        devices = devices.decode('ascii')
        devices= devices.replace("\r","")
        print(devices)
        speak(devices)
    if "disconnect" in c:
        disconnectwifi()
    if "password" in c:
        passwordchecker()
    if "detail" in c or "signal" in c or "about" in c or "strength" in c:
        wifidetail()
#9
def videodownloader(c):
    def youtube():
        from pytube import YouTube
        root = Tk()
        root.geometry("400x350")
        root.title("Youtube video downloader application")
        def download():
            try:
                myVar.set("Downloading...")
                speak(" your video is downloading please wait") 
                root.update()
                YouTube(link.get()).streams.first().download()
                link.set("Video downloaded successfully")
                speak("your video is downloaded successfully")
            except Exception as e:
                myVar.set("Mistake")
                speak("your are entered the invalid link")
                root.update()
                link.set("Enter correct link")
                speak("Enter correct link")
        Label(root, text="YOUTUBE\n VIDEO DOWNLOADER", font="calibri 20 bold" ,fg='deeppink').pack()
        myVar = StringVar()
        myVar.set("Enter the link below")
        Entry(root, textvariable=myVar, width=50).pack(pady=10)
        link = StringVar()
        Entry(root, textvariable=link, width=50).pack(pady=10)
        Button(root, text="Download video", command=download).pack()
        root.mainloop()
    if "youtube" in c:
        youtube()
#10
def restart(c):
    import os
    try:
        from num2words import num2words
        numbers = [int(word) for word in c.split() if word.isdigit()]
        numbertowords=str(num2words(numbers[0]))
        speak("restarting the computer in "+numbertowords+" seconds")
        os.system("shutdown /r /t "+str(numbers[0]))
    except:
        speak("restarting the computer")
        os.system("shutdown /r /t 1")
#11
def search(c):
    import webbrowser
    cs=c.split()
    cs.remove("search")
    j=' '.join(cs)
    webbrowser.open('https://www.google.com/search?q='+j)
    speak("searching "+j)
#12
def joke():
    import pyjokes
    import os
    from plyer import notification
    i= str(os.getcwd()+ '\\callls.ico')
    My_joke = pyjokes.get_joke(language="en", category="neutral")
    notification.notify(title="JOKE", message=str(My_joke),app_icon = i,timeout = 25)
    speak(My_joke)
#13
def data():
    if "name" in c:
        speak("i am call")
    if "owner" in c:
        speak("my owner is Aravind Raj")
    if "creator" in c:
        speak("my creator is Aravind Raj")
    if "founder" in c:
        speak("my founder is Aravind Raj")
    if "subscription" in c:
        speak("limit less subscription ")
    if "lifespan" in c:
        speak("my life is limitless")
    if "birthday" in c:
        speak("since 2020, i am corona batch monster baby")
    if "age" in c:
        speak("No age for me i am always young    and   new")
#14
def close(c):
    def chrome():
        import os
        try:
            os.system("taskkill /im chrome.exe /f")
        except:
            speak("Chrome is not in use")
    def python():
        import os
        try:
            os.system("taskkill /im pythonw.exe /f")
        except:
            speak("Python is not in use")
    def devc():
        import os
        try:
            os.system("taskkill /im devcpp.exe /f")
        except:
            speak("dev c plus plus is not in use")
    def cmd():
        import os
        try:
            os.system("taskkill /im cmd.exe /f")
        except:
            speak("Command prompt is not in use")
    def notepad():
        import os
        try:
            os.system("taskkill /im notepad.exe /f")
        except:
            speak("Notepad is not in use")
    
    if "all" in c:
        speak("closing aLL the application")
        chrome()
        python()
        devc()
        cmd()
        notepad()
        speak("all the application are closed")
    if "chrome" in c:
        speak("closing chrome")
        chrome()
    if "python" in c:
        speak("closing python")
        python()
    if "notepad" in c:
        speak("closing notepad")
        notepad()
    if "cmd" in c or "command prompt" in c.replace(" ","") or "terminal" in c:
        speak("closing command prompt")
        cmd()
    if "closedevc" in c.replace(" ",""):
        speak("closing c programing")
        devc()
#15
def usage(c):
    def cpu():
        import psutil
        from num2words import num2words
        from plyer import notification
        import os
        i= str(os.getcwd()+ '\\callls.ico')
        try:
            numbers = [int(word) for word in c.split() if word.isdigit()]
            numbertowords=str(num2words(numbers[0]))
            a=psutil.cpu_percent(numbers[0])
            notification.notify(title="Usage CPU", message="The usage CPU in "+str(numbers[0])+" second is "+str(a)+"%",app_icon = i,timeout = 10)
            speak("The usage CPU  in "+numbertowords+" second  is  "+numbertoword+" percentage")
        except:
            a=str(psutil.cpu_percent(1))
            numbertoword=str(num2words(a))
            notification.notify(title="Usage CPU", message="The usage of CPU in 1 second is"+str(a),app_icon = i,timeout = 10)
            speak("The usage of CPU in one second   is  "+numbertoword)
    def ram():
        import psutil
        from plyer import notification
        import os
        i= str(os.getcwd()+ '\\callls.ico')
        print('RAM memory % used:', psutil.virtual_memory()[2])
        notification.notify(title="Usage RAM", message="The usage RAM memory using"+str(psutil.virtual_memory()[2])+"%" ,app_icon = i,timeout = 10)
        speak('RAM memory using'+str(psutil.virtual_memory()[2])+'%')
    if "cpu" in c or "computer" in c or "pc" in c:
        cpu()
    if "ram" in c :
        ram()
#16
def boostperformance(c):
    import os
    from plyer import notification
    i= str(os.getcwd()+ '\\callls.ico')
    def tempfiledelete():
        from plyer import notification
        os.system("del /q/f/s %TEMP%\*")
        speak("temporary files deleted ")
    def caches():
        from plyer import notification
        os.system("ipconfig/flushDNS")
        speak("caches cleaned")
    if "boost" in c or "increase" in c:
        tempfiledelete()
        caches()
        notification.notify(title="Performance Increased", message="Temporary Files Deleted Successfully \n Cache Cleaned Successfully",app_icon = i,timeout = 0.2)
        speak("your pc performance is increased")
    if "cache" in c:
        caches()
    if "temp" in c:
        tempfiledelete()
        notification.notify(title="Temporary Files", message="Deleted Successfully",app_icon = i,timeout = 0.2)
#17
#def goto(c):
 #   import webbrowser
  #  cs=c.split()
  #  a=cs.replace(" ","")
   # try:
  #      a.remove("goto")
   # except:
  #      a.remove("gotu")
   # j=' '.join(a)
   # webbrowser.open(j)
#18
def server():
    import http.server
    import socketserver
    import socket
    import pyperclip as pc
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        a="http://"+str(socket.gethostbyname(socket.gethostname()))+":8000/"
        b="Link: "+a
        print(b,"link is copied to click board")
        pc.copy(a)
        speak("http is copied to your click board the that to access the files")
        http.serve_forever()
#19
def selfdis():
    import os
    if os.path.exists("call.exe"):
        os.remove("call.exe")
    else:
        print("unable to self destruction")
#20
def meaning(c):
    import webbrowser
    webbrowser.open('https://www.google.com/search?q='+c)
    speak("searching "+c)
def raspberrypiconnection(c):
    import pyrebase
    config={
        "apiKey": "AIzaSyCMdwsdzWycUH_WVbkG9RRfIEadWazLaIo",
        "authDomain": "homeautomation-ddfdd.firebaseapp.com",
        "databaseURL": "https://homeautomation-ddfdd-default-rtdb.firebaseio.com",
        "projectId": "homeautomation-ddfdd",
        "storageBucket": "homeautomation-ddfdd.appspot.com",
        "messagingSenderId": "587715575052",
        "appId": "1:587715575052:web:6e2d075cb4e846bd21dd29",
        "measurementId": "G-YYKQMGCPCG"
        }
    firebase= pyrebase.initialize_app(config)
    database=firebase.database()
    users=database.child("pi message").set(str(c))
def take_c():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        speak('Listening'),print('listening')
        r.pause_threshold = 0.7
        audio = r.listen(s)
        try:
            speak("Recognizing"),print("Recognizing")
            Query = r.recognize_google(audio)
        except Exception as e:
            print(e)
            print(" Say Again sir"),speak("sir i cannot hear you sir Say Again sir")
            return ""
        return Query
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
if __name__ == '__main__':
    while True:
        c=take_c()
        print(c)
        c=c.lower()
        if "stop" in c.replace(" ",""):
            speak("ok sir")
            break
        if "close" in c:
            close(c)
        if "off" in c and "computer" in c:
            shutdown(c)
            break
        if "light" in c:
            if "on" in c:
                raspberrypiconnection("switch1 on")
                speak("turning on light")
            else:
                raspberrypiconnection("switch1 off")
                speak("turning off light")
        if "fan" in c:
            if "on" in c:
                raspberrypiconnection("switch2 on")
                speak("turning on fan")
            else:
                raspberrypiconnection("switch2 off")
                speak("turning off fan")
        if "everything" in c and "turn":
            if "on" in c:
                raspberrypiconnection("everything on")
                speak("turning on everything")
            else:
                raspberrypiconnection("everything off")
                speak("turning off everything")
        if "battery" in c.replace(" ",""):
            battery()
        if "open" in c.replace(" ",""):
            opens(c)
        if "shutdown" in c.replace(" ",""):
            shutdown(c)
            break
        if "restart" in c.replace(" ",""):
            restart(c)
            break
        if "search" in c:
            search(c)
        if "insta" in c.replace(" ",""):
            instagram(c)
        if "goto" in c or "gotu" in c:
            goto(c)
        if "usage" in c:
            usage(c)
        if "date" or "time " or "day" in c:
            dateandtime(c)
        if "boost" in c or "performance" in c or "delete" in c:
            boostperformance(c)
        if "wi-fi" in c:
            wifi(c)
        if "download" in c:
            videodownloader(c)
        if "configuration" in c:
            deviceconfig()
        if "ip" in c:
            ipaddress()
        if "your" in c or "you" in c:
            data()
        if "server" in c:
            server()
        if "mean" in c or "meaning" in c :
            meaning(c)
        if "joke" in c:
            joke()
        if "program" in c and "close" in c:
            speak("ok sir")
            break
        if "shutup" in c.replace(" ",""):
            speak("ok")
            break
