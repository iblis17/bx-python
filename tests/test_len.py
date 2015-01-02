from jsonschema import validate, ValidationError
from time import sleep
from nose.tools import *
from tests import *
import bx


def test():
    """Tests len(db) with a for loop."""

    db = bx.Db()
    for i in range(0, 5):
        assert len(db) == i
        db.put(i, i)
