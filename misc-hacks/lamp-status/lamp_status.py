#!/usr/bin/env python

import os
import sys
import time
import urllib2

#######################################
# Configure these variables if you like
rootpath = "/root/agz"
serverstatusurl = "http://127.0.0.1/whm-server-status"

########################################
# Stop configuring here.

timestamp = time.strftime("%Y-%m-%d_%T")
logfile = file(rootpath+"/logs/%s.log" % timestamp,"w")

oldstdout = sys.stdout
sys.stdout = logfile

def get_apache_status():
  url1 = serverstatusurl + "?auto"
  url2 = serverstatusurl
  data1 = urllib2.urlopen(url1).read()
  data2 = urllib2.urlopen(url2).read()

  file(rootpath+"/whm-server-status/%s.log" % timestamp,'w').write(data1)
  file(rootpath+"/whm-server-status/%s.html" % timestamp,'w').write(data2)
  return data1

def get_mysql_status():
  mysqlprocs = os.popen('mysql -q -e "show processlist"').read()
  mysqlprocsfull = os.popen('mysql -q -e "show full processlist"').read()
  file(rootpath+"/mysql/%s.processlist" % timestamp,"w").write(mysqlprocs)
  file(rootpath+"/mysql/%s.processlist-full" % timestamp,"w").write(mysqlprocsfull)
  return mysqlprocs

def get_process_list():
  procs = os.popen('ps auxwwwf').read()
  file(rootpath+"/processes/%s.procs" % timestamp, "w").write(procs)
  return procs

def get_iostat():
  iostat = os.popen('iostat -x').read()
  file(rootpath+"/iostat/%s.iostat" % timestamp,"w").write(iostat)
  return iostat
  

loadavg = file("/proc/loadavg").read().split()
one,five,fifteen = map(float,loadavg[:3])

apache_status = get_apache_status()
mysqlprocs = get_mysql_status()
processlist = get_process_list()
iostat = get_iostat()

if one > 10 or '--force' in sys.argv:
  print "Load average: %s" % ' '.join(loadavg)
  print 
  print "Apache:"
  print apache_status
  print 
  print "Mysql:"
  print mysqlprocs
  print
  print "Processes:"
  print processlist
  print
  print "iostat:"
  print iostat
  print