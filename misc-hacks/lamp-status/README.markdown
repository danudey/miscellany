lamp_status
-----------

lamp_status is a simple Python script that I wrote to gather snapshots of
a LAMP server's overall condition. It gets the unix process list, the Apache
server-status data, disk I/O stats, MySQL process list, and load average.

Note that at the current time, it only works on Linux systems (due to a trivial
non-portable reliance on /proc/loadavg) with iostat installed.

USAGE
-----

    Usage:	lamp_status.py
    		lamp_status.py --force
    
    Options:
      --force   display output to stdout even if load is below 10
