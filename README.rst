hcbl
===========

A plugin for Hachi_ to block spam words.

.. _Hachi: https://github.com/guokr/Hachi

Usage
-------

::

    > bl = Blacklist()
    > bl.predict(message)

Attention
----------

You need to provide your blacklist.csv in ``./data/`` .
