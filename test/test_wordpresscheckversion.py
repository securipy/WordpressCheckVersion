import unittest

from wordpresscheckversion import WordpressCheckVersion


class WCVTests(unittest.TestCase):
    def test_Readme(self):

        w = WordpressCheckVersion()
        v = w.getReadme('<h1 id="logo">' +
                        '<a href="https://wordpress.org/"><img alt="WordPress" src="wp-admin/images/wordpress-logo.png"></a>'+
                        '<br /> Version 4.7</h1>')

        self.assertEqual(v, '4.7')

    def test_Readme_no_version(self):

        w = WordpressCheckVersion()
        v = w.getReadme('<h1 id="logo">' +
                        '<a href="https://wordpress.org/"><img alt="WordPress" src="wp-admin/images/wordpress-logo.png"></a>'+
                        '<br /> Version </h1>')

        self.assertEqual(v, False)

    def test_Admin(self):

        w = WordpressCheckVersion()
        v = w.getAdmin("<link rel='dns-prefetch' href='//s.w.org' /><script type='text/javascript' src='http://localhost.example/wp-admin/load-scripts.php?c=0&amp;load%5B%5D=jquery-core,jquery-migrate&amp;ver=4.7.3'></script><link rel='stylesheet' href='http://localhost.example/wp-admin/load-styles.php?c=0&amp;dir=ltr&amp;load%5B%5D=dashicons,buttons,forms,l10n,login&amp;ver=4.7.3' type='text/css' media='all' /><meta name='robots' content='noindex,follow' /><meta name='viewport' content='width=device-width' /></head><body class='login login-action-login wp-core-ui  locale-es-es'><div id='login'>")

        self.assertEqual(v, '4.7.3')

    def test_Admin_no_version(self):

        w = WordpressCheckVersion()
        v = w.getAdmin("<link rel='dns-prefetch' href='//s.w.org' /><script type='text/javascript' src='http://localhost.example/wp-admin/load-scripts.php?c=0&amp;load%5B%5D=jquery-core,jquery-migrate'></script><link rel='stylesheet' href='http://localhost.example/wp-admin/load-styles.php?c=0&amp;dir=ltr&amp;load%5B%5D=dashicons,buttons,forms,l10n,login' type='text/css' media='all' /><meta name='robots' content='noindex,follow' /><meta name='viewport' content='width=device-width' /></head><body class='login login-action-login wp-core-ui  locale-es-es'><div id='login'>")

        self.assertEqual(v, False)


    def test_GeneratorSiteFeed(self):

        w = WordpressCheckVersion()
        v = w.getGeneratorFeed('<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"'+
                                'xmlns:content="http://purl.org/rss/1.0/modules/content/"'+
                                'xmlns:wfw="http://wellformedweb.org/CommentAPI/"'+
                                'xmlns:dc="http://purl.org/dc/elements/1.1/"'+
                                'xmlns:atom="http://www.w3.org/2005/Atom"'+
                                'xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"'+
                                'xmlns:slash="http://purl.org/rss/1.0/modules/slash/"'+
                                '>'+
                            '<channel>'+
                                '<title>Test Check Wordpress Version</title>'+
                                '<atom:link href="http://localhost.example/feed/" rel="self" type="application/rss+xml" />'+
                                '<link>http://localhost.example</link>'+
                                '<description>Blog demo.</description>'+
                                '<lastBuildDate>Mon, 10 Apr 2017 16:12:52 +0000</lastBuildDate>'+
                                '<language>es-ES</language>'+
                                '<sy:updatePeriod>hourly</sy:updatePeriod>'+
                                '<sy:updateFrequency>1</sy:updateFrequency>'+
                                '<generator>https://wordpress.org/?v=4.7.3</generator>'+

                            '</channel>'+
                            '</rss>')



        self.assertEqual(v, '4.7.3')


    def test_GeneratorSiteFeed_no_version(self):

        w = WordpressCheckVersion()
        v = w.getGeneratorFeed('<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"'+
                                'xmlns:content="http://purl.org/rss/1.0/modules/content/"'+
                                'xmlns:wfw="http://wellformedweb.org/CommentAPI/"'+
                                'xmlns:dc="http://purl.org/dc/elements/1.1/"'+
                                'xmlns:atom="http://www.w3.org/2005/Atom"'+
                                'xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"'+
                                'xmlns:slash="http://purl.org/rss/1.0/modules/slash/"'+
                                '>'+
                            '<channel>'+
                                '<title>Test Check Wordpress Version</title>'+
                                '<atom:link href="http://localhost.example/feed/" rel="self" type="application/rss+xml" />'+
                                '<link>http://localhost.example</link>'+
                                '<description>Blog demo.</description>'+
                                '<lastBuildDate>Mon, 10 Apr 2017 16:12:52 +0000</lastBuildDate>'+
                                '<language>es-ES</language>'+
                                '<sy:updatePeriod>hourly</sy:updatePeriod>'+
                                '<sy:updateFrequency>1</sy:updateFrequency>'+
                                '<generator>https://wordpress.org/</generator>'+

                            '</channel>'+
                            '</rss>')



        self.assertEqual(v, False)

    def test_GeneratorSite(self):

        w = WordpressCheckVersion()
        v = w.getGeneratorSite('<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://localhost.example/xmlrpc.php?rsd" /><link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://localhost.example/wp-includes/wlwmanifest.xml" /> <meta name="generator" content="WordPress 4.7.3" /><link rel="canonical" href="http://localhost.example/" /><link rel="shortlink" href="http://localhost.example/" />')

        self.assertEqual(v, '4.7.3')

    def test_GeneratorSite_no_version(self):

        w = WordpressCheckVersion()
        v = w.getGeneratorSite('<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://localhost.example/xmlrpc.php?rsd" /><link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://localhost.example/wp-includes/wlwmanifest.xml" /> <meta name="generator" content="WordPress" /><link rel="canonical" href="http://localhost.example/" /><link rel="shortlink" href="http://localhost.example/" />')

        self.assertEqual(v, False)

    def test_GeneratorSite_no_generator(self):

        w = WordpressCheckVersion()
        v = w.getGeneratorSite('<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://localhost.example/xmlrpc.php?rsd" /><link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://localhost.example/wp-includes/wlwmanifest.xml" /><link rel="canonical" href="http://localhost.example/" /><link rel="shortlink" href="http://localhost.example/" />')

        self.assertEqual(v, False)


if __name__ == '__main__':
    unittest.main()
