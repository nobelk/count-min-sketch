import hashlib
import math
from typing import Callable
from src.count_min_sketch.item import Item


class CMS:
    def __init__(self, cols: int, hash_functions: Callable[[str], int] = None):
        self._cols = cols
        if hash_functions:
            self._hash_functions = hash_functions
        else:
            self._hash_functions = [hashlib.sha256, hashlib.shake_256, hashlib.blake2b]
        self._matrix = [[0 for _ in range(self._cols)] for _ in range(len(self._hash_functions))]

    def update(self, item: Item) -> None:
        for i, hash_function in enumerate(self._hash_functions):
            hash_value = self._get_int_hash_value(hash_function, item)
            col_offset = hash_value % self._cols
            self._matrix[i][col_offset] += 1

    def query(self, item: Item) -> int:
        min_val = math.inf
        for i, hash_function in enumerate(self._hash_functions):
            hash_value = self._get_int_hash_value(hash_function, item)
            col_offset = hash_value % self._cols
            min_val = min(min_val, self._matrix[i][col_offset])
        return min_val

    def _get_int_hash_value(self, hash_function: Callable[[str], int], item: Item) -> int:
        if hash_function == hashlib.sha256 or hash_function == hashlib.blake2b:
            return int.from_bytes(hash_function(repr(item).encode()).hexdigest().encode(), 'big')
        elif hash_function == hashlib.shake_256:
            return int.from_bytes(hash_function(repr(item).encode()).hexdigest(32).encode(), 'big')
        else:
            raise NotImplementedError("Unknown hash function")
