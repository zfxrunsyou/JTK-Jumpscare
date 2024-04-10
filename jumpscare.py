import webbrowser
import pyautogui
import time

from tkinter import Tk, Button

root = Tk()

def open_website1():
    webbrowser.open('https://web.archive.org/web/20210516003534im_/https://pnrtscr.com/video.mp4', new=2)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.press('f11')
    pyautogui.press('volumeup', presses=100)
    pyautogui.press('volumeup', presses=100)
    time.sleep(2.4)
    pyautogui.click(x=1334, y=837)
    time.sleep(2.5)
    pyautogui.click(x=1334, y=837)
    time.sleep(2.6)
    pyautogui.click(x=1334, y=837)
    time.sleep(2.7)
    pyautogui.click(x=1334, y=837)
    time.sleep(2.8)
    pyautogui.click(x=1334, y=837)
    time.sleep(2.9)
    pyautogui.click(x=1334, y=837)
    time.sleep(3.0)
    pyautogui.click(x=1334, y=837)
    time.sleep(3.1)
    pyautogui.click(x=1334, y=837)
    time.sleep(3.2)
    pyautogui.click(x=1334, y=837)
    time.sleep(3.3)
    pyautogui.click(x=1334, y=837)
          

button1 = Button(root, text="zfx1", command=open_website1)
button2 = Button(root, text="zfx2", command=open_website1)

button1.pack()
button2.pack()

root.mainloop()
