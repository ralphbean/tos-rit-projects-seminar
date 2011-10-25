Syllabus
========

Projects Seminar in FLOSS Game Development
------------------------------------------

 - Instructor - Ralph Bean <rjbpop@rit.edu>
 - Time/Location - TBD
 - IRC - irc.freenode.net, #floss-seminar
 - Course web page? - TBD
 - Email list - `floss-seminar@lists.rit.edu
   <https://lists.rit.edu/mailman/listinfo.cgi/floss-seminar>`_
 - Wiki? - TBD
 - The source for this syllabus can be found at
   http://github.com/ralphbean/rit-tos-projects-seminar

Goals of the course
---------------------


Having taken this course, students should be able to:

 - Demonstrate competence with modern FLOSS development tools and conventions
   (git, public forges, unit tests, bug trackers, wikis, etc..).
 - Demonstrate competence with modern web development technologies (HTML5,
   Javascript, CoffeeScript, CSS3, etc..).
 - Document their work progress, accomplishments, and pitfalls by way of weekly
   blog posts.
 - Work with and contribute to existing open source projects.
 - Build and manage a new project using open source tools.
 - Deploy a web application to the `cloud <http://rhcloud.com>`_.
 - Have a fun, open-source web-based game for their portfolio and/or to show
   off to their friends.

The spirit of the course
------------------------

While still a course where you will receive a letter grade, the spirit of the
course is intended to be both `open` and `fun`.  This is a seminar course,
so an experimental approach will be taken.

An `open` course -- students will have access to the 'document source' for the
syllabus and grading rubric.  While you are reading `the syllabus` right now,
as a student of the class you have a right to `fork the upstream repository
<http://github.com/ralphbean/tos-rit-projects-seminar>`_, make modifications,
and submit patches for review.  Barring a troll festival, this can create a fun,
dynamic environment in which the course curriculum can develop by the very same
mechanism being taught during the quarter (community-driven).

A `fun` course -- while the primary deliverable for the course is a working
web-based game, we are going to subject the course itself to `gamification`.
Instead of grading students' final projects individually, projects will be
pitted against one another through a scheme developed by the students
themselves, called the :doc:`final_project_rubric`.

For example, one way this could work is through simple accumulation of weighted
point values awarded for the presence of certain features: a game that works in
all modern browsers as well as on mobile devices gets +5 points, a game that
includes a velociraptor gets +3 points, etc...

Licensing
---------

All code developed by students in the course must be licensed (by the student)
under any one of the `licenses approved by the open source initiative
<http://www.opensource.org/licenses/category>`_.

Your code that you write is your code, with which you can do what you will;
true.  However, if you're unwilling to license code you write for an open source
course with an open source license, you're in the wrong course.

Schedule
--------

+----+---+----------------------------+-------------------+-------------------+
|Week|Day|Topic                       | Assigned          | Due               |
+----+---+----------------------------+-------------------+-------------------+
|1   |1  | Introductions, Syllabus,   |:doc:`hw/fflight`  |                   |
|    |   | Mailman, IRC, git, github  |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Bugfix deep dive           |:doc:`hw/bugfix`   |                   |
+----+---+----------------------------+-------------------+-------------------+
|2   |1  | Casual Games: Matching,    |                   |:doc:`hw/fflight`  |
|    |   | Sorting, and Seeking       |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Introduction to HTML5      |:doc:`program/1`   |                   |
+----+---+----------------------------+-------------------+-------------------+
|3   |1  | Casual Games: Managing,    |                   |:doc:`hw/bugfix`   |
|    |   | Hitting, and Chaining      |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Audio, WebWorkers, and     |:doc:`hw/rubric`   |:doc:`program/1`   |
|    |   | CoffeeScript               |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|4   |1  | Casual Games: Constructing,|:doc:`hw/review`   |                   |
|    |   | Socializing, and Physics   |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Server choices, Social     |:doc:`program/2`   |                   |
|    |   | APIs, and `le Cloud`.      |                   |                   |
|    |   | (#openshift)               |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|5   |1  | Paper Prototypes           |                   |:doc:`hw/review`   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Paper Prototypes           |                   |:doc:`program/2`   |
+----+---+----------------------------+-------------------+-------------------+
|6   |1  | Rubric Discussion          |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Rubric Discussion          |                   |:doc:`hw/rubric`   |
+----+---+----------------------------+-------------------+-------------------+
|7   |1  | Guest Lecture - TBD        |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Guest Lecture - TBD        |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|8   |1  | Progress Reports           |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Progress Reports           |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|9   |1  | Progress Reports           |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Progress Reports           |                   |                   |
+----+---+----------------------------+-------------------+-------------------+
|10  |1  | Final Demos                |                   |                   |
+    +---+----------------------------+-------------------+-------------------+
|    |2  | Finals Demos, Wrap-up      |                   |                   |
|    |   | Discussion                 |                   |                   |
+----+---+----------------------------+-------------------+-------------------+

Grading
-------

Your final grade for the quarter will be derived from the following weights.

+--------------------------------------------------------+--------------+
| Component                                              | Weight       |
+========================================================+==============+
|In-Class Participation                                  | 10%          |
+--------------------------------------------------------+--------------+
|FLOSS Dev Practices (Blogging, patching, writing, IRC)  | 15%          |
+--------------------------------------------------------+--------------+
|Homework Assignments                                    | 10%          |
+--------------------------------------------------------+--------------+
|Programming Assignments                                 | 15%          |
+--------------------------------------------------------+--------------+
|Paper Prototype                                         | 10%          |
+--------------------------------------------------------+--------------+
|Final Project                                           | 40%          |
+--------------------------------------------------------+--------------+

----

*Class partitipation* is speaking in class, answering questions, etc...

----

*Blog updates* -- students are required to keep a blog to which they post updates
about their investigations, progress, success, and pitfalls.  This blog can be
hosted anywhere, but must be added to the course `planet
<http://planet.teachingopensource.org/>`_.

 - You must make at least one blog post per week to receive full credit.
 - You must participate regularly in the course's IRC channel: asking and
   answering questions.
 - You must participate in the course's mailman list,
   `floss-seminar@lists.rit.edu
   <https://lists.rit.edu/mailman/listinfo.cgi/floss-seminar>`_.
 - Contributions to the course curriculum, syllabus, and rubric are factored in
   here as well.

.. TODO -- setup and add a link to a real planet.  Should students submit to
   big-planet-in-the-sky for teaching open source, as well?

----

The *homework assignments* are listed in the syllabus.  You will be able to
complete some of these in class.

----

*Programming assignments* are more in depth, but will amount to two deliverables
derived from one of the course's two textbooks, `Making Isometric Social
Real-Time Games with HTML5, CSS3, and Javascript
<http://www.amazon.com/Making-Isometric-Real-Time-JavaScript-ebook/dp/B005KOJ4DK/ref=dp_kinw_strp_1?ie=UTF8&m=AG56TWVU5XWC2>`_.

.. TODO -- add links to those two assignments

----

Students' *paper prototypes* are presentations to the rest of the class on their
idea for their game, *before a single line of code is written*.  You will
be graded on preparation and presentation.

.. note : these are 'play session'.  grade based on students notes on their own
   evaluation

----

Your *final project* will be the culmination of the quarter's work and will be
graded according to the :doc:`final_project_rubric`.

Lightning Talks - Extra Credit
------------------------------

Every Tuesday for the first portion of class, any student has the opportunity
to give a `lightning talk <http://en.wikipedia.org/wiki/Lightning_Talk>` on a
topic of their chosing.  Your lightning talk must be less than 5 minutes in
length and must be at least remotely related to the course material.

You will receive +1 extra credit points towards your final grade for every
lightning talk you give.  Only the first three lightning talks offered will be
allowed during a given class.  Talks will be chosen from among those offered by
students on a FIFO basis.
