import keyboard
from time import time, sleep
from win32gui import GetWindowText, GetForegroundWindow, SetForegroundWindow

FPS = 20                         # rate
browser_name = "Mozilla Firefox" # "Google Chrome", etc.

timeout = 1 / FPS
timer = time()
try:
   while True:
      active_title = GetWindowText(GetForegroundWindow())

      if browser_name in active_title:

         unclaimed = active_title.split("/", 1)[0][1:]
         if unclaimed.isdigit() and int(unclaimed):
            keyboard.press_and_release('c')
            #print("c", end="")

      sleep(max(0, timeout - (time() - timer)))
      timer = time()

except KeyboardInterrupt:
   print("^C")
