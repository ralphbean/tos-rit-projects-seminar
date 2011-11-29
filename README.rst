Tools for teaching the open source projects seminar @ RIT
=========================================================

This is an all-purpose repository for storing some content, but mostly tools for
teaching the open source projects seminar @ RIT.

Future tools could include things like scripts to produce blog/commit/unittest
statistics.  This is also a place the syllabus could live, where students could
fork and produce pull requests.

Setting up your environment
---------------------------

Before you can do anything with this (build the documentation or run any of the
scripts) you'll need to setup and activate a python `virtualenv
<http://pypi.python.org/pypi/virtualenv>`_.  Run the following at the command
prompt::

 $ virtualenv --no-site-packages ~/sphinxenv # This creates it
 $ source ~/sphinxenv/bin/activate           # This activates it
 $ python setup.py develop                   # This will install packages to it

.. note::  This has only been tested on Linux, although it is definitely
   possible on Windows and OS X.  If you encounter problems setting up your
   virtualenv on any environment, please edit this file and add a GOTCHA.

Building the Documentation
--------------------------

Make sure you have your virtualenv activated.

Being certain of that, in the root directory, simply run::

 $ sphinx-build -b html doc html-output

The html documentation will be generated in ``html-output/``.  Check
``html-output/index.html`` to see if it exists.

