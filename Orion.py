import pyttsx3
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
import keyboard as k
import info
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice",voices[1].id)
#Chrome Path
chrome_path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}")
        

    except Exception as e:
        print("Please, say that again")
        return "None"
    return query

def getTime():
    current_time=time.localtime()
    hour=current_time.tm_hour
    minute=current_time.tm_min
    sec=current_time.tm_sec
    return [hour,minute,sec]

def speakTime():
    mytime=getTime()
    c_time=f"The time is, {mytime[0]} hours, {mytime[1]} minutes"
    speak(c_time)

def greet():
    mytime=getTime()
    time=""
    if (mytime[0]>=4 and mytime[1]>=30) and (mytime[0]<12) :
        time="morning"
    elif mytime[0]>=12 and mytime[0]<17:
        time="Afternoon"
    elif mytime[0]>=17 and mytime[0]<20:
        time="evening"
    else:
        time="night"
        speak(f"Good {time} Sir, I'm Orion, How may I help you")


if __name__=="__main__":
    # greet()
    while True:
        userSaid=takecommand().lower()
        if userSaid=="hello" :
                greet()
            
        elif "what is the time" in userSaid or "what's the time" in userSaid:
            speakTime()
            
        elif 'wikipedia' in userSaid:
            speak("searching wikipedia")
            userSaid=userSaid.replace("wikipedia","")
            userSaid=userSaid.replace("orion","")
            print(userSaid)
            result=wikipedia.summary(userSaid,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            
        elif "pause" in userSaid or "stop" in userSaid:
            speak("Thank you for letting me assist you")
            break
            
        elif "open youtube" in userSaid:
            webbrowser.get(chrome_path).open("youtube.com")
            
        elif "youtube search" in userSaid:
            userSaid=userSaid.replace("youtube search","")
            webbrowser.get(chrome_path).open(f"https://www.youtube.com/results?search_query={userSaid}")

        elif "open google" in userSaid:
            webbrowser.get(chrome_path).open("google.com")

        elif "search" in userSaid:
            userSaid=userSaid.replace("search","")
            webbrowser.get(chrome_path).open(f"https://www.google.com/search?q={userSaid}")
        elif "open code" in userSaid:
            codepath="C://Users//DELL//Desktop//Visual Studio Code.lnk"
            os.startfile(codepath)
        elif "open whatsapp" in userSaid:
            path="C://Users//DELL//Desktop//WhatsApp.lnk"
            os.startfile(path)

        elif "open calendar" in userSaid:
            path="C://Users//DELL//Desktop//Google Calendar.lnk"
            os.startfile(path)
        elif "message me" in userSaid:
            userSaid=userSaid.replace("message me","")
            pywhatkit.sendwhatmsg_instantly(info.me(),userSaid,17,True)
            pyautogui.click(1050, 950)
            time.sleep(15)
            k.press_and_release('enter')
        elif "message sister" in userSaid:
            userSaid=userSaid.replace("message sister","")
            pywhatkit.sendwhatmsg_instantly(info.sister(),userSaid,17,True)
            # pyautogui.click(1050, 950)
            # time.sleep(15)
            # k.press_and_release('enter')
        elif "message mother" in userSaid:
            userSaid=userSaid.replace("message mother","")
            pywhatkit.sendwhatmsg_instantly(info.mother(),userSaid,17,True)
            # pyautogui.click(1050, 950)
            # time.sleep(15)
            # k.press_and_release('enter')
        elif "message girlfriend" in userSaid:
            userSaid=userSaid.replace("message girlfriend","")
            pywhatkit.sendwhatmsg_instantly(info.girlfriend(),userSaid,20,True)
            # pyautogui.click(1050, 950)
            # time.sleep(15)
            # k.press_and_release('enter')