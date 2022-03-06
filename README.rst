================
python-pinterest
================

A simple Python wrapper for Pinterest REST API (Beta) (5.x) ✨ 🍰 ✨

.. image:: https://github.com/sns-sdks/python-pinterest/workflows/Test/badge.svg
    :target: https://github.com/sns-sdks/python-pinterest/actions

.. image:: https://codecov.io/gh/sns-sdks/python-pinterest/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/sns-sdks/python-pinterest


Introduction
============

This library provides a service to easily use Pinterest REST API for v5.x.

And support ``Async`` And ``sync`` mode.


Using
=====

The API is exposed via the ``pinterest.Api`` class and ``pinterest.AsyncApi`` class.

INSTANTIATE
-----------

You can initial an instance with ``access token``::

    # Sync
    >>> from pinterest import Api
    >>> p = Api(access_token="Your access token")
    # Async
    >>> from pinterest import AsyncApi
    >>> ap = AsyncApi(access_token="Your access token")

Usage
-----

Get pin info::

    # Sync
    >>> p.pins.get(pin_id="1022106077902810180")
    # Pin(id='1022106077902810180', created_at='2022-02-14T02:54:38')
    # Async
    >>> await ap.pins.get(pin_id="1022106077902810180")
    # Pin(id='1022106077902810180', created_at='2022-02-14T02:54:38')


TODO
====

- Docs
- Tests