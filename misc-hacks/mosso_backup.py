#!/usr/bin/env python

import sys
import cloudfiles

# If output is not a TTY (e.g. in a cronjob) it won't print the log data.
# That way, you won't get e-mails every time this runs.
if sys.stdout.isatty():
	log = lambda x: sys.stdout.write(x + '\n')
else:
	log = lambda x: x

username = 'YOURUSER'
apikey = 'YOURKEY'

if len(sys.argv) < 3:
	log("Invalid command line: %s" % ' '.join(sys.argv))
	log("Usage: %s <container name> [destination filename] <local filename>" % sys.argv[0])
	sys.exit(1)
	
contname,filename = sys.argv[1:3]

try:
	sys.argv[3]
except IndexError, e:
	targetname = filename
else:
	targetname = filename
	filename = sys.argv[3]

log("Connecting to account %s..." % username)
conn = cloudfiles.get_connection(username, apikey)

log("Creating container %s... " % contname)
container = conn.create_container(contname)

log("Creating object... ")
cfile = container.create_object(targetname)

log("Uploading file %s..." % filename)
cfile.load_from_filename(filename)

log("Done!")
