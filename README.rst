.. image:: https://img.shields.io/pypi/v/importlib_resources.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/importlib_resources.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/importlib_resources

.. image:: https://github.com/python/importlib_resources/workflows/tests/badge.svg
   :target: https://github.com/python/importlib_resources/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://readthedocs.org/projects/importlib-resources/badge/?version=latest
   :target: https://importlib-resources.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2022-informational
   :target: https://blog.jaraco.com/skeleton

.. image:: https://tidelift.com/badges/package/pypi/importlib-resources
   :target: https://tidelift.com/subscription/pkg/pypi-importlib-resources?utm_source=pypi-importlib-resources&utm_medium=readme

``importlib_resources`` is a backport of Python standard library
`importlib.resources
<https://docs.python.org/3/library/importlib.html#module-importlib.resources>`_
module for older Pythons.

The key goal of this module is to replace parts of `pkg_resources
<https://setuptools.readthedocs.io/en/latest/pkg_resources.html>`_ with a
solution in Python's stdlib that relies on well-defined APIs.  This makes
reading resources included in packages easier, with more stable and consistent
semantics.

Compatibility
=============

New features are introduced in this third-party library and later merged
into CPython. The following table indicates which versions of this library
were contributed to different versions in the standard library:

.. list-table::
   :header-rows: 1

   * - importlib_resources
     - stdlib
   * - 5.8
     - 3.12
   * - 5.7
     - 3.11
   * - 5.0
     - 3.10
   * - 1.3
     - 3.9
   * - 0.5 (?)
     - 3.7

For Enterprise
==============

Available as part of the Tidelift Subscription.

This project and the maintainers of thousands of other packages are working with Tidelift to deliver one enterprise subscription that covers all of the open source you use.

`Learn more <https://tidelift.com/subscription/pkg/pypi-importlib-resources?utm_source=pypi-importlib-resources&utm_medium=referral&utm_campaign=github>`_.

Security Contact
================

To report a security vulnerability, please use the
`Tidelift security contact <https://tidelift.com/security>`_.
Tidelift will coordinate the fix and disclosure.
