from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_empty():
    """Tests db.clear when database was already empty."""

    db = bx.Db()
    db.clear()
    assert_dict_equal(db.data, {})
    assert_dict_equal(db.all(), {})


def test_filled():
    """Tests db.clear, when data was present before."""

    db = bx.Db()
    db.put('hello', 'world')
    db.clear()
    assert_dict_equal(db.data, {})
    assert_dict_equal(db.all(), {})
