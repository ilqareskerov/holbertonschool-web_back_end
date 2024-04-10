#!/usr/bin/python3
"""  Basic dictionary """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                print("DISCARD: {}".format(first))
                del self.cache_data[first]
            self.cache_data[key] = item

    def get(self, key):
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
