import pyttsx3
soz = input("matn kiriting: ")
engine = pyttsx3.init()

engine.save_to_file(soz,"txt.mp3")
engine.runAndWait()

