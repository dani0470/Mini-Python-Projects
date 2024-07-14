import win32com.client as wincom
import time
from plyer import notification
akh=wincom.Dispatch("SAPI.SpVoice")
for i in range(24):
    hou=time.strftime("%H %M")
    time.sleep(3600)
    akh.speak(f"and Its {hou} o clock")
    akh.speak("Hi Please drink water an hour has been passed")
    notification.notify(title="Drink Water Remainder", message="Hi Please drink a glass of water", timeout=2)