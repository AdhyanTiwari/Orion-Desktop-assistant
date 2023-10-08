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
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice", voices[1].id)
# Chrome Path
chrome_path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"

# Contact List
contact = [["me", info.me()], ["mother", info.mother()], ["sister", info.sister()], ["girlfriend", info.girlfriend()],["father",info.father()]]

# Sites list
site = [["google", "google.com"], ["youtube","youtube.com"], ["whatsapp", "web.whatsapp.com"],["github","github.com"]]

#Device shortcuts and applications
shortcuts=[["code","C://Users//DELL//Desktop//Visual Studio Code.lnk"],["whatsapp","C://Users//DELL//Desktop//WhatsApp.lnk"],["calendar","C://Users//DELL//Desktop//Google Calendar.lnk"]]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}")

    except Exception as e:
        speak("Please, say that again")
        return "None"
    return query

def getTime():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    sec = current_time.tm_sec
    return [hour, minute, sec]

def speakTime():
    mytime = getTime()
    c_time = f"The time is, {mytime[0]} hours, {mytime[1]} minutes"
    speak(c_time)

def greet():
    mytime = getTime()
    time = ""
    if (mytime[0] >= 4 and mytime[1] >= 30) and (mytime[0] < 12):
        time = "morning"
    elif mytime[0] >= 12 and mytime[0] < 17:
        time = "Afternoon"
    elif mytime[0] >= 17 and mytime[0] < 20:
        time = "evening"
    else:
        time = "night"
    speak(f"Good {time} Sir, I'm Orion, How may I help you")


if __name__ == "__main__":
    speak("Hello, I'm orion, how can i help you")
    while True:
        userSaid = takecommand().lower()
        if userSaid == "hello":
            greet()

        elif "what is the time" in userSaid or "what's the time" in userSaid:
            speakTime()

        elif 'wikipedia' in userSaid:
            speak("searching wikipedia")
            userSaid = userSaid.replace("wikipedia", "")
            userSaid = userSaid.replace("orion", "")
            print(userSaid)
            result = wikipedia.summary(userSaid, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open" in userSaid:
            for i in site:
                if f"open {i[0]}" in userSaid:
                    speak(f"opening {i[0]}")
                    webbrowser.get(chrome_path).open(i[1])
                    break
        
        elif "youtube search" in userSaid:
            userSaid = userSaid.replace("youtube search", "")
            speak("searching on youtube")
            webbrowser.get(chrome_path).open(
                f"https://www.youtube.com/results?search_query={userSaid}")

        elif "search" in userSaid:
            userSaid = userSaid.replace("search", "")
            speak("searching on google")
            webbrowser.get(chrome_path).open(
                f"https://www.google.com/search?q={userSaid}")

        elif "start" in userSaid:
            for i in shortcuts:
                if f"start {i[0]}" in userSaid:
                    speak(f"starting {i[0]}")
                    path = i[1]
                    os.startfile(path)
                    break
                
        elif "message" in userSaid:
            for i in contact:
                if f"message {i[0]}" in userSaid:
                    speak("please tell your message")
                    userSaid = takecommand()
                    pywhatkit.sendwhatmsg_instantly(i[1], userSaid, 30, True)
                    # pyautogui.click(1050, 950)
                    # time.sleep(15)
                    # k.press_and_release('enter')
                    speak("message sent")

        elif "pause" in userSaid or "stop" in userSaid:
            speak("Thank you for letting me assist you")
            break