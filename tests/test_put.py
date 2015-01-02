from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_no_timeout():
    """Tests db.put, with no timeout on the data."""

    db = bx.Db()
    db.put('hello', 'world')
    assert db.get('hello') == 'world'
    assert_dict_equal(db.data['hello'], {'value': 'world', 'exp': None})


def test_timeout():
    """Tests db.put, with a timeout on the data."""

    db = bx.Db()
    db.put('hello', 'world', timeout=2000)
    assert db.get('hello') == 'world'
    assert type(db.data['hello']['exp']) is float


def test_schema():
    """Tests db.put, with a schema."""

    db = bx.Db(schema=student_schema)
    db.put('student 1', student)
    assert_dict_equal(db.get('student 1'), student)


def test_schema_malformed():
    """Tests db.put, with data that doesn't fit the schema."""

    db = bx.Db(schema=student_schema)
    assert_raises(ValidationError, db.put, 'student 1', 'oops')


def test_changing_data():
    """Tests db.put, where it's used multiple times on the same key."""

    db = bx.Db()
    db.put('hello', 'world')
    assert db.get('hello') == 'world'
    db.put('hello', 'friend')
    assert db.get('hello') == 'friend'
