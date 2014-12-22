from jsonschema import validate
import threading
import time


class Db():
    """Defines a simple key-value database."""

    def __init__(self, debug=False, schema=None):
        """Creates a new data store."""

        if type(debug) is not bool:
            raise TypeError('debug must be True or False')
        else:
            self.__debug = debug
            self.__schema = schema
            self.__data = {}
            self.__credits = """
                              __
                       ___~~~`  `~~__
                 ___~~~              `~_
                |~_                     `~_
                |  ~_               ___ ~~ |
                |    ~_        __~~~       |
                |      ~_ __~~~            |
                |        |                 |
                |        |                 |
                |        |                 |
                |        |       bx        |
                ~_       |                 |
                  ~_     |               __|
                    ~_   |          __~~~
                      ~_ |     __~~~
                        ~|__~~~

                (c) 2014 tylucaskelley
            """
            self.__lock = threading.RLock()

    def put(self, key, val, time=None):
        """Put something in the data store, with an optional expiration time."""
        pass

    def check(self, data):
        """Check to see if data fits the schema."""
        pass

    def get(self, key):
        """Get a value from the data store."""
        pass

    def mget(self, keys):
        """Get multiple values from the data store."""
        pass

    def delete(self, key):
        """Delete a value from the data store."""
        pass

    def mdelete(self, keys):
        """Delete multiple values from the data store."""
        pass

    def clear(self):
        """Empty the data store."""
        pass

    def all(self):
        """Get everything from the data store."""
        pass

    def keys(self):
        """Get a list of the keys in the data store."""
        pass

    def vals(self):
        """Get a list of the values in the data store."""
        pass

    def size(self):
        """Get the size in bytes of the data store."""
        pass

    def exp(self, key):
        """Get the expiration date of an item in the data store."""
        pass

    def __len__(self):
        """Get the number of items in the data store."""
        return len(self.__data)
