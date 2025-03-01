Welcome to |project| documentation!
===================================

``importlib_resources`` is a library which provides for access to *resources*
in Python packages.  It provides functionality similar to ``pkg_resources``
`Basic Resource Access`_ API, but without all of the overhead and performance
problems of ``pkg_resources``.

In our terminology, a *resource* is a file tree that is located within an
importable `Python package`_.  Resources can live on the file system or in a
zip file, with support for other loader_ classes that implement the appropriate
API for reading resources.

``importlib_resources`` supplies a backport of :mod:`importlib.resources`,
enabling early access to features of future Python versions and making
functionality available for older Python versions. Users are encouraged to
use the Python standard library where suitable and fall back to
this library for future compatibility. Developers looking for detailed API
descriptions should refer to the standard library documentation.

The documentation here includes a general :ref:`usage <using>` guide and a
:ref:`migration <migration>` guide for projects that want to adopt
``importlib_resources`` instead of ``pkg_resources``.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   using.rst
   migration.rst
   history.rst

.. tidelift-referral-banner::


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _`Basic Resource Access`: http://setuptools.readthedocs.io/en/latest/pkg_resources.html#basic-resource-access
.. _`Python package`: https://docs.python.org/3/reference/import.html#packages
.. _loader: https://docs.python.org/3/reference/import.html#finders-and-loaders
