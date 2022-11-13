
#The packeges that we import for using speechRecognition
import speech_recognition
import pyttsx3
import webbrowser


#Method for changing the test to voice
def SpeakNow(command):
    voice=pyttsx3.init()
    voice.say(command)
    voice.runAndWait()

#methode for welcome
def sayWelcome():
    welcome='Welcome to the code written by Khalid Mubaraze. Can you say something?'
    SpeakNow(welcome)

# call the welcome method
sayWelcome()


path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s"
sr= speech_recognition.Recognizer()


with speech_recognition.Microphone() as source2:
    print('silent please...')
    sr.adjust_for_ambient_noise(source2,duration=2)
    print('Speack now please.....')
    audio2=sr.listen(source2)

    try:
        # for persian language we write (,language='fa-IR') after audio2 in recognize_google
        textt=sr.recognize_google(audio2)
        print('you said:  '+textt.lower())
        SpeakNow(textt)

        if 'search' in textt:
            webbrowser.open(textt)

        else:
           print("not thing for search online")


    except Exception as e:
        print('error :  '+str(e))






