README.rst -- Tools for teaching the open source projects seminar @ RIT
=======================================================================

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
prompt...

On Linux/Mac OS X
+++++++++++++++++

::

 $ virtualenv --no-site-packages -p python2 sphinxenv
 $ source sphinxenv/bin/activate
 $ git clone git@github.com:YOUR_USERNAME/tos-rit-projects-seminar.git
 $ cd tos-rit-projects-seminar
 $ python setup.py develop

On Windows
++++++++++

At the windows command prompt::

 $ virtualenv --no-site-packages -p python2 sphinxenv
 $ sphinxenv/Scripts/activate.bat

In msysGit or git-bash::

 $ git clone git@github.com:YOUR_USERNAME/tos-rit-projects-seminar.git

Back in the windows command prompt::

 $ cd tos-rit-projects-seminar
 $ python setup.py develop


Building the "Documentation"
----------------------------

The "documentation" for the course (the syllabus, all the homework assignments,
notes on the lectures) are all kept in the ``doc/`` directory of this
repository.  The files all end with the extension ``.rst`` which is the file
extension for the `reStructuredText <http://sphinx.pocoo.org/rest.html>`_ markup
language.  They are all furthermore tied together the the `sphinx` framework for
building integrated docs.

You might notice that the syllabus, et. al. is hosted on
http://readthedocs.org/.  The `upstream github repository
<http://github.com/ralphbean/tos-rit-projects-seminar>`_ has a hook installed
that automatically triggers a ``git pull`` at http://readthedocs.org from
http://github.com.  Thus, every time we change the docs here, they are
automatically re-built into HTML for us and posted online.  Awesome!

This however means that we should be careful before we push anything to github,
or it will 'go live'.  To be careful, you should rebuild the documentation
locally (on your machine) to check that whatever modifications you made to the
``.rst`` files actually renders into the HTML that you want.

In order to do that, first make sure you have your virtualenv activated.

Being certain of that, in the root directory, simply run::

 $ sphinx-build -b html doc html-output

The html documentation will be generated in ``html-output/``.  Check
``html-output/html/index.html`` to see if it exists.

.. note:: If your machine complains that 'sphinx-build' is a command that could
   not be found, try running "$ python setup.py develop" in the root of the
   tos-rit-projects-seminar repository first.  That ``setup.py`` file contains
   information about all *other* open source projects that are *required* for
   this project, and will automatically install them from
   http://pypi.python.org/

Validating the ``data/students.yaml`` file
------------------------------------------

The ``data/students.yaml`` file is a structured data file that keeps track of
all the students in the class and metadata about them.  Using this file and the
bindings in ``lib/ritfloss/model/students.py`` we can build scripts that count
how many lines of code each student modifies each week, or how many
words/blogpost, or whatever we like.

The data format (`YAML <http://www.yaml.org/>`_) can be a little prickly though.
It is `whitespace-sensitive`, meaning that how many spaces you put before an
entry on each line has an impact on how the data is interpreted.  It also means
that tabs and spaces are distinctly different in their meaning.  It also means
that editing such a file is easy to mess up.

In order to ensure that you don't introduce any unparseable errors into the
file, there is a script in ``lib/ritfloss/model/validate.py`` that reads in the
file and checks each entry.  You should run it after every time you edit
``data/students.yaml``.

In order to run the ``validate.py`` script, make sure you have your
virtualenv activated.

In the root of the cloned source directory, run::

  $ python lib/ritfloss/model/validate.py
