import os
import unittest
from testfixtures import compare

from wordpresscheckversion import WordpressCheckVersion


class WCVTests(unittest.TestCase):
    def test_Readme(self):

        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/readme.html'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_readme(testdata)
        file.close()
        self.assertEqual(v, '4.7')

    def test_Readme_no_version(self):

        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/readme_no_version.html'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_readme(testdata)
        file.close()
        self.assertFalse(v)

    def test_Admin(self):
        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/wp-login.html'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_admin(testdata)
        file.close()
        self.assertEqual(v, '4.7.3')

    def test_Admin_no_version(self):

        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/wp-login_no_version.html'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_admin(testdata)
        file.close()
        self.assertFalse(v)

    def test_GeneratorSiteFeed(self):
        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/feed.xml'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_generator_feed(testdata)
        file.close()
        self.assertEqual(v, '4.7.3')

    def test_GeneratorSiteFeed_no_version(self):
        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/feed_no_version.xml'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_generator_feed(testdata)
        file.close()
        self.assertFalse(v)

    def test_GeneratorSite(self):
        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/index.html'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_generator_site(testdata)
        file.close()
        self.assertEqual(v, '4.7.3')

    def test_GeneratorSite_no_version(self):
        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/index_no_version.html'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_generator_site(testdata)
        file.close()
        self.assertFalse(v)

    def test_GeneratorSite_no_generator(self):
        file = open(os.path.join(os.path.dirname(__file__), 'webfiles/index_no_generator.html'))
        testdata = file.read()
        w = WordpressCheckVersion()
        v = w.get_generator_site(testdata)
        file.close()
        self.assertFalse(v)

    def test_md5_database(self):
        w = WordpressCheckVersion()
        v = w.get_md5('8610f03fe77640dee8c4cc924e060f12')
        resulttest = [('4.8.3',), ('4.8.2',), ('4.8.1',), (4.8,), ('4.7.7',), ('4.7.6',), ('4.7.5',), ('4.7.4',), ('4.7.3',), ('4.7.2',), ('4.7.1',), (4.7,), ('4.6.8',), ('4.6.7',), ('4.6.6',), ('4.6.5',), ('4.6.4',), ('4.6.3',), ('4.6.2',), ('4.6.1',), (4.6,), ('4.5.11',), ('4.5.10',), ('4.5.9',), ('4.5.8',), ('4.5.7',), ('4.5.6',), ('4.5.5',), ('4.5.4',), ('4.5.3',)]
        self.assertListEqual(v,resulttest)

if __name__ == '__main__':
    unittest.main()
