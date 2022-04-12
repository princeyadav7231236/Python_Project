import requests
import datetime
import os
import random
import pywhatkit
import smtplib
import webbrowser
from ecapture import ecapture
import wolframalpha
import pyttsx3
import requests as request
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty('voice', voices[3].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Boss")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boss")
    elif 18 <= hour < 21:
        speak("Good Evening Boss")
    else:
        speak("Good Night Boss")

    speak("This is Lily  Please tell me how may I help you ")


def browser():
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))


def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query_of_the_user = r.recognize_google(audio, language='en-in')
        print(f"User said : {query_of_the_user}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query_of_the_user


def sendEmail(to, content):
    """This will send the Email to the input user """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("Your  Email", "your password")
    server.sendmail(""
                    "Receivers Gmail", to, content)


if __name__ == '__main__':
    # speak("Hello boss how are you ")
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if "wikipedia" in query:
            try:
                speak("what do you want to  search ? ")
                search = takeCommand()
                speak("Searching Wikipedia ")
                results = wikipedia.summary(search, sentences=100)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except:
                speak("Sorry for that Boss, I haven't heard what you have said. Will you please repeat your Command.")

        elif "open youtube" in query:
            browser()
            speak("Opening youtube")
            webbrowser.get('chrome').open("youtube.com")

        elif "open google" in query:
            browser()
            speak("Opening Google")
            webbrowser.get('chrome').open("google.com")

        elif "open stack overflow" in query:
            browser()
            speak("Opening Stackoverflow")
            webbrowser.get('chrome').open("stackoverflow.com")

        elif "open github" in query:
            browser()
            speak("Opening Github")
            webbrowser.get('chrome').open("github.com")
            # path = "C:\\Users\\Bansh\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            # os.startfile(path)

        elif "play music" in query:
            music_dir = "G:\\music"
            songs = os.listdir(music_dir)
            # print(songs)
            speak("Playing music  Boss")
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        elif "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss the time is {str_time}")

        elif "send email" in query:
            try:
                speak("What should i say")
                message = takeCommand()
                to_whom_you_want_to_send_the_email = "Recievers Gmail"
                sendEmail(to_whom_you_want_to_send_the_email, message)
                speak("Email has been send !")
            except Exception as e:
                print(e)
                speak("Sorry Boss, I am not able to send this email. ")

        elif "news" in query:
            speak("The latest news are as follows")
            json_of_news = request.get(
                "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=95a2058faa4e49ddb1391a8fcc2de3eb")
            dict_of_news = json_of_news.json()
            i = 0
            while i < len(dict_of_news["articles"]):
                for a in range(len(dict_of_news["articles"])):
                    print(i + 1, ".)  ", dict_of_news["articles"][i]["title"])
                    speak(dict_of_news["articles"][i]["title"])
                    i += 1
                    if i > len(dict_of_news["articles"]):
                        break

        elif "take photo" in query or "click a image " in query or "open camera" in query:
            try:
                speak("Going to click your photo boss. ")
                ecapture.capture(0, "DESKTOP-MKSSB8T", "IMAGE.jpg")
            except Exception as e:
                print(e)
                speak("Sorry boss I am unable to click your photo .")

        elif "search" in query:
            try:
                query = query.replace("search", "")
                speak("What do you want to search")
                print("Speak your text which you want to search. ")
                search = takeCommand()
                new_search = "https://www.google.com/search?q=" + search
                speak(f"Searching for {search}")
                webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(
                    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get("chrome").open(new_search)
            except:
                speak("Sorry for that Boss, I haven't heard what you have said. Will you please repeat your Command.")
        elif "ask" in query:
            try:
                speak(
                    "I can answer to computational and geographical questions  and what question do you want to ask now")
                question = takeCommand()
                app_id = "6KGV8K-UXAW2G3QUL"
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                print(answer)
                speak(answer)
            except:
                print("Sorry for that Boss, I haven't heard what you have said. Will you please repeat your Command.")
                speak("Sorry for that Boss, I haven't heard what you have said. Will you please repeat your Command.")

        elif "weather" in query:
            try:
                API_key = "35a17cd0632e0df4b61eab70a07ef41c"
                base_url = f"http://api.openweathermap.org/data/2.5/weather?"
                speak("What is the City name")

                City_name = takeCommand()
                complete_url = base_url + "appid=" + API_key + "&q=" + City_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print("Temperature in Degree Celsius unit is " + str(
                        float(current_temperature - 273.15)) + "\n Humidity in percentage is " + str(
                        current_humidity) + "\n Description " + str(weather_description))
                    speak(
                        "Temperature in Degree Celsius unit is " + str(
                            float(current_temperature - 273.15)) + "\n Humidity in percentage is " + str(
                            current_humidity) + "\n Description " + str(weather_description))
            except Exception as e:
                print(e)
                speak("Sorry Boss, I can't Recognize it, can you please repeat the command again.")

        elif "log off " in query or "sign out " in query or "shut down" in query:
            speak("Do you want to turn off your computer say : yes / no ?")
            command = takeCommand()
            if "no" in command:
                speak("You said no so, I am not shutting your computer.")
            elif "yes" in command:
                speak("You said yes boss so, I am shutting your computer. ")
                os.system("shutdown /s /t 1")
            else:
                speak("you said something else, so I am not running your command shutdown ")

        elif "who made you  " in query or "who created you " in query or "who invented you " in query:
            speak(
                "I am Lily and I was invented by BOSS Diwakar, and I am here to help him to improve his Programming skills. ")

        elif "what can you do " in query or "what are the tasks which you can perform " in query:
            speak(
                "I am designed to do some mini tasks like opening Google, YouTube, GitHub, StackOverFlow, and I programmed in such a way that I can "
                "help you in Computational and Geographical problems, and I can also tell the time and Weather of different cities, and I can Provide you with the "
                "latest News, and search anything on Google or Wikipedia, there are many more functionalities which are going to be updated with time in me.")

        elif "what is your name " in query:
            speak("This is Lily the Desktop Assistant of BOSS Diwakar")

        elif "exit" in query:
            speak("Exiting Assistant Boss")
            exit()
