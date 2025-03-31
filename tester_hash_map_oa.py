import unittest
import unittest
from hash_map_oa import *

class TestHashMapOA(unittest.TestCase):
    def test_put(self):
        self.m = HashMap(53, hash_function_1)
        for i in range(150):
            self.m.put('str' + str(i), i * 100)
            if i == 24:
                print(self.m.empty_buckets(), round(self.m.table_load(), 2), self.m.get_size(), self.m.get_capacity())
            elif i == 49:
                print(self.m.empty_buckets(), round(self.m.table_load(), 2), self.m.get_size(), self.m.get_capacity())
            elif i == 74:
                print(self.m.empty_buckets(), round(self.m.table_load(), 2), self.m.get_size(), self.m.get_capacity())
            elif i == 99:
                print(self.m.empty_buckets(), round(self.m.table_load(), 2), self.m.get_size(), self.m.get_capacity())
            elif i == 124:
                print(self.m.empty_buckets(), round(self.m.table_load(), 2), self.m.get_size(), self.m.get_capacity())
            elif i == 149:
                print(self.m.empty_buckets(), round(self.m.table_load(), 2), self.m.get_size(), self.m.get_capacity())

if __name__ == '__main__':
    unittest.main()
