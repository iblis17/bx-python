from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_one():
    """Tests db.mdelete, with one item."""

    db = bx.Db()
    db.put('hello', 'world')
    assert db.get('hello') == 'world'
    db.mdelete('hello')
    assert_raises(KeyError, db.get, 'hello')


def test_three():
    """Tests db.mdelete, with three items."""

    db = bx.Db()
    db.put('hello', 'world')
    db.put('hey', 'what is up')
    db.put('i like', 'ice cream')
    db.mdelete('hello', 'hey', 'i like')
    assert_dict_equal(db.data, {})


def test_malformed():
    """Tests db.mdelete on a key that doesn't exist."""

    db = bx.Db()
    db.put('hello', 'world')
    db.put('yo', 'dude')
    assert_raises(KeyError, db.mdelete, 'hello', 'yo', 'hey')
