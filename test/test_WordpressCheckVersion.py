import os
import unittest

from wordpresscheckversion import WordpressCheckVersion


class WCVTests(unittest.TestCase):
    def test_Readme(self):

        path = os.path.join(os.path.dirname(__file__), 'webfiles/readme.html')
        testdata = open(path).read()
        w = WordpressCheckVersion()
        v = w.getReadme(testdata)

        self.assertEqual(v, '4.7')

    def test_Readme_no_version(self):

        path = os.path.join(os.path.dirname(__file__), 'webfiles/readme_no_version.html')
        testdata = open(path).read()
        w = WordpressCheckVersion()
        v = w.getReadme(testdata)

        self.assertFalse(v)

    def test_Admin(self):

        path = os.path.join(os.path.dirname(__file__), 'webfiles/wp-login.html')
        testdata = open(path).read()
        w = WordpressCheckVersion()
        v = w.getAdmin(testdata)

        self.assertEqual(v, '4.7.3')

    def test_Admin_no_version(self):

        path = os.path.join(os.path.dirname(__file__), 'webfiles/wp-login_no_version.html')
        testdata = open(path).read()
        w = WordpressCheckVersion()
        v = w.getAdmin(testdata)

        self.assertFalse(v)


    def test_GeneratorSiteFeed(self):

        path = os.path.join(os.path.dirname(__file__), 'webfiles/feed.xml')
        testdata = open(path).read()
        w = WordpressCheckVersion()
        v = w.getGeneratorFeed(testdata)



        self.assertEqual(v, '4.7.3')


    def test_GeneratorSiteFeed_no_version(self):

        path = os.path.join(os.path.dirname(__file__), 'webfiles/feed_no_version.xml')
        testdata = open(path).read()
        w = WordpressCheckVersion()
        v = w.getGeneratorFeed(testdata)

        self.assertFalse(v)

    def test_GeneratorSite(self):

        w = WordpressCheckVersion()
        v = w.getGeneratorSite('<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://localhost.example/xmlrpc.php?rsd" /><link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://localhost.example/wp-includes/wlwmanifest.xml" /> <meta name="generator" content="WordPress 4.7.3" /><link rel="canonical" href="http://localhost.example/" /><link rel="shortlink" href="http://localhost.example/" />')

        self.assertEqual(v, '4.7.3')

    def test_GeneratorSite_no_version(self):

        w = WordpressCheckVersion()
        v = w.getGeneratorSite('<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://localhost.example/xmlrpc.php?rsd" /><link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://localhost.example/wp-includes/wlwmanifest.xml" /> <meta name="generator" content="WordPress" /><link rel="canonical" href="http://localhost.example/" /><link rel="shortlink" href="http://localhost.example/" />')

        self.assertFalse(v)

    def test_GeneratorSite_no_generator(self):

        w = WordpressCheckVersion()
        v = w.getGeneratorSite('<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://localhost.example/xmlrpc.php?rsd" /><link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://localhost.example/wp-includes/wlwmanifest.xml" /><link rel="canonical" href="http://localhost.example/" /><link rel="shortlink" href="http://localhost.example/" />')

        self.assertFalse(v)


if __name__ == '__main__':
    unittest.main()
