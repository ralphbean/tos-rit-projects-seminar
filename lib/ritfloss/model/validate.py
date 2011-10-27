#!/usr/bin/env python

import students

from urllib import urlopen
from pprint import pprint

required_keys = [
    'rit_dce',
    'name',
    'blog',
    'irc',
    'forges',
]

def validate():
    for student in students.load_students():
        missing = [key for key in required_keys if key not in student.keys()]

        if missing:
            print
            print "** ERR ",
            pprint(student)
            print "** is missing the following keys ",
            pprint(missing)
            continue

        if not type(student['forges']) is list:
            print "** ERR:  forges for", student['name'], "is not a list."
            continue

        print "Entry %s (%s) looks okay!" % (student['name'], student['irc'])


if __name__ == '__main__':
    validate()
