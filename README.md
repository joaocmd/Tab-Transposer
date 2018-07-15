# Tab Transposer

This program is used to transpose text file guitar tabs.

## Requirements

You must have python installed in order to run the script (Written in python 3.6).

## Instructions

* Run the script, and it asks the name of the tab that you want to transpose. If your file is "tab.txt", type "tab", the files have to be under the same directory.
* The program will ask for how many frets to transpose to, this is pretty straightforward, type 5 if you want to subtract 5 from the original numbers, etc.
* Next the program will ask for the green lights. This is useful if the tab has multiple playing guitars and you only want to change for example "Guitar 1". If no string is given, it will start transposing from the beggining of the file (it will replace all numbers, not just ones in the tab).
* The next step is to give the programs the red lights. For example if there are three guitars and you only want to change the first one, give "Guitar 1" as a green light and "Guitar" as an invalid one, it will only check if it's invalid after checking if it's valid. This can also be used to stop transposing after a given line, such as "Verse 1".
* Voila, it should be finished!
* The new file will be caled "tab_new.txt" and will be on the same directory as the original "tab.txt" file.

## Example:

Simple example "tab".

Given a file and these options:
* Frets to transpose: 5
* Green lights: Guitar 1
* Red lights: Guitar

Original file:
```
Guitar 1
|------6---7--8h9--5|
|---5---------------|

Guitar 2
|------4---5--6h7--2|

Guitar 1
|------5---6--6h7---|
|---5--------------5|
```

The new file:
```
|Guitar 1
|------1---2--3h4--0|
|---0---------------|

Guitar 2
|------4---5--6h7--2|

Guitar 1
|------0---1--1h2---|
|---0--------------0|
```
