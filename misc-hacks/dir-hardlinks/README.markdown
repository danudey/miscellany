Hardlink
--------

Hardlink is a simple script written in python to create directory
hardlinks on HFS+ filesystems on Mac OS X 10.5 or higher. It will
not work on any other OS, or on any other filesystem. It is also
most likely not backwards-compatible. On older OSes without hardlink
support, the hardlinks will show up as small (empty?) files, and be
inaccessible, but the original directory should still exist.

USAGE
-----

    Usage:	hardlink.py [-q] <dir1> <dir2>
    		hardlink.py [-q] -u <dir1> [<dir2> ...]
    
    Options:
      -h, --help    show this help message and exit
      -u, --unlink  remove a directory hardlink
      -q, --quiet   no output
    
Limitations
-----------

1. You cannot create a hardlink to a directory in the same location as
   the original. For example, you cannot link `/tmp/dir1` to `/tmp/dir2`,
   as you will get an error.
2. --unlink will only unlink a directory hardlink. It will not unlink
   files, and you cannot unlink a regular directory anyway. This is done
   to prevent any possible data loss from using this utility.
3. DO NOT USE `rm -rf` TO REMOVE A DIRECTORY HARDLINK. `rm` will enter into
   the directory, remove all the files in it, and only then remove the
   directory. This will ERASE YOUR FILES. YOU HAVE BEEN WARNED!
