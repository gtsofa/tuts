#This tests name program if it works as expected.
import unittest

from name import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'name.py'. """

    def test_first_last_name(self):
        """Do names like 'Julius Nyule' work? """
        formatted_name = get_formatted_name('Julius', 'nyule')#call function we want to test & store a return value that we'are interested in testing. 
        self.assertEqual(formatted_name, 'Julius Nyule')

    def test_first_last_middle_name(self):
        """Do names like 'Julius Tsofa Nyule' work? """
        formatted_name = get_formatted_name('julius', 'nyule', 'tsofa')
        self.assertEqual(formatted_name, 'Julius Tsofa Nyule')

unittest.main()
