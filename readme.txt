This is a set of modules, allowing for text to speech, and screenreader support
Import mactalk
mactalk.speak("hello, world")
The same with NVDA and sapi but NVDA can do following
Import gspeak_nvda as nvda
if nvda.running >0
##use sapi
Else
##use NVDA.