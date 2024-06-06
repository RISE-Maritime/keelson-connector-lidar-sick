#
# Copyright (c) 2023 SICK AG
# SPDX-License-Identifier: MIT
#

from scansegmentdecoding import msgpackUtil
import msgpack
import struct
import numpy as np
import pytest
import copy


def test_single_key_is_replaced_correctly():
    integerKeys = msgpack.packb({0xA0: "Test"})
    stringKeys = {"LayerId": "Test"}

    assert msgpackUtil.UnpackMsgpackAndReplaceIntegerKeywords(
        integerKeys) == stringKeys


def test_multiple_keys_are_replaced_correctly():
    integerKeys = msgpack.packb({0xA0: "Test", 0x52: 42})
    stringKeys = {"LayerId": "Test", "DistValues": 42}

    assert msgpackUtil.UnpackMsgpackAndReplaceIntegerKeywords(
        integerKeys) == stringKeys


def test_nested_dicts_are_replaced_correctly():
    integerKeys = msgpack.packb({0xA0: {0x52: 42}})
    stringKeys = {"LayerId": {"DistValues": 42}}

    assert msgpackUtil.UnpackMsgpackAndReplaceIntegerKeywords(
        integerKeys) == stringKeys


def test_list_of_dicts_are_replaced_correctly():
    integerKeys = msgpack.packb(
        {
            0x11: [
                {0x50: 42},
                {0x51: 43},
                {0x52: 44}
            ]
        }
    )
    stringKeys = {
        "data": [
            {"ChannelTheta": 42},
            {"ChannelPhi": 43},
            {"DistValues": 44}
        ]
    }

    assert msgpackUtil.UnpackMsgpackAndReplaceIntegerKeywords(
        integerKeys) == stringKeys


def test_value_of_class_key_is_replaced():
    integerKeys = msgpack.packb(
        {
            0x10: 0x70
        }
    )
    stringKeys = {
        "class": "Scan"
    }

    assert msgpackUtil.UnpackMsgpackAndReplaceIntegerKeywords(
        integerKeys) == stringKeys


def test_value_of_endian_key_is_replaced():
    integerKeys = msgpack.packb(
        {
            0x14: 0x30
        }
    )
    stringKeys = {
        "endian": "little"
    }

    assert msgpackUtil.UnpackMsgpackAndReplaceIntegerKeywords(
        integerKeys) == stringKeys


def test_data_types_are_replaced_correctly():
    integerKeys = msgpack.packb(
        {
            0x15: [0x31, 0x32, 0x33, 0x34, 0x35]
        }
    )
    stringKeys = {
        "elemTypes": ["float32", "uint32", "uint8", "uint16", "int16"]
    }

    assert msgpackUtil.UnpackMsgpackAndReplaceIntegerKeywords(
        integerKeys) == stringKeys
