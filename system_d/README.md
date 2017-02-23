Coffee ready?
=============

If you could get a numerical reading from the coffee container, how much it weighs (or something similar), you could set the color of a CILamp to some color between green (full) and red (no more coffee) by interpolating between the two colors component-wise.

_Kata: Develop this functionality using test driven development towards an imaginary get_coffee_weight (giving a numerical value between 0.0 and 1.0)._

The coffee.py script is supposed to be called to update the lamp status, like this:

	python coffee.py

Note: there is example code to set lamp color in the root of this repository!

Files:

	test_coffee.py  # The tests
	coffee.py       # The implementation

