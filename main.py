import ctypes
import os
import random
import shutil

def Admin():
    try:
        admin = (os.getuid() == 0)

    except AttributeError:
        admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return admin

if Admin():
    chamber = [1, 2, 3, 4, 5, 6]
    print("In order to play this game, you must accept all risks involved. I recommend spinning up a virtual machine as if you lose, your data will be lost. Do you accept the risks? (y/n)")
    confirm = input()
    if confirm == "y":
        input("Press Enter To Pull The Trigger.")
        if random.choice(chamber) == 6:
            print("bang!")
            try:
                shutil.rmtree(fr"/home/{os.getlogin()}")

            except:
                try:
                    shutil.rmtree(fr"/home/{os.getlogin()}")

                except:
                    shutil.rmtree(fr"/home/{os.getlogin()}")

            input()

        else:
            print("click")
            input()

    else:
        pass

else:
    print("Run this as administrator to play.")
