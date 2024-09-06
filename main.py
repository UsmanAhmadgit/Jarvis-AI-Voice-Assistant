import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import music_library

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def process_command(c):
    if "open google" in c.lower():
        wb.open("https://google.com")
    elif "open youtube" in c.lower():
        wb.open("https://youtube.com")
    elif "open claude" in c.lower():
        wb.open("https://claude.ai/new")
    elif "open chatgpt" in c.lower():
        wb.open("https://chatgpt.com/")
    elif "open portal" in c.lower():
        wb.open("https://cuonline.cuilahore.edu.pk:8091/")
    elif "open microsoft" in c.lower():
        wb.open("https://www.office.com/?auth=2")
    elif "cricket" in c.lower():
        wb.open("https://www.espncricinfo.com/live-cricket-score")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        wb.open(link)

def speak(text):
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    print("Initializing Jarvis...")
    speak("Initializing Jarvis...")
    #   Listen for the wake word "Jarvis"
    while True:
        r = sr.Recognizer()
        # recognize speech using Google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "hello" or "jarvis"):
                speak("Yes")
                #   Listen for command
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    #   Process command
                    process_command(command)
        except Exception as e:
            print("No Command {0}".format(e))