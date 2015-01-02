from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_no_timeout():
    """Tests db.get with no timeout."""

    db = bx.Db()
    db.put('hello', 'world')
    assert db.get('hello') == 'world'
    assert_dict_equal(db.data['hello'], {'value': 'world', 'exp': None})


def test_timeout():
    """Tests db.get with a timeout."""

    db = bx.Db()
    db.put('hello', 'world', timeout=750)
    assert db.get('hello') == 'world'
    sleep(0.8)
    assert_raises(KeyError, db.get, 'hello')


def test_malformed():
    """Tests db.get with malformed data."""

    db = bx.Db()
    assert_raises(KeyError, db.get, 0)
    assert_raises(KeyError, db.get, 'item')
    assert_raises(KeyError, db.get, 'hello')
