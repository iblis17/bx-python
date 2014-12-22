from nose.tools import *
import bx

student_schema = {
    'title': 'students',
    'type': 'object',
    'required': ['name', 'major', 'gpa'],
    'properties': {
        'name': {
            'type': 'string'
        },
        'major': {
            'type': 'string'
        },
        'gpa': {
            'type': 'number'
        }
    }
}

item_schema = {

}


def test_init_empty():
    """Tests the Db constructor, with no arguments passed."""
    db = bx.Db()

    assert db.debug is False
    assert db.schema is None
    assert type(db.credits) is str
    assert_dict_equal(db.data, {})


def test_init_malformed():
    """Tests the Db constructor, with debug set to a non-boolean value."""
    assert_raises(TypeError, bx.Db, debug='oops')


def test_init_schema():
    """Tests the Db constructor, with a schema passed in."""
    db = bx.Db(schema=student_schema)

    assert db.debug is False
    assert type(db.credits) is str
    assert_dict_equal(db.schema, student_schema)
    assert_dict_equal(db.data, {})


def test_put_no_schema():
    """Tests Db.put, with no schema."""


def test_put_schema_malformed():
    """Tests Db.put, with malformed input."""


def test_put_schema():
    """Tests Db.put, with a schema."""


def test_put_timeout():
    """Tests Db.put, with a timeout."""
