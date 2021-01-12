import time
import os
import pyautogui
from playsound import playsound

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

print("Welcome to NexusSolver")

while True:
    try:
        delay = int(input("Enter the delay time (seconds): "))
    except:
        print("Incorrect input")
        pass
    else:
        if delay < 0:
            print("Incorrect input")
            pass
        else:
            break

if __name__ == "__main__":
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
    loglines = follow(logfile)
    print("Waiting for tasks...")
    for line in loglines:
        if line.find("Решите пример:") != -1 and "?" not in line:
            line = line[line.find("Решите пример:") + 15:len(line) - 1]
            print('Task caught: ' + line)
            print('Answer: ' + str(eval(line)))
            playsound("pig.mp3")
            time.sleep(delay)
            pyautogui.press('t')
            pyautogui.write(str(eval(line)))
            pyautogui.press('enter')
            print('Answer sent!')
            print("Waiting for tasks...")