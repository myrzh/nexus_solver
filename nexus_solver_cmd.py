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
delay = int(input("Enter the delay time (seconds): "))

if __name__ == "__main__":
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
    loglines = follow(logfile)
    print("Waiting for tasks...")
    for line in loglines:
        if "[main/INFO]: [CHAT]    Решите пример:" in line and "?" not in line: # workaround
            line = line[49:len(line)-1]
            print('Task caught: ' + line)
            print('Answer: ' + str(eval(line)))
            playsound("C:/Windows/Media/Windows Hardware Fail.wav")
            time.sleep(delay)
            pyautogui.press('t')
            pyautogui.write(str(eval(line)))
            pyautogui.press('enter')
            print('Answer sent!')
            print("Waiting for tasks...")