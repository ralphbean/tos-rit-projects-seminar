Tools for teaching the open source projects seminar @ RIT
=========================================================

This is an all-purpose repository for storing some content, but mostly tools for
teaching the open source projects seminar @ RIT.

Future tools could include things like scripts to produce blog/commit/unittest
statistics.  This is also a place the syllabus could live, where students could
fork and produce pull requests.

Building the Documentation
--------------------------

To build the documentation, you'll need to have
`Sphinx <http://sphinx.pocoo.org/>`_ installed as well as the ``cloud``
sphinx theme.

 $ virtualenv --no-site-packages ~/sphinxenv
 $ source ~/sphinxenv/bin/activate
 $ pip install sphinx
 $ pip install cloud_sptheme

In the root directory, simply run::

 $ sphinx-build -b html doc html-output

The html documentation will be generated (obviously) in ``html-output/``.  Check
``html-output/index.html`` to see if it exists.

