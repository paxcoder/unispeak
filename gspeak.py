import sys
def speak(text):
    if sys.platform=="darwin":
        import mactalk
        speak=mactalk.speak
    if sys.platform=="windows":
     import nvda_speak
     running=int(nvda_gspeak.nvda_is_running())
     if running=="0":
      speak=gspeak_nvda.speak
     else:
        import gsapi
        speak=gsapi.speak