#!/usr/bin/env python

import os
import sys
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-u", "--unlink", action="store_true", dest="unlink",
                  help="remove a directory hardlink")
parser.add_option("-q", "--quiet", action="store_true", dest="quiet",
                  help="no output")

(options, args) = parser.parse_args()

if len(args) == 0:
	print parser.format_help()
	sys.exit()

if options.quiet:
	def log(output):
		pass
else:
	def log(output):
		sys.stdout.write("%s\n" % output)

if options.unlink:
	if len(args) == 0:
		sys.stderr.write("Unlink only supports directories.\n")
		sys.exit(1)
	else:
		for arg in args:
			if os.path.isdir(arg):
				try:
					os.unlink(arg)
					log("Unlink: %s" % arg)
				except OSError, e:
					print e
			else:
				print "%s not a directory, skipping" % arg
else:
	if len(args) == 2:
		log("Link: %s -> %s" % (args[0],args[1]))
		os.link(*args)
	elif len(args) == 1:
		newpath = os.path.basename(args[0])
		log ("Link: %s -> %s" % (args[0],newpath))
		os.link(args[0],newpath)