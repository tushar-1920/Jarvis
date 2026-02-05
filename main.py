import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "", 1).strip()       # take everything after “play”
        link = musicLibrary.music.get(song)                   # safe dictionary lookup
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in library.")
    


if __name__ == "__main__":
    speak("initializing Jarvis.... ")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word = r.recognize_google(audio)
            print(f"You said: {word}")

            if word.lower() == "jarvis":
                speak("ya")
                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                command = r.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except Exception as e:
            print(f"Error: {e}")















