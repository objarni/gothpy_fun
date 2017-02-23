import unittest

from got_mail import update_lamp_status


class TestGotMail(unittest.TestCase):

    def test_lamp_is_set_to_green_when_no_mails_in_inbox(self):
        # TODO
        pass

    def test_lamp_is_set_to_orange_when_1_to_9_mails(self):
        # TODO
        pass

    def test_lamp_is_set_to_red_if_10_or_more_mails(self):
        # TODO
        pass


if __name__ == '__main__':
    unittest.main()
