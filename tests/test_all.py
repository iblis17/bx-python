from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_empty():
    """Tests db.all, with no data."""

    db = bx.Db()
    assert_dict_equal(db.all(), {})


def test_filled():
    """Tests db.all, with some data present."""

    db = bx.Db()
    db.put('hello', 'world')
    assert_dict_equal(db.all(), {'hello': 'world'})
    db.put('goodbye', 'world')
    assert_dict_equal(db.all(), {'hello': 'world', 'goodbye': 'world'})
