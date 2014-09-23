#!/usr/bin/env python

import re
import sys



def renamer(title_string):
	""" Using the expand function of re.match to do in place string substitution """
	#Example 'Episode 902 - Al Madrigal.mp4' yields 'Never Not Funny s9e02 - Al Madrigal.mp4'

	matches = re.match(r"^(?P<title>Episode)(\s+)(?P<season>\d{1})(?P<episode>\d{2})\s-\s(?P<guest>[^.]*)(?P<suffix>.*)", title_string)
	new_name = m.expand('Never Not Funny s\g<season>e\g<episode> - \g<guest>\g<suffix>')
	return new_name


