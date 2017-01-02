# Created by: Iêso Dias // iesodias.com // iesodias.wordpress.com // github.com/iesodias 
# Script for clean the print spooler to windows 2003 ~ 2012
# Tutorial: iesodias.wordpress.com - 

import os

start_prog = str(input("Clean Printer Spooler? (Type Yes or No):"))

if start_prog == "Yes" or start_prog == "y" or start_prog == "yes":
	#stop printer spool
	os.system('net stop spooler /y')
	#changing the current directory for default folder of windows spool
	os.chdir('C:\\Windows\\System32\\spool\\PRINTERS')
	#deleting all files
	print(os.system('del /f /s *.shd'))
	print(os.system('del /f /s *.spl'))
	print(os.system('del /f /s *.tmp'))
	#start printer spool
	print(os.system('net start spooler'))
	print("Files deleted successfully")
else:
	print("Closing the program")