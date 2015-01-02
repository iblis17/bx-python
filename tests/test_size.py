from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx
import sys


def test_empty():
    """Tests db.size, with an empty data store."""

    db = bx.Db()
    empty_dict = sys.getsizeof({})
    assert db.size() == empty_dict
