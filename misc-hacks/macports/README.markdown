Macports hacks
==============

libmemcached-0.25.14-portfile
-----------------------------

### Description

This is a portfile with an added variant to support Evan Weaver's forked
version of libmemcached, which is required to use version 0.14 of the
'memcached' rubygem.

You may also be interested in Evan Weaver's [blog post][bp] about it.

### Usage

Replace this file: 

[/opt/local/var/macports/sources/rsync.macports.org/release/ports/devel/libmemcached/][file]

With the contents of the portfile included. Once done, you can run this command:

`sudo port install libmemcached +evanweaver`

and it should download and install the custom version of the port.


[bp]: http://blog.evanweaver.com/articles/2009/01/24/secret-codes/
[file]: file:///opt/local/var/macports/sources/rsync.macports.org/release/ports/devel/libmemcached/