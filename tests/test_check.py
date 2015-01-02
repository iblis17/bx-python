from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_valid():
    """Tests Db.check, with valid data."""

    db = bx.Db(schema=student_schema)
    assert db.check(student) is True


def test_no_schema():
    """Tests Db.check, with no schema."""

    db = bx.Db()
    assert db.check(0) is True
    assert db.check(student) is True


def test_invalid():
    """Tests Db.check, with invalid data."""

    db = bx.Db(schema=student_schema)
    assert db.check(0) is False


def test_malformed():
    """Tests Db.check, with a malformed schema."""

    db = bx.Db(schema=0)
    assert db.check('hello') is True
    assert db.check(student) is True
    assert db.check(12) is True
