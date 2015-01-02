from jsonschema import validate, ValidationError
from time import sleep, time
from nose.tools import *
from tests import *
import bx


def test_none():
    """Tests db.exp, with a key that doesn't expire."""

    db = bx.Db()
    db.put('hello', 'world')
    assert db.exp('hello') is None


def test_expiring():
    """Tests db.exp, with a key that does expire."""

    db = bx.Db()
    db.put('hello', 'world', 2000)
    now = time()
    assert db.exp('hello') > now


def test_malformed():
    """Tests db.exp, with a key that doesn't exist."""

    db = bx.Db()
    assert_raises(KeyError, db.exp, 'hello')
