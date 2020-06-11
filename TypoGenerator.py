import pyHook
import pythoncom
import sys
import pyautogui
import random
import pyperclip
import threading


secondpress = False


def clipboard_typo(text):
    e = ''
    for i in text:
        print('"{}"'.format(i))
        if random.choice([1, 2, 3, 4, 5, 6]) == 4:
            print('before: '+i)
            if i in 'abcdefghijklmnopwrstuvwxyz':
                i = random.choice('abcdefghijklmnopwrstuvwxyz')
            elif i in 'abcdefghijklmnopwrstuvwxyz'.upper():
                i = random.choice('abcdefghijklmnopwrstuvwxyz'.upper())
            elif i in '1234567890':
                i = random.choice('1234567890')
            elif i == ' ':
                e += '  '
            elif i == '.'
                e += random.choice(',<>/?;:')
            print('after: '+i)
        e += i
    print('Randomized clipboard to {}'.format(e))
    pyperclip.copy(e)


def pyp_manager():
    clipboard_typo(pyperclip.waitForPaste())
    while True:
        clipboard_typo(pyperclip.waitForNewPaste())


def on_keypress(event):
    global secondpress
    if not secondpress:
        if event.Key.lower() not in 'abcdefghijklmnopwrstuvwxyz1234567890':
            return True
        if random.choice([1, 2, 3, 4, 5, 6]) == 4:
            secondpress = True
            if event.Key in '1234567890':
                pyautogui.press(random.choice('1234567890'))
            else:
                pyautogui.press(random.choice('abcdefghijklmnopqrstuvwxyz'))
        else:
            return True
        return False
    else:
        secondpress = False
        return True


threading.Thread(target=pyp_manager).start()
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = on_keypress
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
