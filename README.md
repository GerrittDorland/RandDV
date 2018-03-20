# RANDOM DISTORTED VIEW SHOW SCRIPT

This thing currently only works on Windows. I'll update it to be multiplatform if there is any interest.

USAGE (universal):
	- While script is running, set focus to the console that is running the script.
	- Press [ENTER]. Alternatively, enter 't' or 'today'+[ENTER] to attempt to load today's show.

TO CLOSE (universal):
	- Escape sequence is required. On OSX/Linux, use CTRL+C.
	- On Windows, just close the IDLE/Powershell window.

USAGE (Windows):
	- While the script is running, press R_CONTROL. Window focus on the script is not necessary.

TO COMPILE (universal):
	- No dependencies. Python 2.7.

TO COMPILE (Windows):
	- You need two non-standard Python libraries:
		- win32api
		- win32con
	- You can get both here: https://github.com/mhammond/pywin32

FUTURE:
	- No plans. If people complain enough, I'll make conversions for OSX and/or Linux.
