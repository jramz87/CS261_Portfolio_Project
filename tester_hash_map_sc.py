import unittest
from hash_map_sc import *

class TestHashMapSC(unittest.TestCase):
    def test_put(self):
        self.m = HashMap(53, hash_function_1)
        for i in range(150):
            self.m.put('str' + str(i), i * 100)
            if i == 24:
                self.assertEqual(self.m.empty_buckets(), 39)
                self.assertEqual(round(self.m.table_load(), 2), 0.47)
                self.assertEqual(self.m.get_size(), 25)
                self.assertEqual(self.m.get_capacity(), 53)
            elif i == 49:
                self.assertEqual(self.m.empty_buckets(), 39)
                self.assertEqual(round(self.m.table_load(), 2), 0.94)
                self.assertEqual(self.m.get_size(), 50)
                self.assertEqual(self.m.get_capacity(), 53)
            elif i == 74:
                self.assertEqual(self.m.empty_buckets(), 82)
                self.assertEqual(round(self.m.table_load(), 2), 0.7)
                self.assertEqual(self.m.get_size(), 75)
                self.assertEqual(self.m.get_capacity(), 107)
            elif str(i) == 'str99':
                self.assertEqual(self.m.empty_buckets(), 79)
                self.assertEqual(round(self.m.table_load(), 2), 0.93)
                self.assertEqual(self.m.get_size(), 100)
                self.assertEqual(self.m.get_capacity(), 107)
        self.m.put('str124', 12400)
        self.m.put('str149', 14900)

    def test_load(self):
        self.m = HashMap(101, hash_function_1)
        self.assertEqual(round(self.m.table_load(), 2), 0.0)
        self.m.put('key1', 10)
        self.assertEqual(round(self.m.table_load(), 2), 0.01)
        self.m.put('key2', 20)
        self.assertEqual(round(self.m.table_load(), 2), 0.02)
        self.m.put('key1', 30)
        self.assertEqual(round(self.m.table_load(), 2), 0.02)

    def test_resize_table(self):
        self.m = HashMap(20, hash_function_1)
        self.m.put('key1', 10)
        self.assertEqual(self.m.get_size(), 1)
        self.assertEqual(self.m.get_capacity(), 23)
        self.assertEqual(self.m.get('key1'), 10)
        self.assertTrue(self.m.contains_key('key1'))
        self.m.resize_table(30)
        self.assertEqual(self.m.get_size(), 1)
        self.assertEqual(self.m.get_capacity(), 31)
        self.assertEqual(self.m.get('key1'), 10)
        self.assertTrue(self.m.contains_key('key1'))

        self.m = HashMap(75, hash_function_2)
        keys = [i for i in range(1, 1000, 13)]
        for key in keys:
            self.m.put(str(key), key * 42)
        self.assertEqual(self.m.get_size(), 77)
        self.assertEqual(self.m.get_capacity(), 79)

        self.m.resize_table(111)
        self.assertEqual(self.m.get_size(), 77)
        self.assertEqual(round(self.m.table_load(), 2), 0.68)

    def test_empty_buckets(self):
        self.m = HashMap(53, hash_function_1)
        for i in range(150):
            self.m.put('key' + str(i), i * 100)
            if i == 0:
                self.assertEqual(self.m.empty_buckets(), 52)
                self.assertEqual(self.m.get_size(), 1)
                self.assertEqual(self.m.get_capacity(), 53)
            elif i == 30:
                self.assertEqual(self.m.empty_buckets(), 39)
                self.assertEqual(self.m.get_size(), 31)
                self.assertEqual(self.m.get_capacity(), 53)
            elif i == 60:
                self.assertEqual(self.m.empty_buckets(), 83)
                self.assertEqual(self.m.get_size(), 61)
                self.assertEqual(self.m.get_capacity(), 107)
                print(self.m.empty_buckets(), self.m.get_size(), self.m.get_capacity())
            elif i == 90:
                print(self.m.empty_buckets(), self.m.get_size(), self.m.get_capacity())
            elif i == 120:
                print(self.m.empty_buckets(), self.m.get_size(), self.m.get_capacity())

    def test_find_mode(self):
        da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")



if __name__ == '__main__':
    unittest.main()
