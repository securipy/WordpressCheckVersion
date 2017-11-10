#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

""" Wordpress Check Version """

import sqlite3

import os.path

__author__ = "GoldraK"
__credits__ = "GoldraK"
__version__ = "0.1"
__maintainer__ = "GoldraK"
__email__ = "goldrak@gmail.com"
__status__ = "Development"


class Database(object):
    """
    Database object
    """

    def __init__(self):
        basedir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(basedir, "versions.db")
        self.con_bd = sqlite3.connect(db_path)

    def get_versions(self):
        cursor_version = self.con_bd.cursor()
        cursor_version.execute("SELECT * FROM wp_version")
        return cursor_version

    def get_version(self, version):
        cursor_version = self.con_bd.cursor()
        cursor_version.execute("SELECT * FROM wp_version WHERE version=?", (version, ))
        data = cursor_version.fetchone()
        return data

    def set_version(self, version):
        cursor_version = self.con_bd.cursor()
        cursor_version.execute("INSERT INTO wp_version (version) VALUES (?)",  (version, ))
        self.con_bd.commit()
        return cursor_version.lastrowid

    def get_files(self):
        cursor_files = self.con_bd.cursor()
        cursor_files.execute("SELECT * FROM files")
        data = cursor_files.fetchall()
        return data

    def get_file(self, file):
        cursor_files = self.con_bd.cursor()
        cursor_files.execute("SELECT * FROM files WHERE name=?", (file, ))
        data = cursor_files.fetchone()
        return data

    def set_files(self, file):
        cursor_files = self.con_bd.cursor()
        cursor_files.execute("INSERT INTO wp_version (name) VALUES (?)", (file, ))
        self.con_bd.commit()
        return cursor_files.lastrowid

    def get_md5s(self):
        cursor_md5 = self.con_bd.cursor()
        cursor_md5.execute("SELECT * FROM md5")
        data = cursor_md5.fetchall()
        return data

    def get_md5(self, md5):
        cursor_md5 = self.con_bd.cursor()
        cursor_md5.execute("SELECT * FROM md5 WHERE md5=?", (md5, ))
        data = cursor_md5.fetchone()
        return data

    def set_md5(self, md5):
        cursor_md5 = self.con_bd.cursor()
        cursor_md5.execute("INSERT INTO md5 (md5) VALUES (?)", (md5, ))
        self.con_bd.commit()
        return cursor_md5.lastrowid

    def set_version_file_md5(self, id_version, id_md5, id_file):
        cursor_versionfilemd5 = self.con_bd.cursor()
        cursor_versionfilemd5.execute("INSERT INTO wp_files_md5 (wp_id,md5_id,file_id)" +
                                      "VALUES (?,?,?)", (id_version, id_md5, id_file))
        self.con_bd.commit()
        return cursor_versionfilemd5.lastrowid

    def get_version_md5(self, md5):
        cursor_versionmd5 = self.con_bd.cursor()
        cursor_versionmd5.execute("""SELECT version FROM wp_md5 as wp_md5 INNER JOIN wp_files_md5  as wp_files_md5 ON wp_files_md5.md5_id = wp_md5.id INNER JOIN wp_version as wp_version ON wp_files_md5.wp_id = wp_version.id INNER JOIN wp_files as wp_files ON wp_files_md5.file_id = wp_files.id WHERE wp_md5.wp_md5 = ? """, (md5, ))
        data = cursor_versionmd5.fetchall()
        return data
