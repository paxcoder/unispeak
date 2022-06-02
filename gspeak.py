import ctypes
nvda=ctypes.windll.LoadLibrary("./nvdaControllerClient64.dll")
def speak(nvdaspeak):
     nvda.nvdaController_speakText(nvdaspeak)
def nvda_is_running():
     running=nvda.nvdaController_testIfRunning()
     return running