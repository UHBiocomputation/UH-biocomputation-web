SOP for administrators
#######################
:author: Ankur Sinha
:date: 2015-09-19 11:26:14
:status: hidden
:slug: 07-SOP-admins

Introduction
-------------

This purpose of this page is to document the steps required to update the UHBiocomputation website.  The steps here apply only to users that have write access to the repository. `There is a different SOP document for non admins <{filename}../pages/08-SOP-nonadmins.rst>`_. The website is generated using a Python tool called Pelican_ which converts the source files into HTML files with the required template design and so on. The sources are kept in the `Github repository`_ so that:

.. _Pelican: http://docs.getpelican.com/en/3.6.3/quickstart.html
.. _Github repository: https://github.com/UHBiocomputation/UH-biocomputation-web

- They are backed up.
- Any errors can be easily rolled back.
- They are easily accessible to anyyou that may need to modify them.
- Non administrators that would like to make modifications can make them without the admins having to actively do all the work.
 
Since Pelican is written in Python, it can be installed on all operating systems. It is easiest on Linux where it can generally be installed using the distribution's package manager:

.. code:: bash

    $ sudo dnf install python-pelican #On Fedora
    $ sudo apt-get install pelican #On Ubuntu variants

If it isn't available on your platform, it can be installed using the pip utility:

.. code:: bash

    $ pip install pelican #If unavailable using the package manager

`More information on installing Pelican can be found here`_.

.. _More information on installing Pelican can be found here: http://docs.getpelican.com/en/3.1.1/getting_started.html

You will also need Git installed to get the sources. On Linux variants, Git is available using the default package managers.

.. code:: bash

    $ sudo dnf install git-all #On Fedora
    $ sudo apt-get install git #On Ubuntu variants.

Git can also be installed on Windows and Mac systems using the `installers available here`_.  The default Git installation provides gitk, but there are `other graphical clients available for install too`_.

To publish using FTP, the Makefile uses the lftp command. This can also be installed on Linux systems quite easily:

.. code:: bash

    $ sudo dnf install lftp #On Fedora
    $ sudo apt-get install lftp #On Ubuntu variants.

Filezilla_ is an excellent graphical FTP application that can also be used.

.. _installers available here: https://git-scm.com/downloads
.. _other graphical clients available for install too: https://git-scm.com/downloads/guis
.. _Filezilla: https://filezilla-project.org/download.php?show_all=1

There are three simple steps required to make updates to the website:

- Get the sources and make the changes.
- Preview, confirm and commit.
- Generate the final pages and push to hosting.

Get the sources and make the changes
-------------------------------------

The sources are plain text files which can be either written in markdown_ or `restructured text`_ using your favourite text editor on your favourite operating system. If you haven't already cloned the repository, you will need to do so:

.. code:: bash

    $ git clone --recursive git@github.com:UHBiocomputation/UH-biocomputation-web.git

The recursive flag is required so that you also clone the pelican-plugins submodule.
If you already have a clone of the repository, please make sure it is up to date with the latest commits (other people may have made commits too):

.. code:: bash

    $ cd ~/website #wherever your clone resides
    $ git pull
    $ git submodule foreach git pull origin master
    $ git submodule foreach git checkout master

The directory structure of the sources is as follows:

.. code:: bash

    [asinha@ankur  UH-biocomputation-web(master %=)]$ tree -d -L 2
    .
    ├── content
    │   ├── files
    │   ├── images
    │   └── pages
    ├── output
    ├── pelican-plugins
    └── pelican-theme-gum
        ├── static
        └── templates

- **All the source files are stored in the content directory**. Posts in Pelican are divided into two categories: blogs and static pages. All the pages in the site header are static pages. These reside in content/pages. The posts that make up the "news" section are blog posts and go straight in the content directory. Various images and files that are linked to in either pages or posts go into their respective folders.
- **The generated output files go in the output directory**. The contents of this directory are then uploaded to our hosting webspace and constitute the actual website.
- **The pelican-theme-gum directory holds the theme template and css files for the site**. Again, unless tinkering with the theme, you need not touch this directory at all.
- The pelican-plugins directory is a git repository in itself. Most of the time, you will not deal with this directory at all. We only use the tag_cloud plugin. The commands mentioned enough will correctly clone this directory.

Once you've cloned the repository, make your changes and save them.
**Note**: Changes can be made to files using the Github web interface also. However, to run pelican, preview changes, and then generate the final website, you have to download the sources anyway.

Preview, confirm and commit
----------------------------

The Pelican Makefile has the commands required to preview and publish the website.

Once the required changes have been made and the file saved, preview the website to confirm that everything works as expected. To do this, in the main directory where the Makefile resides, run:

.. code:: bash

    $ make html
    Pelican /home/asinha/Documents/02_Code/00_repos/others/UHBiocomputation/UH-biocomputation-web/content -o /home/asinha/Documents/02_Code/00_repos/others/UHBiocomputation/UH-biocomputation-web/output -s /home/asinha/Documents/02_Code/00_repos/others/UHBiocomputation/UH-biocomputation-web/pelicanconf.py
    Dyou: Processed 4 articles, 0 drafts, 5 pages and 7 hidden pages in 1.04 seconds.

If this command completes without errors, preview the website:

.. code:: bash

    $ make serve 

This sets up a local server that serves the website at `localhost\:8000`_ so that you can preview your changes. To stop this server, hit Ctrl + C. If everything is OK, you can commit your changes:

.. code:: bash

    $ git add .
    $ git commit -m "A sensible commit message."
    $ git push -u origin master

Generate the final pages and push to hosting.
---------------------------------------------

The last step is to generate the final version and upload the site to the webhosting location. If ftp access is available, this can be dyou with you command:

.. code:: bash

    $ make ftp_upload #runs make publish for you

The Makefile already contains the required details. The command will ask you for the ftp password and do the rest. When it finishes uploading, your site should be up to date.

Merging pull requests
----------------------

Non admins can open pull requests as documented in the nonadmin SOP document. Admins only need to review the proposed changes, merge them if they're OK and then republish the website. This saves the admins from doing all the writing work required to update the website.

Pull requests that have been correctly created do not require anything other than a button click. They will specify that the pull request was made correctly and that the merge can be made without issues as shown in the figure below:

.. image:: {filename}/images/github-merge-pull-request.png
    :target: {filename}/images/github-merge-pull-request.png
    :alt: Open a pull request.

However, an admin should generally check that the changes made in the pull request are all correct. For small changes, you can just click on the "**Files changed**" tab and verify the changes. If they're OK, you can merge the pull request right away. For larger changes, you will have to checkout the person's branch, test the changes and then merge the request. The instructions to do this can be seen by clicking the "command line instructions" link in the merge ticket.

Once you've merged the pull request, the copy of the repository on your local system will need to be updated, the site regenerated, and uploaded. This should generally be as simple as:

.. code:: bash

    $ cd website-directory
    $ git pull origin master #this will pull the latest commits that you or others have merged or made
    $ make html; make serve #Again check that everything is OK by going to localhost:8000
    $ make ftp_upload #If everything is correct, upload the lastest version.


That should be it!


.. _markdown: http://daringfireball.net/projects/markdown/
.. _restructured text: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _localhost\:8000: http://localhost:8000

.. |br| raw:: html

    <br />
