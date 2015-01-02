from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_empty():
    """Tests db.vals with no items."""

    db = bx.Db()
    assert db.vals() == []


def test_filled():
    """Tests db.vals with some items present."""

    db = bx.Db()
    db.put('hello', 'world')
    assert db.vals() == ['world']
