# Name: Jessica Ramirez
# OSU Email: ramirj22@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6 - HashMap Implementation
# Due Date: 3/15/2025
# Description: Implementation of a HashMap using the Separate Chaining
#              technique for collision resolution, based on the DynamicArray
#              and LinkedList classes. Includes various methods: put,
#              resize_table, table_load, empty_buckets, get, contains_key,
#              remove, get_keys_and_values, and clear. Additionally, this code
#              contains a standalone function, find_mode, for determining mode.


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Updates specified key/value pair in the HashMap. If the key/value pair
        doesn't exist, it is added to the HashMap.

        :param key:     string representation of a key to be added or updated
        :param value:   object representation of a value, corresponding to the
                        specified key, to be added or updated
        """
        # Check load factor and resize if needed
        if self.table_load() >= 1:
            self.resize_table(2 * self._capacity)

        # Calculate index from hash function
        index = self._hash_function(str(key)) % self._capacity
        bucket = self._buckets.get_at_index(index)

        # Modify key-value pair in existing bucket
        node = bucket.contains(key)
        if node:
            node.value = value

        # If key not found, add key to HashMap via LinkedList
        else:
            bucket.insert(key, value)
            self._size += 1

    def resize_table(self, new_capacity: int) -> None:
        """
        If the load factor is >= 1, the capacity of the underlying
        DynamicArray is increased to next larger prime number.

        :param new_capacity:    integer describing new DynamicArray size
        """
        # Validate new_capacity
        if new_capacity < 1:
            return

        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        # Create new DynamicArray
        new_buckets = DynamicArray()
        for _ in range(new_capacity):
            new_buckets.append(LinkedList())

        # Store old values and create new ones
        old_buckets = self._buckets
        old_capacity = self._capacity
        self._buckets = new_buckets
        self._capacity = new_capacity
        self._size = 0

        # Rehash old keys and insert into new DynamicArray
        for index in range(old_capacity):
            old_bucket = old_buckets.get_at_index(index)
            # Use iterator to traverse LinkedList
            for node in old_bucket:
                current_key = node.key
                current_value = node.value
                self.put(current_key, current_value)

    def table_load(self) -> float:
        """
        Return the current hash table load factor.

        :return:    float representation of the current load factor
        """
        # Load factor = # of elements / table size
        load_factor = self._size / self._capacity

        return load_factor

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the HashMap.

        :return:    integer representation of the number of empty buckets
        """
        count = 0
        for index in range(self._capacity):
            current_bucket = self._buckets.get_at_index(index)
            if current_bucket.length() == 0:
                count += 1

        return count

    def get(self, key: str) -> object:
        """
        Returns the value associated with the specified key, or None
        if the key is not contained in the HashMap.

        :param key:     string type key whose value we seek to retrieve
        :return:        object representation of the matching value,
                        or None if not present
        """
        # Identify where value should be
        index = self._hash_function(str(key)) % self._capacity
        bucket = self._buckets.get_at_index(index)

        # Iterate over bucket to find value
        node = bucket.contains(key)
        if not node:
            return None

        return node.value

    def contains_key(self, key: str) -> bool:
        """
        Uses Boolean logic to express whether a specified key is present.

        :param key:     string type key who we are inquiring about
        :return:        Boolean logic describing whether the specified key
                        is in the HashMap (True) or not (False)
        """
        # Identify where value should be
        index = self._hash_function(str(key)) % self._capacity
        bucket = self._buckets.get_at_index(index)

        # Iterate over bucket to find value
        node = bucket.contains(key)
        if not node:
            return False

        return True

    def remove(self, key: str) -> None:
        """
        Removes the specified key-value pair from HashMap, if they exist.

        :param key:     string type key that we seek to remove
        """
        index = self._hash_function(str(key)) % self._capacity
        bucket = self._buckets.get_at_index(index)

        # Exit if node doesn't exist
        if not bucket.contains(key):
            return

        # Remove node if it exists
        bucket.remove(key)
        self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Extracts all key-value pairs from the HashMap and stores them
        in a DynamicArray (in no particular order).

        :return:    DynamicArray containing all key-value pairs in HashMap
        """
        output_array = DynamicArray()

        # Iterate over all buckets in HashMap
        for index in range(self._capacity):
            bucket = self._buckets.get_at_index(index)
            # Iterate over all nodes in buckets
            for node in bucket:
                output_array.append((node.key, node.value))

        return output_array

    def clear(self) -> None:
        """
        Clears the contents of the HashMap, while maintaining the same capacity.
        """
        self._buckets = DynamicArray()
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())
        self._size = 0

def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Calculates the mode---most frequently occurring value(s)---and its
    frequency occurring in a provided DynamicArray, outputting the mode
    and frequency in a tuple (in that order).

    :param da:      DynamicArray of interest whose mode we seek to identify
    :return:        tuple  representing the mode (DynamicArray) and its
                    frequency (integer), in that order
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap()
    max_frequency = 0
    max_key = DynamicArray()

    # Store frequencies of values in DynamicArray into HashMap
    for index in range(da.length()):
        key = da.get_at_index(index)
        frequency = map.get(key)
        # Increment frequency of existing key
        if frequency:
            frequency += 1
            map.put(key, frequency)
        # Add new key to HashMap
        else:
            frequency = 1
            map.put(key, frequency)

        # Extract highest frequency value and store key
        if frequency > max_frequency:
            max_frequency = frequency
            max_key = DynamicArray()
            max_key.append(key)
        elif frequency == max_frequency:
            max_key.append(key)

    return max_key, max_frequency


# ------------------- BASIC TESTING ---------------------------------------- #


if __name__ == "__main__":
    """
    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())
    """
    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))
    """
    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())
    
    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())
    
    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    
    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)
    
    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')
    
    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())
    
    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())
    
    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
    """
