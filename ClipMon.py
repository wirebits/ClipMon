#ClipMon
#A tool which records the copied data of the clipboard.
#Author - Wirebits

import sys
import time
import pyperclip as pc
from datetime import datetime

while True:
	current_time = datetime.now()
	clipboard_text = pc.paste()
	timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")
	if not clipboard_text:
		sys.exit()
	with open("log.txt",'a') as file_log:
		file_log.write(timestamp + ' - ' + clipboard_text + '\n')
	time.sleep(1)