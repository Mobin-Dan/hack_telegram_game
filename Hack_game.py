import colorama
#mr_ngrok |T.me/termux_learning
print(Fore.CAYAN+"

 _     ____  ____  _  __   _____ ____  _      _____   _  ____    ____  _     
/ \ /|/  _ \/   _\/ |/ /  /  __//  _ \/ \__/|/  __/  / \/ ___\  /  _ \/ \  /|
| |_||| / \||  /  |   /   | |  _| / \|| |\/|||  \    | ||    \  | / \|| |\ ||
| | ||| |-|||  \_ |   \   | |_//| |-||| |  |||  /_   | |\___ |  | \_/|| | \||
\_/ \|\_/ \|\____/\_|\_\  \____\\_/ \|\_/  \|\____\  \_/\____/  \____/\_/  \|
                                                                             

")

import pyautogui, time
time.sleep(5)
while True:
	screen = pyautogui.screenshot().convert("RGB")
	l1, l2 = screen.getpixel((872, 642)), screen.getpixel((1045, 642))
	l3, l4 = screen.getpixel((872, 541)), screen.getpixel((1045, 541))
	l5, l6 = screen.getpixel((872, 444)), screen.getpixel((1045, 444))
	l7, l8 = screen.getpixel((872, 343)), screen.getpixel((1045, 343))	
	l9, l10 = screen.getpixel((872, 243)), screen.getpixel((1045, 243))
	l11, l12 = screen.getpixel((872, 143)), screen.getpixel((1045, 143))
	if l1==(211, 247, 255) or l2==(153, 204, 102):
		pyautogui.press('left')
		pyautogui.press('left')
	else:
		pyautogui.press('right')
		pyautogui.press('right')
	if l3==(211, 247, 255) or l4==(153, 204, 102):
		pyautogui.press('left')
		pyautogui.press('left')
	else:
		pyautogui.press('right')
		pyautogui.press('right')
	if l5==(211, 247, 255) or l6==(153, 204, 102):
		pyautogui.press('left')
		pyautogui.press('left')
	else:
		pyautogui.press('right')
		pyautogui.press('right')
	if l7==(211, 247, 255) or l8==(153, 204, 102):
		pyautogui.press('left')
		pyautogui.press('left')
	else:
		pyautogui.press('right')
		pyautogui.press('right')
	if l9==(211, 247, 255) or l10==(153, 204, 102) or l9==(241, 252, 255):
		pyautogui.press('left')
		pyautogui.press('left')
	else:
		pyautogui.press('right')
		pyautogui.press('right')
	if l11==(211, 247, 255) or l12==(153, 204, 102) or l11==(241, 252, 255):
		pyautogui.press('left')
		pyautogui.press('left')
	else:
		pyautogui.press('right')
		pyautogui.press('right')
	time.sleep(0.05)
