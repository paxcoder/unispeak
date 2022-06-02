import win32com.client
sapi=win32com.client.Dispatch("SAPI.SpVoice")
def speak(text):
    sapi.speak(text)