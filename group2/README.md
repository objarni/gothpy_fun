Web site down?
==============

isup.me is a site that can be used to check whether a web site is up or down (not sure how, but it seems to work quite well). If you post-pend a website url (e.g. isup.me/dn.se), and parse the result html body (use WGET, curl or e.g. the fabulous mechanize Python library, or some other useful GET fetching library), you can somewhat reliably check if a site is up or down.

_Kata: mocking out the actual fiddling with isup.me (just fake some html result from the site!), control a CILamp to show green (site up) or red (site down)!_

The site_up.py script is supposed to be called to update the lamp status, like this:

	python site_up.py

Note: there is example code to set lamp color in the root of this repository!

Files:

	test_site_up.py  # The tests
	site_up.py       # The implementation

