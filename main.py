import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import time
import pyjokes



   

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(random.choice( ['Good Morning!', 'Bonjur!.It means good morning in french', 'Suprabhat!'] ))

    elif hour>=12 and hour<18:
        speak(random.choice( ['Good Afternoon!', 'Bonne après-midi!.It means good afternoon in french','Namaskar!' ] ))   

    else:
        speak(random.choice( ['Good Evening!', 'Bonsoir!. It means good evening in french','Namaskar!' ] ))  

    speak("How may I help you")       

def takeCommand():
        #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            # print(e)    
        print("sorry, can you say that again please...")
        speak("Sorry, can you say that again please")
        return "None"
    return query

#this files are of sending mail if you want to access this feature contact me

# myfile = open("E:\\OneDrive\\Desktop\\maxmainfiles\\passwsderede.txt",'rt')
# data_1 = myfile.read()
# myfile.close()

# myfile_1 = open("E:\\OneDrive\\Desktop\\maxmainfiles\\mail.txt",'rt')
# data_2 = myfile_1.read()
# myfile_1.close()


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login(data_2, data_1)
#     server.sendmail(data_2, to, content)
#     server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

            # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            # write here your own file location where this app is located
            # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://youtube.com")
            speak("Opening youtube ")
                
        elif 'open google' in query:
            # write here your own file location where this app is located
            # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://google.com")
            speak("Opening google ")
                
        elif 'open github' in query:
            # write here your own file location where this app is located
            speak("Opening Github ")
            # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://github.com/")   


        elif 'play music' in query:
            # write here your own file location where this app is located
            # codePat = "C:\\Users\\ABC\\AppData\\Roaming\\Spotify\\Spotify.exe"
            speak("Opening spotify ")
            os.startfile(codePat)

        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            # write here your own file location where this app is located
            # codePath = "C:\\Microsoft VS Code\\Code.exe"
            speak("Opening code plese wait")
            os.startfile(codePath)

        # elif 'email to person' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "person mail id"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry sir. I am not able to send this email .please try again")

        elif 'open game studio' in query:
            # write here your own file location where this app is located
            # codepa = "E:\\OneDrive\\Desktop\\godot.exe"
            speak("Opening godot as your game studio ")
            os.startfile(codepa)

        elif 'open blender' in query:
            speak('opening blender 3D software')
            # write here your own file location where this app is located
            # blender = "C:\\Program Files\\Blender Foundation\\Blender 2.83\\blender.exe"
            os.startfile(blender)

        elif 'thank you'  in query:
            speak('welcome!.Glad you like it')

        elif 'well done'  in query:
            speak('Thank you!.Glad you like it')

        elif 'who made you' in query:
            speak('Well my maker is my boss . who is shreyas')

        elif 'search' in query:
            speak('what do want to search for')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            speak('here is what I found about' + search)
            # write here your own file location where this app is located
            # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
        elif 'go offline' in query:
            speak("Ok bye see you soon")
            exit()

        elif 'what is your name' in query:
            speak("My name is max")

        elif 'what you can do' in query:
            print('''I can assists you in different types of work like
            I can search  anything for you on google.   
            I can open your default game studio godot.
            I can open youtube.
            I can tell you the time.
            I can search content on wikipedia for you.
            I can mail to your family member.
            I can open blender 3D software for you.
            I can open Microsoft visual studio code from were i got birth.
            and more things will be adaded in future. ''')
            speak('''I can assists you in different types of work like
            I can search  anything for you on google.   
            I can open your default game studio godot.
            I can open youtube.
            I can tell you the time.
            I can search content on wikipedia for you.
            I can mail to your family member.
            I can open blender 3D software for you.
            I can open Microsoft visual studio code from were i got birth.
            and more things will be added in future. ''')
            
        elif 'i am bored' in query:
            print('''ok I have 2 ways to get rid of your bordem
                i can open steam for gaming
                i can also google online games for you''')
            speak('''ok! .I have 2 ways to get rid of your bordem
                i can open steam for gaming
                i can also google online games for you''')
        elif 'find the place' in query:
            speak('which place you want to search')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            # write here your own file location where this app is located
            # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
        elif 'i want to play games on steam' in query:
            speak('opening steam')
            # write here your own file location where this app is located
            # steam = "E:\\New folder\\steam.exe"
            os.startfile(steam)
        elif 'i want to play online games on google' in query:
            print('''i have many online games  like
                    slither .io
                    google Solitaire
                    and more will be added soon
                    which one you want to play''')
            speak('''i have many online games  like
                    slither .io
                    google Solitaire
                    and more will be added soon
                    which one you want to play''')
            
        elif 'i want to play snake game' in query:
            speak('opening slither game')
            # write here your own file location where this app is located
            # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://slither.io/")
        elif "joke" in query:
            joke=pyjokes.get_joke(language='en', category= 'all')
            print(joke)
            speak(joke)            #has to be made more funny

        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop me from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 

