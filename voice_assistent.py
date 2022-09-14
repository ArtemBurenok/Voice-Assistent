from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import nltk
from datetime import datetime
from VoiceAssistent.simple_progect.volume.sound import Sound
from newsapi import NewsApiClient
import webbrowser
import os

nltk.download('omw-1.4')


class Speech:
    def __init__(self, recognizer):
        self.recognizer = recognizer

        self.speaker = tts.init()
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('rate', 150)
        self.speaker.setProperty('voice', voices[1].id)

        self.months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']

    def time_now(self):
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        self.speaker.say(str(hour) + " hours " + str(minute) + ' minutes')
        self.speaker.runAndWait()

    def date_now(self):
        current_time = datetime.now()
        day = current_time.day
        month = self.months[current_time.month - 1]
        self.speaker.say(str(day) + ' ' + month)
        self.speaker.runAndWait()

    def change_volume(self):
        self.speaker.say("What volume to set?")
        self.speaker.runAndWait()

        done = False

        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    try:
                        vol = self.recognizer.recognize_google(audio)
                        vol = int(vol)

                        Sound.volume_set(vol)
                    except ValueError:
                        self.recognizer = speech_recognition.Recognizer()
                        self.speaker.say("I don't understand! Please, say a number!.")
                        self.speaker.runAndWait()
                    done = True

            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                self.speaker.say("I don't understand! Please, try again.")
                self.speaker.runAndWait()

    def search_internet(self):
        self.speaker.say("What do you want to search?")
        self.speaker.runAndWait()

        done = False

        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    search = self.recognizer.recognize_google(audio)
                    url = 'http://google.com/search?q=' + search
                    webbrowser.get().open(url)

                    done = True
            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                self.speaker.say("I don't understand! Please, try again.")
                self.speaker.runAndWait()

    def find_location(self):
        self.speaker.say("What location you want find?")
        self.speaker.runAndWait()

        done = False

        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    location = self.recognizer.recognize_google(audio)
                    url = 'http://google.com/maps?q=' + location
                    webbrowser.get().open(url)

                    done = True
            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                self.speaker.say("I don't understand! Please, try again.")
                self.speaker.runAndWait()

    def youtube(self):
        self.speaker.say("What video you want to watch?")
        self.speaker.runAndWait()

        done = False

        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    location = self.recognizer.recognize_google(audio)
                    url = 'https://www.youtube.com/results?search_query=' + location
                    webbrowser.get().open(url)

                    done = True
            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                self.speaker.say("I don't understand! Please, try again.")
                self.speaker.runAndWait()

    def news(self):
        newsapi = NewsApiClient(api_key='1e375df6058d4617b40e8e6335397af9')

        self.speaker.say("What the title of news?")
        self.speaker.runAndWait()
        done = False

        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    title = self.recognizer.recognize_google(audio)
                    top_headlines = newsapi.get_everything(q=title)
                    articles = top_headlines['articles']

                    for x, y in enumerate(articles):
                        # speaker.say(f"{str(x)} {y['title']}")
                        if x < 5:
                            print(f"{str(x + 1)} {y['title']}")
                            self.speaker.say(f"{str(x + 1)} {y['title']}")
                        else:
                            break

                    done = True
            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                self.speaker.say("I don't understand! Please, try again.")
                self.speaker.runAndWait()

    def open_apps(self):
        self.speaker.say("What app to open?")
        self.speaker.runAndWait()
        done = False

        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    app = self.recognizer.recognize_google(audio)

                    if app == "telegram":
                        os.system('C:/Users/Пользователь/AppData/Roaming/Telegram Desktop/Telegram.exe')
                        done = True
                    elif app == "zona":
                        os.system('C:/"Program Files (x86)"/Zona/Zona.exe')
                        done = True
                    elif app == 'zoom':
                        os.system('C:/Users/Пользователь/AppData/Roaming/Zoom/bin/Zoom.exe')
                        done = True
                    else:
                        self.speaker.say("I don't open the app. Please, check your computer by this app.")
                        self.speaker.runAndWait()

            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                self.speaker.say("I don't understand! Please, try again.")
                self.speaker.runAndWait()

    def greeting(self):
        self.speaker.say("Hello, what can I help you?")
        self.speaker.runAndWait()

    def name_bot(self):
        self.speaker.say("My name is Eva.")
        self.speaker.runAndWait()

    def name_owner(self):
        self.speaker.say("Artem is my owner")
        self.speaker.runAndWait()

    def quit(self):
        self.speaker.say("Goodbye")
        self.speaker.runAndWait()
        sys.exit(0)


def main():
    recognizer = speech_recognition.Recognizer()

    speech_system = Speech(recognizer)

    mapping = {
        'greeting': speech_system.greeting,
        'name_bot': speech_system.name_bot,
        'name_creator': speech_system.name_owner,
        'time': speech_system.time_now,
        'date': speech_system.date_now,
        'change_volume': speech_system.change_volume,
        'search_internet': speech_system.search_internet,
        'find_location': speech_system.find_location,
        'youtube': speech_system.youtube,
        'news': speech_system.news,
        'exit': speech_system.quit
    }

    assistant = GenericAssistant('intents.json', intent_methods=mapping)
    assistant.train_model()

    print("speech recording:")

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio)
                message = message.lower()

            assistant.request(message)
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()


if __name__ == '__main__':
    main()

