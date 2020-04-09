"""
singleton 单例模式
保证一个类仅有一个实例，并提供一个访问它的全局访问点。
怎么才能保证一个类只有一个实例并且这个实例易于被访问呢
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, x, y):
        self.x = x
        self.y = y

s = Singleton(1, 2)

from contextlib import contextmanager
import asyncio