import pyttsx3 as ptt             # This module is use for convert text-to-speech 
import datetime                   # This module is use for import date and time   
import speech_recognition as sr   # This module is use for convert spoken word into text 
import wikipedia                  # This module is use for searching and retrieving information from Wikipedia.
import webbrowser                 # This module is use for automating web browsing tasks in Python
import os                         # This module is use for for interacting with the operating system
from PIL import Image, ImageGrab  # This module is use for taking screen shot
import pyautogui         # This module is use for automate keybord and mouse with python programm
import time
import multiprocessing
from DAGUI import guiStart
from pynput.keyboard import Key,Controller
#===================================================================================================================================

engine = ptt.init('sapi5')  # Make instence of pyttsx3 module 
voices = engine.getProperty('voices')   # Get voice from system 
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)   # Set voice 

keyboard = Controller()
#===================================================================================================================================
# This function speak given audio string 
def speak(audio):
    engine.say(audio)   # use for speak given string
    engine.runAndWait() # Run and wait for outpout

#===================================================================================================================================
# It's wish base on time 
def wishMe(VAName):
    hour = int(datetime.datetime.now().hour)    # Get current hour from date and time moudle
    if hour >= 0 and hour < 12:
        print(f"{VAName} : Good Morning Sir")
        speak("good Morning sir")
    elif hour >= 12 and hour <18:
        print(f"{VAName} : Good Afternoon Sir")
        speak("good Afternoon sir")
    elif hour >= 18 and hour <= 24:
        print(f"{VAName} : Good Evening Sir")
        speak("Good evening sir")
    print(f"{VAName} : How can i help you?")
    speak(f"I am {VAName}, How can i help you?")

#===================================================================================================================================
# It's take microphone input from the user and return output
def takeCommand():
    
    r = sr.Recognizer() # Create instence of speech_recognintion 

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source,timeout=20,phrase_time_limit=20)    # for convert voice to text
        
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio)   
        print(f"User said : {query}\n")
    
    except Exception as e :
        print(e)
        print("Say that again please.")
        print("Somthing want's wrong.")
        speak("Please say that again.")
        return "None"
    
    engine.runAndWait()
    return query 

#===================================================================================================================================
def Recogniting(query, VAName):

    media_control = ['increase volume', 'decrease volume', 'play', 'paush', 'mute', 'play next', 'play previous']
    if 'google' in query:
        from webTask import searchGoogle
        searchGoogle(query)

    elif 'youtube' in query:
        from  webTask import searchYoutube
        searchYoutube(query)

    elif 'wikipedia' in query:
        from webTask import searchWikipedia
        searchWikipedia(query)
    
    elif "open brave" in query:
        print(f"{VAName} : Opening brave")
        speak("Opening brave")
        webbrowser.open('http://www.brave.com') 
        
           
    elif 'open incognito tab' in query:
        print(f"{VAName} : opening incognito tab " )
        speak(f"opening incognito tab")
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('chrome')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('tab') 
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl','shift','n')  

    elif  'whatsapp' in query:
        from DesktopTask import whatsappTask
        whatsappTask(query)


    elif 'open' in query:
        from DesktopTask import openApp
        openApp(query)
        

    elif 'close tab' in query:
        print(f"{VAName} : closing tab")
        speak("closing tab")
        pyautogui.hotkey('ctrl','w') 

    
    elif 'close' in query:
        from DesktopTask import closeApp
        closeApp(query)
    
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{VAName} : the time is {strTime}")
        speak(f"the time is {strTime}")

    elif 'increase volume' in query:
        for i in range(2):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            time.sleep(0.1)
    
    elif 'decrease volume' in query:
        for i in range(2):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            time.sleep(0.1)

    elif query in media_control:
        from keyboardTask import mediaControl
        mediaControl(query)

    elif 'change tab' in query:
        print(f"{VAName} : changing tab")
        speak("changing tab")
        pyautogui.hotkey('alt','tab')

    elif "take a screen shot" in query:
        print(f"{VAName} : Taking screen shot")
        speak("Taking screenshot")
        image  = ImageGrab.grab()
        image.show()

    elif 'lock pc' in query:
        print(f"{VAName} : pc locked ")
        speak("pc locked ")
        pyautogui.hotkey('win','l')  
    

    elif "shutdown this pc" in query:
        from DesktopTask import shutdownPC
        shutdownPC(query)

    elif "restart this pc" in query:
        print(f'{VAName} : Restarting')
        speak('Restarting')
        os.system('shutdown /r') 

    elif 'select all' in query:
        print(f'{VAName} : selecting all')
        speak('Selecting all')
        pyautogui.hotkey('ctrl','a')
        
    elif 'copy all' in query:
        print(f'{VAName} : Coping all')
        speak('Coping all')
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.sleep(0.5)
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')

    elif 'remove all file' in query:
        print(f'{VAName} : Removing all file')
        speak('Removing all file')
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('delete')

    elif 'remove all' in query:
        print(f'{VAName} : Removing all')
        speak('Removing all')
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.press('backspace')
        pyautogui.keyUp('ctrl')

    else:
        from NormalConversation import Conversetion
        Conversetion(query)
        
#===================================================================================================================================
        
def inputQuery(self):
    while True:
        query = takeCommand().lower()
        Recogniting(query, VAName)
#===================================================================================================================================
# def stopProcess(query):
#     if query=='stop':

#      p2.close()        



#===================================================================================================================================
    
# ------------------------------ Main part ---------------------------
VAName = "ALEX".lower()
if __name__ == '__main__':
    
    p1 = multiprocessing.Process(target=guiStart,args=(10,))
    p2 = multiprocessing.Process(target=inputQuery,args=(10,))
    # p3 = multiprocessing.Process(target=stopProcess,args=(10,))
    p1.start()
    time.sleep(1)
    wishMe(VAName)

    p2.start()
    # p3.start()
    p1.join()
    p2.join()
    # p3.join()
    
   
