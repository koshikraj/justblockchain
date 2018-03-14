#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `justblockchain` package."""

import json
import pytest

from Crypto.Hash import SHA256
from justblockchain import justblockchain


def test_genesis_block():
    """Sample pytest test function with the pytest fixture as an argument."""
    blockchain = justblockchain.Blockchain()
    genesis_block = blockchain.get_genesis_block()
    hash_object = SHA256.new(data=(str(genesis_block.index) +
                                   genesis_block.previous_hash +
                                   str(genesis_block.timestamp) +
                                   genesis_block.data).encode())
    assert hash_object.hexdigest() == genesis_block.hash
