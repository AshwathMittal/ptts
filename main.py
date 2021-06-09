from gtts import gTTS
import os

o = open("speech.txt", "r")
text = o.read().replace("\n", " ")

language = "en"
output = gTTS(text=text, lang=language, slow = False)
text.save("conv.mp3")
os.system("start conv.mp3")