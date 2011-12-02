What is RegMan?
===============
It's our very own, ridiculously basic registration manager!

It assumes that a registration page should be structured as follows:
-  *Greeting*: paragraph saying hi to everyone!
-  *Question Matrix*: table of checkboxes where selecting 'checkbox[i][j]' means
   you agree with 'line_option[i]' and 'column_option[j]'
-  *Profile*: a couple of forms to fill out about your background
-  *Contact*: email address and possibly phone number or whatever you want...
   these should be validated with at least an embarassingly basic regex
-  *Followup*: follow up paragraph, for now, our e-mail address!

Configuration
-------------
Tweak 'regconf.py' and notice the effects that has on 'static/index.html', the
template that the form is generated from. There are a couple of basic configs
already for the sake of it.

Installation
------------
RegMan is a Flask (Python) application. You'll need to install Flask somehow
(easy_install/pip?) and then run:
    python regman.py
It will autoreload if you modify the Python files.

