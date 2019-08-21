# RANDOM DISTORTED VIEW SHOW SCRIPT

THE SKINNY:
	- The "Universal" script works on all platforms, but requires interacting with the console window to load new shows. This script is more robust, and sports a couple extra commands e.g. the 'today' command.
	- THE WINDOWS SCRIPT IS DEAD.

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
