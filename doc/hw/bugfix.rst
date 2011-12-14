Homework - Bugfix
=================

Real learning in computing comes more from doing and less from studying.
Debugging, figuring out how some software works and how it doesn't, is an
interactive process that develops basic engineering practices and, in the open
source context, community engagement and collaboration.

Pick a Project
--------------

You can choose any project you like.  The best to pick is something you *already
use*, something with which you're already familiar.  If you can't think of any
projects to investigate off the top of your head, here's a list of suggestions.

 - The `Battle for Wesnoth <http://www.wesnoth.org/>`_
 - `js.io <https://github.com/gameclosure/js.io>`_
 - The Linux Kernel (`bugzilla is down
   <http://comments.gmane.org/gmane.linux.kernel/1209650>`_, you could try
   `looking here
   <https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&version=rawhide&component=kernel>`_
 - `liveusb-creator <https://fedorahosted.org/liveusb-creator/>`_
 - The `Mozilla Project <https://bugzilla.mozilla.org/>`_
 - `node.js <http://nodejs.org/>`_
 - `pandas <http://github.com/wesm/pandas>`_, a data manipulation library
 - `Pyramid (web framework) <http://docs.pylonsproject.org/>`_
 - `Toscawidgets 2 (web widgets)
   <http://tw2core.readthedocs.org/en/latest/index.html>`_
 - `Turbogears 2 (web framework) <http://turbogears.org/>`_
 - The `Ur-Quan Masters <http://sc2.sourceforge.net/>`_
 - The `ManaWorld MMORPG for Linux <http://mantis.themanaworld.org/my_view_page.php>`_

A little more focused, here is a list of open source javascript/html5 game
engines and links to their bug trackers.

 - `gameQuery <https://github.com/onaluf/gameQuery/issues>`_
 - `limeJS <https://github.com/digitalfruit/limejs/issues>`_
 - `melonJS <https://github.com/obiot/melonJS/issues>`_
 - `akihabara <https://github.com/kesiev/akihabara/issues>`_
 - `effect <https://github.com/jhuckaby/Effect-Games/issues>`_

You might also find something neat over at bounty sites like:

 - Gun.io `<http://gun.io/>`_

Really, the sky is the limit here.

.. note:: For background, you might want to also check out the project on
   http://ohloh.net/.  It can help you characterize what kind of community
   orbits around your choice.

Find a bug
----------

A bug can be anything: an unintended side-effect in a low-level routine, a
user-interface cleanup, a feature enhancement, grammatical errors or lack of
clarity in the project's documentation.

Broadly, you have two different options here.  You can

 - Find a known bug (or feature enhancement) listed in the project's bug
   tracker.
 - Find a bug yourself by using the software.

In the event of the second case, make sure you file the bug in the project's
tracker before proceeding.

OpenHatch.org
~~~~~~~~~~~~~

OpenHatch.org bills itself as an "Open source Involvement Engine." It's mission
is *explicitly* to reach out to communities of developers just like the one in
this very course, and make it trivial for new contributors to effectively cycle
on upstream projects!

You can read more about OpenHatch and it's vision `here on their wiki <https://openhatch.org/wiki/About_OpenHatch>`_

For this homework assignment, you should check out:

 - `OpenHatch <http://openhatch.org>`_, particularly
 - The OpenHatch Volunteer Opportunity Finder for `Bite-sized Bugs <http://openhatch.org/search/?toughness=bitesize>`_
 - If you want *all* the bugs, you can find them through `OpenHatch's Search <http://openhatch.org/search>`_


Use the Source, Luke
--------------------

Once you've identified a bug that needs fixing, you'll need to get ahold of the
source.  In most cases, the code for a project will be hosted on a forge and the
process of forking and cloning the source will be straightforward.   If you
forget how to do this for `github <http://github.com>`_, you can refer to
:doc:`fflight`.

For whatever project you've chosen, you should ask that project's community for
help.  Look for `IRC` channels and project mailing lists.  You'll be
communicating with developers who have a lot on their plate so make sure to `be
polite and leave your ego at the door
<http://maymay.net/blog/2009/02/11/how-to-start-contributing-to-open-source-projects/>`_.

Find the code related to the bug; use whatever code navigation tools you're
more familiar with.  The instructor's favorite method is:  ``grep -inr "some
string" project_src/``.

Fix the bug, this may require some thinking, and some more asking around.

Test your fix!  Project maintainers hate nothing more than receiving a patch
that breaks every other function of the project.  Often, projects have built-in
test suites.  If yours does, run it!

Prepare your patch with descriptive commit messages.  Follow the method for
submitting patches recommended by your project and submit!

Make sure the project community can easily understand what you did and
why you did it.

Make sure there is a reference in the tracked bug ticket to your patch (that is,
if the project maintains a bug tracker).

The Deliverable
---------------

Write a blog post about this process and provide relevant links where
possible to documentation.

 - A link to the patch(es) hosted somewhere on the web, usually forges provide
   the ability to link to changesets.
 - A link to any mailing list discussions archived on the web
 - Snippets of any relevant IRC conversations.

You will be graded on your post and the explanation of your process.  Extra
kudos (but not extra credit) for super epic patches.

An Afterthought (not required)
------------------------------

Once your patch has been accepted, mosey on over to http://ohloh.net.

 - Create an account
 - Find the project you patched

   - If it doesn't exist, you can add it yourself

 - "Claim your position" as the author of the commit(s) you sent in to increase
   your rank among open source developers of the world!
