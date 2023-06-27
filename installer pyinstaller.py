import os
os.system("PyInstaller --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5  --icon=callls.ico callai.py")
print("sucessfully")
