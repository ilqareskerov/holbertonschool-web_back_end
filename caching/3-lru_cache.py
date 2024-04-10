#!/usr/bin/python3
""" FIFO caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = next(iter(self.cache_data))
                print("DISCARD: {}".format(discard))
                self.cache_data.pop(discard)
            self.cache_data[key] = item

    def get(self, key):
        if key is None or self.cache_data.get(key) is None:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
