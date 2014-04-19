Title: Getting Python working in your environment (Running)
Slug: running-python
Status: draft
Date: 2014-04-25 15:30

Depending on what operating system you're working on, Python installation is a little different.  Additionally, using Python on each of these OS platforms is a little different.

Getting on my soapbox, I will say this; I work in all three of these environments and I vastly prefer to write Python in Linux, preferably a distribution that is widely used and common (Ubuntu/Debian or CentOS).  If you are working on OSX or Windows, it might be worth learning how to use a Virtual Machine.  VirtualBox is free and works on OSX and Windows.  VMWare is a popular option, but typically requires a license (though some educational institutions have institution licenses).

# OSX

For many years now, OSX has come with Python pre-installed.  Open up Terminal type in the following:

```
rweiss$ which python
/usr/bin/python
```

So the executable that is called by your system when you call `python` at the Terminal command line is located at `/usr/bin/python`.  And you can tell what version of Python is installed on your machine.  

```
rweiss$ python --version
Python 2.7.2
```

Your version will depend on a variety of factors such as your OSX version or how often you update your software, so I'm not going to pretend I can guess what is most common.  If you are running a version less than 2.6, you will probably run into problems; a lot of the 3rd-party modules that other people develop for Python that are really super useful expect that you have 2.6+ installed.

You should probably know, however, that there might be more than one version of Python on your machine.  You can check this with the following:

```
rweiss$ ls /usr/bin/python*
/usr/bin/python			
/usr/bin/python2.5-config	
/usr/bin/python2.7		
/usr/bin/pythonw2.5
/usr/bin/python-config		
/usr/bin/python2.6		
/usr/bin/python2.7-config	
/usr/bin/pythonw2.6
/usr/bin/python2.5		
/usr/bin/python2.6-config	
/usr/bin/pythonw		
/usr/bin/pythonw2.7
```

How does your machine know which one of these to use when you call `python`?  Without getting too deep into filesystems, all we need to know is that OSX has mapped `/usr/bin/python` to `/usr/bin/python2.7` through a _symbolic link_.  Similarly, `/usr/bin/python2.7` is a _symbolic link_ to another location

```
rweiss$ ls -lha /usr/bin/python2.7*
lrwxr-xr-x  1 root  wheel    75B Mar 12  2013 /usr/bin/python2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7
lrwxr-xr-x  1 root  wheel    82B Mar 12  2013 /usr/bin/python2.7-config -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7-config
```

And the actual `python` executable is located in that directory, which is `/System/Library/Frameworks/Python.framework/Versions/2.7/bin/` on my machine.


# Windows

# Linux

# Other useful Python distributions