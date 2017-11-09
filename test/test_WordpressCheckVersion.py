import os
import unittest

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


if __name__ == '__main__':
    unittest.main()
