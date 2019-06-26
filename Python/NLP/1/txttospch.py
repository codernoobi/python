#text to speech
import win32com.client					#pip install pywin32
def text2speech(text):
	service=win32com.client.Dispatch("SAPI.SpVoice")
	service.Speak(text)

text2speech(input("Enter text:\n"))

"""
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("I can rell a story")
"""