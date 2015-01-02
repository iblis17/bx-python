from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx

def test_empty():
    """Tests str(db) with an empty database."""

    db = bx.Db()
    assert str(db) == '{}'


def test_filled():
    """Tests str(db) with a filled database."""

    db = bx.Db()
    db.put('hello', 'world')
    assert_dict_equal(eval(str(db)), {'hello': {'value': 'world', 'exp': None}})
