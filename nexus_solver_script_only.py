import time
import os
import pyautogui

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == "__main__": # в душе не ебу зачем это нужно
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
    loglines = follow(logfile)
    for line in loglines:
        if "[main/INFO]: [CHAT]    Решите пример:" in line and "?" not in line: # плохой костыль, надо сделать нормально
            line = line[49:len(line)-1]
            print(line)
            print(eval(line))
            pyautogui.press('t')
            pyautogui.write(str(eval(line)))
            pyautogui.press('enter')