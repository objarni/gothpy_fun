Got mail?
=========

There is a RESTful API to access your GMail account content. What if you could have CIlamp that is green if you have an empty inbox, yellow if you have 1-9 mails in it, and red otherwise? We all want empty mail-boxes, don't we? :)

Kata: Use TDD to develop this functionality, using a mocked-out function get_inbox_count() which counts how many mails are in the inbox. If you want to actually implement the function, see this blog post for inspiration:

https://www.sitepoint.com/mastering-your-inbox-with-gmail-javascript-api/


The got_mail.py script is supposed to be called to update the lamp status, like this:

	python got_mail.py

Note: there is example code to set lamp color in the root of this repository!

Files:

	test_got_mail.py  # The tests
	got_mail.py       # The implementation

