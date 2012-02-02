Notes for Class Sessions
========================

Week 01, Day 1:  First Flight
-----------------------------

 - Introductions
 - Covering the Syllabus
 - :doc:`hw/fflight`


Week 01, Day 2:  Guided Bugfix
------------------------------

 - Lightning Talks?
 - Review last class (:doc:`hw/fflight`)
 - Review Schedule (When are homeworks due, how are we with the reading
   schedule?)
 - Guided Deepdive into `pandas <http://github.com/wesm/pandas>`_
 - Talk about :doc:`hw/bugfix`

Week 02, Day 1:  Matching, Sorting, and Seeking
-----------------------------------------------

 - Graduate student proposals are due
 - :doc:`hw/fflight` is due.  How was it?

   - Review http://threebean.org/floss-planet

 - Slides - http://prezi.com/1qe6g-pvye_q/floss-games-matching-sorting-and-seeking/

Week 02, Day 2:  Introduction to HTML5
--------------------------------------

 - Lightning Talks
 - Introduction to HTML5

   - The book

     - clone from github -
       https://github.com/ralphbean/Making-Isometric-Real-time-Games
     - examples/ex2-fps-requestAnimationFrame.html
     - examples/ex13-isogrid-buildings.html
     - examples/ex14-gui.html

       - `Modernizr.js <http://www.modernizr.com/>`_

   - `jQuery <http://jquery.com/>`_
   - `spritely <http://spritely.net/>`_

     - Here's the `spritely source code <https://gist.github.com/1447119>`_

   - `DuckHunt <https://github.com/ralphbean/DuckHunt-JS>`_

 - Javascript Game Frameworks

   - gameQuery - http://gamequery.onaluf.org/
   - limeJS - http://badassjs.com/post/3200945950/limejs
   - melonJS - http://www.melonjs.org/
   - processingJS - http://processingjs.org/
   - akihabara - http://www.kesiev.com/akihabara/
   - effect - http://www.effectgames.com/effect/

 - :doc:`program/1`


Week 03, Day 1:  Managing, Hitting, and Chaining
------------------------------------------------

 - Managing

   - Diner Dash http://www.playfirst.com/game/dinerdash
   - Cake Mania http://www.bigfishgames.com/download-games/898/cakemania/index.html
   - Insaniquarium http://www.popcap.com/games/insaniquarium/web

     - Requires ActiveX

- Chaining

   - Revisit,

     - Diner Dash
     - Insaniquarium
     - Tetris
     - Scrabble

 - Hitting

   - Whac-a-mole vs Wii Tennis

Week 03, Day 2
--------------

Class was cancelled for the STEM/CSI hackathon!

Week 04, Day 1
--------------

 - Welcome back from break.
 - Homeworks due.  How'd it go?
 - Game Pitches

----

 - ``<audio>`` tags
 - WebWorkers
 - CoffeeScript

   - `Online interpreter
     <http://coffeescript.org/#try:%23%20Assignment%3A%0Anumber%20%20%20%3D%2042%0Aopposite%20%3D%20true%0A%0A%23%20Conditions%3A%0Anumber%20%3D%20-42%20if%20opposite%0A%0A%23%20Functions%3A%0Asquare%20%3D%20(x)%20-%3E%20x%20*%20x%0A%0A%23%20Arrays%3A%0Alist%20%3D%20%5B1%2C%202%2C%203%2C%204%2C%205%5D%0A%0A%23%20Objects%3A%0Amath%20%3D%0A%20%20root%3A%20%20%20Math.sqrt%0A%20%20square%3A%20square%0A%20%20cube%3A%20%20%20(x)%20-%3E%20x%20*%20square%20x%0A%0A%23%20Splats%3A%0Arace%20%3D%20(winner%2C%20runners...)%20-%3E%0A%20%20print%20winner%2C%20runners%0A%0A%23%20Existence%3A%0Aalert%20%22I%20knew%20it!%22%20if%20elvis%3F%0A%0A%23%20Array%20comprehensions%3A%0Acubes%20%3D%20(math.cube%20num%20for%20num%20in%20list)%0A>`_
   - Observations

     - Python style whitespacing
     - Ruby styled lightweight syntax
     - Concise function declarations
     - JSLint approved
     - Class based inheritance
     - Comprehensions!

   - `Hangman <https://github.com/ralphbean/hangman-coffee>`_

Week 04, Day 2 - Paper prototypes
---------------------------------

  - Paper prototypes

Week 05, Day 1 - Settling on projects
-------------------------------------

  - Paper prototypes revisited.
  - Decide on top three projects.
  - Votes -

    - How many per team?

      - 2 teams of 6
      - 3 teams of 4
      - 4 teams of 3

    - Which games?  `Vote on the clipboard site <https://clipboard.rit.edu/take.cfm?sid=77F39FB1>`_.

      - Rabenvald - Robocode++
      - kaeedo - Eco
      - PhilMoc - Haunted House
      - JaceTwice - Arrangamajig
      - Crystick - Gold Rush
      - LakeEffect - Helicopter Race
      - trose/decause - FOSS
      - Lo-Rin - Dragonfire + Maths
      - rossdylan - Pip3z!!1
      - Qalthos - Myst
      - Chips545 - Moar LaZ0rs

  - :doc:`hw/rubric` assigned.

Week 05, Day 2 - Openshift
--------------------------

 - Revisit last class

   - Teams and :doc:`hw/rubric`

 - Due homeworks

   - :doc:`hw/rubric` due next Thursday.
   - :doc:`program/2` due the Tuesday after that.

 - Class this coming Tuesday will be a working session on :doc:`program/2`.

 - Walk through :doc:`program/2`

Week 06, the Valley of the Shadow of Openshift
----------------------------------------------

:(

Week 07, Day 1:  TurboGears
---------------------------

Setting up your environment (on ``typhon.csh.rit.edu``)::

    $ virtualenv ~/myenv
    $ source ~/myenv/bin/activate
    $ pip install tg.devtools Pylons==1.0 WebOb==1.0.8
    $ paster quickstart roflapp

    # Yes you prefer mako templates
    # Yes you need authentication

    $ cd roflapp

At present, the current release of TurboGears doesn't know it, but it needs
 - Pylons==1.0
 - WebOb==1.0.8

::

    $ python setup.py develop
    $ paster setup-app development.ini

Since we're on a shared machine ``typhon.csh.rit.edu``, we'll need to pick different ports to serve our respective roflapps on.  Edit ``development.ini`` accordingly.

Once you've made your edits, serve your app with::

    $ paster serve --reload development.ini


Understanding Modern Web Frameworks
+++++++++++++++++++++++++++++++++++

It's all about MVC -- model, view, controller.  Modern frameworks separate your code out into these three distinct, yet interdependant chunks.

 - *model* (``rolfapp/model/*.py``) - contains all the database-related code
 - *view* (``roflapp/template/*.mak`` and ``roflapp/public/*``) - contains all the presentation-related code, html markup, css, javascript, etc.
 - *controller* (``roflapp/controllers/*.py``) - all the control-logic (or `business` logic).  Who can access what urls?  Validation of data?  Did you win an iPad?

If you look inside ``roflapp`` you'll see these directories and a few other secondary ones.

1) Add ``roflapp/public/testing123.html`` and browse to ``/testing123.html``.
2) Edit ``roflapp/templates/index.html`` and browse to ``/``.
3) Edit ``roflapp/controllers/root.py``.  Edit the ``def index(..)`` method to return a random number.  Display it in the template.
4) Look at ``roflapp/model/``.  Edit ``roflapp/controllers/root.py`` to return the number of users.
5) Throw an exception.
6) Use ``tg.flash()``.


Week 07, Day 2:  More TurboGears - AJAX - Back to the Cloud - Facebook
----------------------------------------------------------------------

1) Edit ``roflapp/controllers/root.py``.

   1.1) Add one method that JSON returns info about users.
   1.2) Add another method that JSON returns {'success': True} but adds a new user

2) Add ``roflapp/public/javascript/rofl.javascript``.

   1.1) Add one function that given JSON, updates the DOM.
   1.2) Add one function that queries the ``/query_users`` URL.
   1.3) Add one function that POSTs to create a random user.
   1.4) Add $(document).ready(..) to kick it all off.

Facebook, if we have time
+++++++++++++++++++++++++

1) Look at `hanginwit-threebean <http://github.com/ralphbean/hanginwit-threebean/>`_ for the example.  In particular, check out ``auth-fb.coffee``.
