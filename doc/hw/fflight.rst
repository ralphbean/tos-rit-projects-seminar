Homework - First Flight
=======================

The purpose of this homework assignment is to introduce students to their first
FLOSS practices.  Read it in full, there are a number of graded deliverables.

The due-date is listed in the :doc:`../syllabus`.

Fill out the survey
-------------------

*Tasks*:
  - Your first task is to fill out the survey located here:
    https://clipboard.rit.edu/take.cfm?sid=E958FABE

It's anonymous, but the results will be published back to the whole class so we
have a feel for the technical level and preferences coming into the course.

IRC
---

`IRC <http://en.wikipedia.org/wiki/Internet_Relay_Chat>`_ is one of the primary
means of communication for a `FLOSS
<http://en.wikipedia.org/wiki/Free_and_open_source_software>`_ community,
particularly for `informal` communication.

There is a course `IRC` channel on irc.freenode.net.  The channel is
``#floss-seminar``.  Communicating regularly in `IRC` factors into the `FLOSS
Dev Practices` component of your final grade.

*Tasks*:
 - Download and install an IRC client on your development machine.

   - Windows: `mIRC <http://www.mirc.com/>`_
   - Mac OS X: `Colloquy <http://colloquy.info/>`_
   - Linux: `irssi <http://irssi.org/>`_

 - Choose a nick and `register yourself with the NickServ
   <http://freenode.net/faq.shtml#userregistration>`_.
 - Connect to ``#floss-seminar`` and introduce yourself.

   - The instructor's nick is ``threebean``.

It is a good practice to "hang out" in IRC channels of projects that you use and
especially of projects that you contribute to.  Here you can find early alerts
regarding any upcoming major changes or security vulnerabilities.  It is also
the easiest (lowest overhead) method for getting your questions answered.

.. note:: Only for the brave -- if you want to be completely awesome, you can
   setup a proxy node so you are always logged in.  People can leave you
   messages this way.

   If you want to be completely completely awesome, you can setup `BitlBee
   <http://www.bitlbee.org/main.php/news.r.html>`_ so you can tweet from your
   IRC client.

Mailman
-------

`Discussion mailing lists
<http://en.wikipedia.org/wiki/Electronic_mailing_list>`_ are a more formal
mechanism of communication for FLOSS projects.  More formal than `IRC`, less
formal than bug trackers.  Discussion mailing lists are often used to ask
questions, announce upcoming releases and beta tests, and to debate redesigns
and refactors.  The advantage here is that mailing lists are typically archived
and indexed by Google; discussions that should be preserved for posterity should
occur here.

There is a `GNU Mailman <http://en.wikipedia.org/wiki/GNU_Mailman>`_
discussion list for the course hosted by RIT.

*Tasks*:
 - Subscribe to it at https://lists.rit.edu/mailman/listinfo.cgi/floss-seminar
 - Write your first email to floss-seminar@lists.rit.edu, introducing yourself.
   Include your name, major, hometown, and favorite color.

Communicating regularly over the course `mailman` list (asking and/or answering
questions) factors into the `FLOSS Dev Practices` component of your final grade.

Blogging
--------

Setup a blog if you don't have one.  Much like mailing lists, blogs are
archived, indexed by Google, and therefore preserved for posterity.  When you
encounter a technical challenge, typically you google for a solution and you
typically find that solution in a blog post of some developer who has run into
a similar situation.  Blogging about your attempts, successes and failures
(and writing tutorials!) is a best practice for increasing the general body of
searchable knowledge available.

Blogs around a topic are also typically aggregated by a `planet
<http://en.wikipedia.org/wiki/Planet_(software)>` (an RSS feed aggregator).
This way, all developers blogging about ``Project X`` can have their blog posts
fast-tracked to a readership subscribed to ``Planet X``.  For instance, here's a
link to `Planet Python <http://planet.python.org/>`_.

The Planet for the course is hosted at http://threebean.org/floss-planet/.
There are instructions for how to subscribe your blog to it in the `Patch the
Course Project` section below.

You must create a blog (if you don't have one already) and write at least one
post per week about your progress, attempts, successes, failures, reflections,
and/or all of the above.

*Tasks*:
 - Create a blog if you don't already have one.  There are lots of free services
   available.  You might try http://wordpress.com or http://blogspot.com.
 - Write an introductory post relevant to the course.  The topic is your choice!

github
------

Code `forges` are service sites around which FLOSS development orbits, some of
the more popular sites are `github <http://github.com>`_, `bitbucket
<http://bitbucket.org>`_, `sourceforge <http://sourceforge.net/>`_, and
`launchpad <https://launchpad.net/>`_.

For your own enlightenment, review the following comparisons of the different
forges:

 - `Timeline <http://flossmole.org/content/when-were-forges-established>`_
 - `Metadata
   <http://flossmole.org/content/project-metadata-matrix-june-2011>`_
 - `Artifacts
   <http://flossmole.org/content/artifacts-matrix-code-forges-june-2011>`_
 - `Features
   <http://flossmole.org/content/feature-matrix-code-forges-june-2011>`_
 - `Revision control
   <http://flossmole.org/content/revision-control-matrix-june-2011>`_
 - `Policies <http://flossmole.org/content/forge-policy-matrix-june-2011>`_

You'll need to create your own account on github.com.  All development for this
course should be tracked on that forge.  Github is, after all, `the most popular
forge <https://github.com/blog/865-github-dominates-the-forges>`_.

*Tasks*:
 - Create a `github <http://github.com>`_ account if you don't already have one.

Patch the Course Project
------------------------

Check out the source repository for this course; it's hosted at
https://github.com/ralphbean/tos-rit-projects-seminar.

Inside the repository, we'll keep an index of all the students in the course and
metadata about them (you!).

*Tasks*:
 - Work through this `git tutorial <http://gitimmersion.com/index.html>`_ if you
   don't have any experience with git.
 - Fork `the repository
   <https://github.com/ralphbean/tos-rit-projects-seminar>`_ (link to
   `github help <http://help.github.com/fork-a-repo/>`_ on this).
 - Clone a local copy.
 - Follow the instructions in ``README.rst`` to setup your environment.
 - Edit the file ``data/students.yaml``.  Perhaps obviously, it is
   a `YAML <http://www.yaml.org/>`_ file.  Add yourself to the file with the
   necessary keywords.
 - Verify that you added yourself correctly by running the script located at
   ``lib/ritfloss/model/validate.py``
 - Edit the file ``planet/config.ini``.  Look at the very bottom of the file and
   there will be the beginnings of a list of subscribed blogs.  Add your blog's
   RSS feed (or a topical sub-feed) to this list.  Make sure its a working RSS
   URL!  (Once the patch is accepted upstream and pushed to production, this
   should add your blog feed to the `course planet
   <http://threebean.org/floss-planet/>`_.)
 - If everything checks out, then

   - Commit your change
   - Push to your github repository
   - Issue a pull request through the web interface.


