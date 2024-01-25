Editing the Documentation
=========================

This lab manual has been created using the `Sphinx Document Generator
<https://www.sphinx-doc.org/en/master/index.html>`_. As such, all pages are
written using the `reStructuredText <https://docutils.sourceforge.io/rst.html>`_
format. Briefly, all files end in the :file:`.rst` extension, but are simple
text documents; you can edit them with any text editor.

======== =====================================
Platform Default Text Editor
======== =====================================
Windows  :program:`notepad`
OS X     :program:`TextEdit`
Linux    :program:`vi`, :program:`emacs`, etc.
======== =====================================

If you take a look at the top-right of this (and any other) page, you should see three
icons: (1) a download button, (2) a fullscreen button, and (3) a toggle for
light/dark mode. Clicking the download button will provide two options for
downloading a printable PDF or the original source rst file.

reStructuredText Format
-----------------------

The reStructuredText format may seem a little intimidating at first, but you'll
hopefully soon find how easy it is to edit because you don't have to worry about
formatting! To create a section header, you just need to write the title and
then "underline" it with a symbol::

    The Header of My Section
    ========================

I have most documents set to use ``===`` as the title of the page, ``+++`` as a
section, followed by ``---`` as a subsection. Every time you change to a new
symbol that has not been used before, Sphinx creates a new sub-/subsub-/etc.
section. 

When you want to start a paragraph, just leave an extra line of whitespace
between the paragraphs::

    This is the first paragraph of text and now it will be done.

    Here is the second paragraph of text.

Most likely, you will be editing procedures and so you may want to create an
enumerated (numbered) list. Numbered lists are as easy as typing the number,
followed by a period and space::

    1. The first step in a long procedure. I do have to
       keep my indents aligned so that this long text stays
       under number "1".
    2. And here's the second step.

Now, sometimes procedures will already have some numbered steps and you will
need to insert a step in between. You **do not** need to renumber all the steps
if you follow this trick: use a ``#.`` instead of the number to allow Sphinx to
automatically number the steps. The example above becomes::

    #. The first step in a long procedure. I do have to
       keep my indents aligned so that this long text stays
       under number "1".
    #. And here's the second step.

If you would like to include an image (let's say :file:`gcms-picture.jpg`), then
you can use the following structure::

    .. figure:: images/gcms-picture.jpg
       
       A caption about the figure

Note that the caption is indented so it lines up with the start of the word
``figure``. I include all images in an :file:`images/` subdirectory, so if you
submit a change with a picture, please use the above line as-is.

For additional details, please see the `ReStructuredText Primer
<https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_.

Tips on File Structure
----------------------

To maintain readability of the source, please do the following:

* Keep lines to about 80 characters. Note that some programs do not
  automatically wrap text for you, but this means a lot of scrolling. If the
  line is looking too long, press :kbd:`Return`/:kbd:`Enter` on your keyboard
  and start a new line.
* Don't readjust line breaks. In other words, if you need to insert a few new
  words or a new sentence, put them on a new line. As long as you don't put a
  blank space between sentences, you will still get 1 paragraph. For example::

    This will
    still output
    as a single sentence
    despite being
    many different lines.

  will still display as "\
  This will
  still output
  as a single sentence
  despite being
  many different lines.\
  "

Submitting Changes
------------------

Brightspace
~~~~~~~~~~~

The easiest (for you) method of editing and submitting changes to the
documentation would be to download the :file:`.rst` file for the page you would
like to change, make edits, and then upload them to Brightspace under the
appropriate category.

GitHub
~~~~~~

The source code is also hosted at `GitHub
<https://github.com/danian95/InstDocs>`_. GitHub allows collaborators to work on
documents together, but keeps track of every version that is ever "committed".
In other words, you can change a file and submit a "Pull Request" for me to pull
your changes into the source code. The benefit? You get credit within the
version control system for making the change.

This would be the easiest method for me to implement your changes, but I
understand that learning a new system (:program:`git`) may be a bit much. While
GitHub tries to make this easier by allowing you to edit the files in the
browser or through their `GitHub Desktop <https://desktop.github.com/>`_
software, you are not expected to use this (though you are certainly encouraged
to do so!).

To edit the documentation on GitHub,

#. Create an account at https://github.com. I recommend using your university
   email, especially if you do not plan on ever using GitHub again.
#. Fork the https://github.com/danian95/InstDocs repository so that you get your own version of
   the documentation.
#. Make changes to whatever file(s) you need to change and then "commit" those
   changes. You can edit the documentation using git a few different ways:

   a. Click the edit icon on the file you want to edit within your forked
      repository.
   b. Change the ``github.com`` in your address bar to ``github.dev`` to use
      GitHub's own web developer console. For example::

        https://github.com/danian95/InstDocs

      becomes::

        https://github.dev/danian95/InstDocs

   c. Use GitHub desktop to download the files to your computer and edit them
      there.
   d. Use :program:`git` in the command line to download the files to your
      computer and edit them there. (Advanced!)

   Once you have committed the changes, remember to "push" them back to your
   forked repository on GitHub!
#. Head to my https://github.com/danian95/InstDocs repository and open a "Pull Request". Bring
   in your changes into the Pull Request. After I review the changes, I will
   "merge" them with my repository.
