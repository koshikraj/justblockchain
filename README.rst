==============
justblockchain
==============


.. image:: https://img.shields.io/pypi/v/justblockchain.svg
        :target: https://pypi.python.org/pypi/justblockchain

.. image:: https://img.shields.io/travis/koshikraj/justblockchain.svg
        :target: https://travis-ci.org/koshikraj/justblockchain

.. image:: https://readthedocs.org/projects/justblockchain/badge/?version=latest
        :target: https://justblockchain.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/koshikraj/justblockchain/shield.svg
     :target: https://pyup.io/repos/github/koshikraj/justblockchain/
     :alt: Updates



A blockchain linker to help understand hash functions in blockchain


* Free software: MIT license
* Documentation: https://justblockchain.readthedocs.io.


Quick start
-----------

Installation
~~~~~~~~~~~~

- pip install justblockchain


Creating simple blockchain
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    >>> from justblockchain import justblockchain
    >>> blockchain = justblockchain.Blockchain()
    >>> blockchain.add_block("some block content")

    #display the blockchain
    >>> blockchain.chain
    [{'previous_hash': '0', 'hash':
    '816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7',
    'timestamp': 1465154705, 'index': 0, 'data': 'my genesis block!!'},
    {'previous_hash':
    '816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7', 'hash':
    'a046e0b31d2374d171a6bf62f15261f8bb1f71e6351aab2ce7ce6d550506d9ee',
    'timestamp': '1521013680', 'index': 1, 'data': 'some block content'}]

Creating a Block using proof-of-work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    >>> from justblockchain import justblockchain
    >>> blockchain = justblockchain.Blockchain()
    >>> blockchain.difficulty_bits = 20
    >>> blockchain.add_block("some block content")
    Computing nonce for the block...
    Success with nonce 2991544
    Hash is 00000fc3d1420243cca17693bcc75334eb9f01b0943772f5d6456e17f3218abc


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
