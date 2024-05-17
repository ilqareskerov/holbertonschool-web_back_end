#!/usr/bin/env python3
"This is a line of text"
import redis
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    "This is a line of text"

    @wraps(method)
    def timesCalled(self, *args, **kwds):
        "This is a line of text"
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return timesCalled


def call_history(method: Callable) -> Callable:
    "This is a line of text"

    @wraps(method)
    def history(self, *args, **kwds):
        "This is a line of text"
        inputs = method.__qualname__ + ":inputs"
        outputs = method.__qualname__ + ":outputs"
        self._redis.rpush(inputs, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(outputs, output)
        return output

    return history


def replay(method: Callable):
    "This is a line of text"
    qualname = method.__qualname__
    redis = method.__self__._redis
    count = redis.llen(qualname + ":inputs")
    inputs = redis.lrange(qualname + ":inputs", 0, -1)
    outputs = redis.lrange(qualname + ":outputs", 0, -1)
    print(f"{qualname} was called {count} times:")
    for input, output in zip(inputs, outputs):
        key = input.decode("utf-8")
        value = output.decode("utf-8")
        print(f"{qualname}(*{key})" + f" -> {value}")


class Cache:
    "This is a line of text"

    def __init__(self):
        "This is a line of text"
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        "This is a line of text"
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        "This is a line of text"
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: bytes) -> str:
        "This is a line of text"
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        "This is a line of text"
        return self.get(key, int)
