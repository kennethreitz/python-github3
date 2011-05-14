Github3: Python wrapper for the (new) GitHub API v3
===================================================

Github's working on a new API. This is the new Python wrapper for it.

**This a work in progress.** Should be relased before the first week of May.



Usage
-----

::

    from github3 import github

    github.login('username', 'password')
    # optional

    github.





Installation
------------

To install clint, simply: ::

    $ pip install github3

Or, if you absolutely must: ::

    $ easy_install github3

But, you really shouldn't do that.



License:
--------

ISC License. ::

    Copyright (c) 2011, Kenneth Reitz <me@kennethreitz.com>

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted, provided that the above
    copyright notice and this permission notice appear in all copies.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


Contribute
----------

If you'd like to contribute, simply fork `the repository`_, commit your changes
to the **develop** branch (or branch off of it), and send a pull request. Make
sure you add yourself to AUTHORS_.



Roadmap
-------

- Get it Started
- HTTP BASIC
- Get it working
- Sphinx Documetnation
- Examples
- Unittests
- OAuth Last (how?)