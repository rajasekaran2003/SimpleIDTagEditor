# SimpleIDTagEditor
Simple ID tag editor for Music files. 

I normally organize my music files by the following folder structure

		Music
		-----Artist1
		------------Album1
		-----------------song1
		-----------------song2
		-----------------song3
		-----------------song'n'
		.
		.
		------------Album'n'
		-----------------song1
		-----------------song2
		-----------------song3
		-----------------song'n'
		.
		.

		-----Artist'n'
		------------Album1
		-----------------song1
		-----------------song2
		-----------------song3
		-----------------song'n'
		.
		.
		------------Album'n'
		-----------------song1
		-----------------song2
		-----------------song3
		-----------------song'n'

People using iPhones would know the hardship of finding music if their Id tags are not filled in properly.

Since iOS lacks folder structure, its really hard to have music organized in the same way as it is in your computer.


# Prerequisites
--------------
Python

Python Packages:eyed3, mutagen


# To install python packages
---------------------------
pip install eyed3

pip install mutagen

# Reason for using both eyed3 and mutagen
-----------------------------------------
I have used both eyed3 and mutagen because eyed3 can modify or add only ID3 tags.

so if your track currently has other versions of ID tags, then mutagen does a great job of clearing them up for eyed3 to take effect.

I found that the combination worked better than one with various version of ID tags and tracks.

I organized around 5k titles through this script and they were of varying formats.


# How to use the script
----------------------
if you folder structure is like

		Music
		-----Artist1
		------------Album1
		-----------------song1
		-----------------song2
		-----------------song3
		-----------------song'n'
		.
		.
		------------Album'n'
		-----------------song1
		-----------------song2
		-----------------song3
		-----------------song'n'
		.
		.

		-----Artist'n'
		------------Album1
		-----------------song1
		-----------------song2
		-----------------song3
		-----------------song'n'
		.
		.
		------------Album'n'
		-----------------song1
		-----------------song2
		-----------------song3
		-----------------song'n'

run the script from Music folder

cd Music

Music/:

**python script.py Artist1**

