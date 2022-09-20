there is just one function, which works as follows
speak("text")
it is going to check on what platform it is running, a.k.a. darwin for macOS and windows, for windows.
Then, if macOS will be detected, a thirt party module, called pyttsx3 will be required.
it will then send that text to this module and speak it aloud.
in windows's case, it first checks if NVDA is running, if yes, use that, if not, sapi will be used instead.