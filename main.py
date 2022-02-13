import config
#Speech recognition
import speech_recognition as sr
#Speech output
import pyttsx3
#translation engine
import deepl




speaker = pyttsx3.init()

#a = sr.Recognizer()
#with sr.Microphone() as source:
#    print("Say it.")
#    audio = a.listen(source)
#    data = a.recognize_google(audio, language='de-DE')
#    print(data)
def voiceFinder(lang):
    voices = speaker.getProperty('voices')
    print("Looking for voices with language " + lang)
    for v in voices:
        if lang in v.languages or lang == "":
            print(v.id)
           


def main():
    print("Welcome " + config.lang_source)
    voiceFinder("")
    speaker.setProperty('voice', config.voice_output)
    print("Current Rate: " + str(speaker.getProperty('rate')))
    speaker.setProperty("rate", config.speech_rate)
    speaker.setProperty("volume", config.speech_volume)

    speaker.say("witaj! jak się masz?") #maybe you need espeak
    speaker.runAndWait()

main()