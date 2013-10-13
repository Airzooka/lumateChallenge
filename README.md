Lumate Challenge
================
An implementation of a Lumate programming challenge, prepared and completed by Alexander Litty.

This is a Django-based website with a brief author's biography and simple guestbook. Digital signatures of the guestbook are stored in a database after passing value validation.

The main project package is situated in "lumatechallenge" with its guestbook app in the sibling directory. Templates are contained in each package directory, with miscellaneous and "base" templates inside the primary package templates. To keep the website simple, there are no static files (nor directories).

Side note: The Django secret key found in this repository does not match the server's.