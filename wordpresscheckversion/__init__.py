#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

""" Wordpress Check Version """

import re

from bs4 import BeautifulSoup

__author__ = "GoldraK"
__credits__ = "GoldraK"
__version__ = "0.1.0"
__maintainer__ = "GoldraK"
__email__ = "goldrak@gmail.com"
__status__ = "Development"


class WordpressCheckVersion(object):
    """
    Wordpress Check Version object
    """

    __slots__ = ('generator', 'regex', 'matches', 'url_version', 'html', 'part_version')

    def __init__(self):
        self.url_version = ""

    def get_admin(self, html):
        """
        This function read version into wp-login
        """
        regex = r"(;ver=)([0-9\.]+)([\-a-z]*)"
        matches = re.search(regex, str(html), re.IGNORECASE)
        if matches:
            if len(matches.groups()) != 3:
                return False
            else:
                return matches.group(2)
        else:
            return False

    def get_generator_site(self, html):
        """
        This function search version into meta generator
        """
        soap = BeautifulSoup(html, 'html.parser')
        generator = soap.findAll("meta", {"name": "generator"})
        if generator:
            part_version = generator[0]['content'].split(' ')
            if len(part_version) == 2:
                return part_version[1]
            else:
                return False
        else:
            return False

    def get_generator_feed(self, html):
        """
        This function search version into feed
        """
        soap = BeautifulSoup(html, 'lxml')
        generator = soap.findAll("generator")[0]
        if generator:
            regex = r"<generator>([^<]*)</generator>"
            matches = re.match(regex, str(generator), re.IGNORECASE)
            if matches:
                for group_num in range(0, len(matches.groups())):
                    group_num = group_num + 1
                    self.url_version = matches.group(group_num)
                if self.url_version:
                    part_version = self.url_version.split('?v=')
                    if len(part_version) == 2:
                        return part_version[1]
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def get_readme(self, html):
        """
        This function search version into Readme.html
        """
        soup = BeautifulSoup(html, "html.parser")
        readme = soup.find_all('h1', {"id": "logo"})
        regex = r"""(<br[\s]*/>[\s]*[Vv]ersion[\s]*)([\d]\.[\d]\.*[\d]*)"""
        matches = re.search(regex, str(readme), re.IGNORECASE)
        if matches:
            if len(matches.groups()) != 2:
                return False
            else:
                return matches.group(2)
        else:
            return False
