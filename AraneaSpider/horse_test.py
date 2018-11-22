from urllib.request import urlopen
from bs4 import BeautifulSoup

import unittest

class TestHorseLand(unittest.TestCase): 
    soup = None

    def setUpClass(): 
        url = 'https://treehouse-projects.github.io/horse-land/index.html'

        # Define soup object
        TestHorseLand.soup = BeautifulSoup(urlopen(url), 'html.parser')

        def test_header1(self): 
            header1 = TestHorseLand.soup.find('h1').get_text()
            # Make sure header 1 is equal to what our string should be. 
            self.assertEqual('Horse Land', header1)

if __name__ == '__main__': 
    unittest.main()
    
