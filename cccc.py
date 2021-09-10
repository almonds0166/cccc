
import re
from time import time, sleep
from sys import stdout

import keyboard
from win32gui import GetWindowText, GetForegroundWindow, SetForegroundWindow

BROWSER_NAMES = ("Mozilla Firefox", "Google Chrome")

# rate
FPS = 10
TIMEOUT = 1 / FPS

# broswer tab title regex, e.g. "(0/0) Queue"
QUEUE = re.compile(r"\(([0-9]+)\/([0-9]+)\) Queue")

def main():
   timer = time()
   max_line_len = 0

   # system's intial states:
   # (True means the active window is the CAT-SOOP help queue)
   last_state = True
   current_state = False

   while True:
      active_title = GetWindowText(GetForegroundWindow())

      current_state = False
      if any(name in active_title for name in BROWSER_NAMES):

         m = QUEUE.match(active_title)

         if m and m.group(1).isdigit() and m.group(2).isdigit():
            unclaimed = int(m.group(1))
            claimed = int(m.group(2))
            # at this point, we're pretty confident that the detected window is
            # the help queue
            current_state = True

            if unclaimed:
               keyboard.press_and_release('c')

      if current_state != last_state:
         stdout.write("\r")
         if not current_state:
            line = "(Active window is not the help queue)"
         else:
            line = f"Claimed: {claimed:<2d} Unclaimed: {unclaimed:<2d}"
            if unclaimed:
               line += " c!"
         
         max_line_len = max(max_line_len, len(line))

         stdout.write(" " * max_line_len + "\r")
         stdout.write(line)
         stdout.flush()

      last_state = current_state

      sleep(max(0, TIMEOUT - (time() - timer)))
      timer = time()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      print("\n^C")
