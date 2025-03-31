# HashMap Implementation

A comprehensive implementation of HashMap data structures using two different collision resolution strategies: Separate Chaining and Open Addressing with Quadratic Probing. Developed as a portfolio project for CS261 (Data Structures) at Oregon State University, Winter 2025.

> **Note:** This project was developed with specific implementation requirements as part of academic coursework. The implementations follow best practices for hash table design to achieve O(1) average time complexity for common operations.

## ✨ Features

- **Two Implementation Approaches**:
  - Separate Chaining using singly linked lists
  - Open Addressing with quadratic probing
  
- **Core Operations**:
  - **put(key, value)**: Insert or update key-value pairs
  - **get(key)**: Retrieve values by key
  - **remove(key)**: Remove entries from the hash map
  - **contains_key(key)**: Check if a key exists
  
- **Performance Analysis**:
  - **table_load()**: Calculate and monitor hash table load factor
  - **empty_buckets()**: Track empty spaces in the hash table
  - **resize_table()**: Dynamically resize the hash table when needed
  
- **Additional Features**:
  - **find_mode()**: Find most frequent values in an array (Separate Chaining)
  - **Iterator support**: Iterate through key-value pairs (Open Addressing)

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Data Structures](https://img.shields.io/badge/Data_Structures-FF6B6B?style=for-the-badge&logo=buffer&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-6495ED?style=for-the-badge&logo=thealgorithms&logoColor=white)
![Unit Testing](https://img.shields.io/badge/Unit_Testing-4B275F?style=for-the-badge&logo=pytest&logoColor=white)

## 📋 Implementation Details

### Separate Chaining (hash_map_sc.py)

| Feature | Implementation |
| ------- | -------------- |
| Storage | Dynamic Array of Linked Lists |
| Collision Handling | Singly Linked Lists at each bucket |
| Load Factor Threshold | 1.0 (triggers resizing) |
| Resize Strategy | Double capacity and rehash |
| Key-Value Storage | LinkedList Nodes |

### Open Addressing (hash_map_oa.py)

| Feature | Implementation |
| ------- | -------------- |
| Storage | Dynamic Array with HashEntry objects |
| Collision Handling | Quadratic Probing |
| Load Factor Threshold | 0.5 (triggers resizing) |
| Resize Strategy | Double capacity and rehash |
| Deletion Strategy | Tombstone marking |
| Key-Value Storage | HashEntry objects |

## 🚀 Complexity Analysis

| Operation | Average Case | Worst Case |
| --------- | ------------ | ---------- |
| put() | O(1) | O(n) |
| get() | O(1) | O(n) |
| remove() | O(1) | O(n) |
| contains_key() | O(1) | O(n) |
| resize_table() | O(n) | O(n) |
| empty_buckets() | O(1) | O(1) |
| table_load() | O(1) | O(1) |
| get_keys_and_values() | O(n) | O(n) |
| clear() | O(n) | O(n) |

## 🖥️ Usage Examples

### Separate Chaining Example
```python
from hash_map_sc import HashMap, hash_function_1

# Create a new HashMap with initial capacity 10
hash_map = HashMap(10, hash_function_1)

# Add some key-value pairs
hash_map.put("apple", 15)
hash_map.put("banana", 20)
hash_map.put("cherry", 25)

# Retrieve values
apple_value = hash_map.get("apple")  # Returns 15
nonexistent = hash_map.get("grape")  # Returns None

# Check if keys exist
has_apple = hash_map.contains_key("apple")  # Returns True
has_grape = hash_map.contains_key("grape")  # Returns False

# Get current stats
load = hash_map.table_load()  # Returns 0.3 (3 elements in 10 buckets)
empty = hash_map.empty_buckets()  # Returns 7

# Find mode in an array
from a6_include import DynamicArray
arr = DynamicArray(["red", "blue", "red", "green", "blue", "red"])
mode_values, frequency = find_mode(arr)  # Returns (['red'], 3)

# Remove an element
hash_map.remove("banana")
```

### Open Addressing Example
```python
from hash_map_oa import HashMap, hash_function_2

# Create a new HashMap with initial capacity 10
hash_map = HashMap(10, hash_function_2)

# Add some key-value pairs
hash_map.put("apple", 15)
hash_map.put("banana", 20)
hash_map.put("cherry", 25)

# Iterate through key-value pairs
for entry in hash_map:
    print(f"Key: {entry.key}, Value: {entry.value}")

# Resize the table
hash_map.resize_table(20)

# Clear the table
hash_map.clear()
```

## 📦 Installation and Setup

```bash
# Clone the repository
git clone https://github.com/jramz87/CS261_Portfolio_Project.git

# Navigate to the project directory
cd CS261_Portfolio_Project

# Run basic tests for Separate Chaining implementation
python hash_map_sc.py

# Run basic tests for Open Addressing implementation
python hash_map_oa.py

# Run comprehensive unit tests
python tester_hash_map_sc.py
python tester_hash_map_oa.py
```

> **Note:** This project includes dedicated unit test files (`tester_hash_map_sc.py` and `tester_hash_map_oa.py`) that provide comprehensive validation of both HashMap implementations with various edge cases and performance scenarios.

## 💡 Key Learning Outcomes

- Implemented efficient hash table data structures with O(1) average-case complexity
- Compared two different collision resolution strategies
- Applied dynamic resizing to maintain performance under varied loads
- Implemented hash functions and analyzed their distribution characteristics
- Gained practical experience with space-time complexity tradeoffs

## 📫 Connect

Feel free to reach out if you have questions or would like to collaborate!                          
[![Email](https://img.shields.io/badge/Email-jramz1897%40gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jramz1897@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-jramz87.github.io-blue?style=for-the-badge&logo=github&logoColor=white)](https://jramz87.github.io/)

## License
This project is licensed under [![License: MIT](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c34_License-MIT-blue.svg)](/LICENSE)  - see the LICENSE file for details.
