import gsapi
import gspeak
f=int(gspeak.nvda_is_running())
if f >>0:
    gsapi.speak("you don't have NVDA enabled, so I will use sapi instead.")
else:
     gspeak.speak("you have NVDA started, so I can use it.")