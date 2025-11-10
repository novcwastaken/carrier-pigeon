import os
import sys

# clear
if sys.platform in ("linux", "darwin"):
    CLEAR = "clear"
elif sys.platform == "win32":
    CLEAR = "cls"

def clear():
    os.system(CLEAR)