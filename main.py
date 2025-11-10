from pigeon.user import *
from pigeon.util import *

UNREGISTERED_USER = User("guest", "Unregistered")
current_user = UNREGISTERED_USER

prompt = f"{current_user.id} >>> "

def __main__():
    clear()
    print("Welcome to CARRIER PIGEON™©")

    while True:
        command = input(prompt)
        if command in ("", " "): continue

        match command:
            case "current":
                print(f"Current user: {str(current_user)}")
            case "register":
                print("@@@ register")

__main__()