import pyatspi
def speak(text):
    desktop=pyatspi.Registry.getDesktop(0)
    orca = desktop.findApplication('orca')
    orca.getFocus().getDocument().insertText(text)