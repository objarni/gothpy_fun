Sun set?
========

Parsing the result from https://www.timeanddate.com/sun/sweden/goteborg, you could control a CILamp to either be yellow (sun up), orange (+/- 30 minutes from sunrise time) or red (+/- 30 minutes from sunset time), and otherwise turned off (zero intensity in RGB).

_Kata: Simulate and test this by mocking out the call get_times(), which returns a tuple (sunrise, sunset).

The sun.py script is supposed to be called to update the lamp status, like this:

	python sun.py

Note: there is example code to set lamp color in the root of this repository!

Files:

	test_sun.py  # The tests
	sun.py       # The implementation

