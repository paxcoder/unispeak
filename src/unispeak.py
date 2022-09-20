import sys
if sys.platform=="darwin":
    import mactalk
    speak=mactalk.speak
if sys.platform=="windows":
     import nvda_speak
     running=int(nvda_gspeak.nvda_is_running())
     if running=="0":
      speak=unispeak_nvda.speak
     else:
        import unisapi
        speak=unisapi.speak   