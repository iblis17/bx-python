from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_empty():
    """Tests db.mget with no data."""

    db = bx.Db()
    assert_dict_equal(db.mget('hello', 'data'), {})


def test_one():
    """Tests db.mget with one item in the database."""

    db = bx.Db()
    db.put('hello', 'world')
    assert_dict_equal(db.mget('hello', 'data'), {'hello': 'world'})


def test_two():
    """Tests db.mget with two items in the database."""

    db = bx.Db()
    db.put('0', 0)
    db.put('1', 1)
    assert set(db.mget('0', '1').keys()) == {'0', '1'}
