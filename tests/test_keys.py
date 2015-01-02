from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_empty():
    """Tests db.keys with no data."""

    db = bx.Db()
    assert db.keys() == []


def test_filled():
    """Tests db.keys with data."""

    db = bx.Db()
    for i in range(0, 5):
        db.put(i, i)

    assert db.keys() == [0, 1, 2, 3, 4]
