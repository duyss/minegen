import pyautogui
import time

layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё:–"'),
                           "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~^-@'))
pyautogui.FAILSAFE = True
print('Введите текст\nEnter your text')
txt = str(input())
txeng = txt.translate(layout)
print('Можете переключить окно\nNow you can switch the window')
print('Время ожидания - 10 секунд\nTimeout - 10 seconds')
time.sleep(10)
lenght = len(txeng)
x = lenght
i = 0
j = 220
if lenght < 255:
    pyautogui.typewrite(txeng, interval=0.02)
else:
    kord1, kord2 = pyautogui.position()
    while x > 0:
        tx255 = txeng[i:j]
        pyautogui.typewrite(tx255, interval=0.02)
        pyautogui.click(kord1, kord2)
        pyautogui.move(100,0)
        i = j
        j=j+220
        x=x-220
        time.sleep(0.5)