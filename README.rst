hcbl
===========

.. image:: https://travis-ci.org/Momingcoder/hcbl.svg?branch=master
    :target: https://travis-ci.org/Momingcoder/hcbl

A plugin for Hachi_ to block spam words.

.. _Hachi: https://github.com/guokr/Hachi

Usage
-------

::

    > bl = Blacklist()
    > bl.predict(message)

Configuration
--------------

::

    > ('hcbl', 'Blacklist()', 'blacklist')

Attention
----------

You need to provide your blacklist.csv in ``./data/`` .
