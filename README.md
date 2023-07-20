# SMARTGreen
SMART Green project for GWS Living Art 

17/7/23 V1.3.1 release
Made amendments to the folder in order for the raspberrypi to
launch the python script on startup.
Updated the instructions and added a few more files:
1. launcher.sh
2. logs

amended code:
1. main.py (programed button)

12/7/23 V1.3 release
This is the final version for usage.
The changes:
1. logging.py
	The logging systm will be on the database. To name
	the file we will connect to the database and retrieve
	the number of the previous entry

	There will be no .csv

2. button.py
	This is a programmable button that would allow you to
	connect/code to the raspberrypi device. This button will end the main function if pressed (hold) on boot.

4/7/23 V1.2.1 alpha
The bugs of v1.1 was fixed:

1. reuccuring uploads 
	fixed in main.py by adding stream.stop() & stream.start()

2. slow transmition times
	added BytesIO() functions in audio.py & 
	main.py

3. delayed recordings
	fixed in audio.py by changing the modules


28/6/23 V1.2 alpha

This code is used to test out on the raspberrypi.
The following Modules have been added:

1. Microphone module

The main.py was changed to fix the functionality of
the device

21/6/23 V1.1 beta

The orignal code of V1.0 beta was built upon.
The following Modules have been added:

1. Cloud module
2. UPS monitor module

3. Microphone module (yet to be added)
   
There are bugs present in the program such as:
1. reuccuring uploads
2. slow transmition times
3. delayed recordings

20/6/23 V1.0 beta

This is the base code that would suffice the project.
The following Modules will be adeed to V1.1 beta:

1. Cloud module
2. Microphone module
3. UPS monitor module

And subsequently cleaning the code, debugging and making it user
friendly will be done for V1.0 release
