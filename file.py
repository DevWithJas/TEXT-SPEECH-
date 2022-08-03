import pyttsx3 

engine = pyttsx3.init()

for voice in engine.getProperty("voices"):
    print(voice)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

text = input("enter your text now:")

speak(text)