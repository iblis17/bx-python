from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_no_timeout():
    """Tests Db.delete, with no timeout."""

    db = bx.Db()
    db.put('color', 'red')
    assert db.get('color') == 'red'
    db.delete('color')
    assert_raises(KeyError, db.get, 'color')


def test_timeout():
    """Tests Db.delete, called thanks to a timeout."""

    db = bx.Db()
    db.put('color', 'red', timeout=1000)
    assert db.get('color') == 'red'
    sleep(1.25)
    assert_raises(KeyError, db.get, 'color')


def test_malformed():
    """Tests Db.delete with a key that doesn't exist."""

    db = bx.Db()
    assert_raises(KeyError, db.get, 'hello')
