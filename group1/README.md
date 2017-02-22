Bridge open?
============

Gothenburg city council has a public API that tells whether the “Götaälvbro” is open or not. Make a lamp that is green if the bridge is usable as a car/bus/tram/bicycle passenger (bridge closed), and red if not (bridge open).

_Kata: mock out the “bridge_open” function, which return True if the bridge is open and False otherwise, and make tests that the correct API calls are made to api.cilamp.se! (implementing the actual Gbg council API calls is left as a post-GothPy excercise!)_

The bridge.py script is supposed to be called to update the lamp status, like this:

	python bridge.py

Note: there is example code to set lamp color in the root of this repository!

Files:
	test_bridge.py  # The tests
	bridge.py       # The implementation


