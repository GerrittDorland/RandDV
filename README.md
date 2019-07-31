# RANDOM DISTORTED VIEW SHOW SCRIPT

THE SKINNY:
	- The "Universal" script works on all platforms, but requires interacting with the console window to load new shows. This script is more robust, and sports a couple extra commands e.g. the 'today' command.
	- The "Windows" script only works on Windows. It's pretty fucking trash in comparison at this point, but you can load a show without window focus... I also think the Windows script can't load Sideshow shows? I can't remember.

USAGE (universal):
	- While script is running, set focus to the console that is running the script.
	- Press [ENTER] to load a random show.
	- Enter 't' or 'today'+[ENTER] to attempt to load today's show.
	- Enter 'y' or 'yesterday'+[ENTER] to attempt to load yesterday's show
		+ This is actually for loading "today's" show after midnight...

TO CLOSE (universal):
	- Escape sequence is required. On OSX/Linux, use CTRL+C.
	- On Windows, just close the IDLE/Powershell window.

TO COMPILE (universal):
	- No dependencies. Python 2.7.

USAGE (Windows):
	- While the script is running, press R_CONTROL. Window focus on the script is not necessary.

TO COMPILE (Windows):
	- You need two non-standard Python libraries:
		- win32api
		- win32con
	- You can get both here: https://github.com/mhammond/pywin32
