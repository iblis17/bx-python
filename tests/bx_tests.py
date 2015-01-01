from jsonschema import validate, ValidationError
from time import sleep
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
    'title': 'items',
    'type': 'object',
    'required': ['name', 'price', 'quantity'],
    'properties': {
        'name': {
            'type': 'string'
        },
        'price': {
            'type': 'number'
        },
        'quantity': {
            'type': 'number'
        }
    }
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
    db = bx.Db()

    db.put('person', 'ty')
    assert_dict_equal(db.data, {'person': {'value': 'ty', 'exp': None}})
    assert db.exp('person') is None
    assert db.get('person') == 'ty'


def test_put_timeout_1():
    """Tests Db.put, with a timeout."""
    db = bx.Db()

    db.put('person', 'ty', timeout=1000)
    assert db.get('person') == 'ty'
    sleep(2)
    assert_raises(KeyError, db.get, 'person')


def test_put_timeout_2():
    """Tests Db.put, with a timeout."""
    db = bx.Db()

    db.put('thing', 1, timeout=5000)
    assert db.get('thing') == 1
    sleep(5.5)
    assert_raises(KeyError, db.get, 'thing')


def test_put_schema_malformed():
    """Tests Db.put, with malformed input."""
    db = bx.Db(schema=item_schema)

    assert_raises(ValidationError, db.put, 'malformed', 'input')
    assert_raises(KeyError, db.get, 'malformed')


def test_put_schema():
    """Tests Db.put, with a schema."""
    db = bx.Db(schema=item_schema)

    milk = {
        'name': 'Hood Fat Free Milk',
        'price': 2.75,
        'quantity': 400
    }

    db.put('milk', milk)
    assert_dict_equal(db.get('milk'), milk)


def test_put_timeout_malformed():
    """Tests Db.put, with an invalid timeout."""
    db = bx.Db()

    assert_raises(ValueError, db.put, 'test', 'test', timeout='haha')


def test_check_schema():
    """Tests Db.check."""
    db = bx.Db(schema=student_schema)

    ty = {
        'name': 'Ty Kelley',
        'major': 'Computer Science',
        'gpa': 0.0
    }

    assert db.check('wrong') is False
    assert db.check(ty) is True


def test_get_no_timeout():
    """Tests Db.get with no timeout."""
    db = bx.Db()

    db.put('item', 0)
    assert db.get('item') == 0
    assert_raises(KeyError, db.get, 'fake')


def test_get_timeout():
    """Test Db.get with a timeout."""
    db = bx.Db()

    db.put('item', 0, timeout=1000)
    assert db.get('item') == 0
    sleep(2)
    assert_raises(KeyError, db.get, 'item')
