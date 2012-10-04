WEBFORGE
========

Simple HTTP protocole request forgery for analysing server headers returning.

The concept
-----------

The idea is to provide a tools for forgery our own http request manually, with parameters configuration,
http method, headers, cookies, and all the element of http protocole for testing and analysing the return.
He can help you in case of AJAX development.

Development philosophy
----------------------

The guideline development is to use a Python software standalone without external third party.
Only use a Python standard library for build it.
That provide an apps portability facility.

Development patterns
--------------------

UI is build on the MVC pattern and all models is observable, inspired from ToyMVC.
All elements of the build is uncouple, the greater part of models that represents http particularity (header, POST and GET params, methods) element
is singleton.
I integrate some tkinter add on from http://tkinter.unpythonic.net/wiki/ for extand fonctionality.

Particularity
-------------

I've create this project for testing more deeply Python and the Pythoning particularity.
Core request is not totaly implemented, i work on actually.
This not a professional apps, i work on me free time, the progress of this apps is not fast.
More bug can live in.

Compatibility
-------------

* Python2.7.2 (not functionnal) Somes errors occurs in import package version
* Python3.2

Possibly compliance with python3.3 but no test doing
If you can, test it on other version and report to me.

Usage
-----

    python3.2 main.py 

Guideline for future
--------------------

04 octobers 2012 :

+ Adding in main content tabs system to looking for http server logs files, and showing http request content download.
+ Adding unit test.
+ Handle view who representing table (http parameters, http headers) with the same controler.
+ Full english for all comments.
+ Complete lazy comments.
+ Adding system to initialize all components with ini files (example : starting from http trace to replay it)

Reference
---------
* http://tkinter.unpythonic.net/wiki/
* http://docs.python.org/library/
