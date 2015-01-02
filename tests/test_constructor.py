from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test_default():
    """Tests the default constructor."""

    db = bx.Db()
    assert db.debug is False
    assert db.schema is None
    assert type(db.credits) is str
    assert_dict_equal(db.data, {})


def test_schema():
    """Tests the constructor, with a schema passed in."""

    db = bx.Db(schema=student_schema)
    assert db.debug is False
    assert_dict_equal(db.schema, student_schema)
    assert type(db.credits) is str
    assert_dict_equal(db.data, {})


def test_debug():
    """Tests the constructor, with debug set to True."""

    db = bx.Db(debug=True)
    assert db.debug is True
    assert db.schema is None
    assert type(db.credits) is str
    assert_dict_equal(db.data, {})


def test_debug_and_schema():
    """Tests the constructor, with debug enabled and a schema."""

    db = bx.Db(debug=True, schema=student_schema)
    assert db.debug is True
    assert_dict_equal(db.schema, student_schema)
    assert type(db.credits) is str
    assert_dict_equal(db.data, {})


def test_debug_malformed():
    """Tests the constructor, with debug set to a non-boolean value."""

    assert_raises(TypeError, bx.Db, debug='oops')
