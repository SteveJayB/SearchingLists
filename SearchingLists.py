################################################
#             Stephen Bridgett                 #
#              Searching Lists                 #
################################################

def search_sorted_list(sorted_list, item):
    """
    Perform binary search on a sorted list.
    Returns the index of the item if found, else returns -1.
    """
    first, last = 0, len(sorted_list) - 1
    while first <= last:
        mid = (first + last) // 2  # Find the middle index
        if sorted_list[mid] == item:
            return mid  # Item found, return index
        elif sorted_list[mid] < item:
            first = mid + 1  # Search right half
        else:
            last = mid - 1  # Search left half
    return -1  # Item not found

print("---------------- #1 ------------------")
sorted_list = [0, 1, 4, 6, 7, 11, 14, 17, 19, 21, 25, 27, 28, 29]
for num in [4, 6, 12, 15, 20, 24, 29]:
    print(search_sorted_list(sorted_list, num))

class HashList:
    """
    A simple Hash List implementation using linear probing.
    """
    def __init__(self, size=19):
        self.size = size  # Define hash table size
        self.slot = [None] * self.size  # Initialize slots

    def hash_function(self, item):
        """Compute hash index using modulo operation."""
        return item % self.size

    def rehash(self, old_hash):
        """Rehash using linear probing."""
        return (old_hash + 1) % self.size

    def put(self, item):
        """Insert an item into the hash table."""
        item_hash = self.hash_function(item)
        while self.slot[item_hash] is not None:  # Resolve collisions using linear probing
            item_hash = self.rehash(item_hash)
        self.slot[item_hash] = item

    def contains(self, item):
        """Check if an item exists in the hash table."""
        item_hash = self.hash_function(item)
        start_hash = item_hash  # Keep track of original position
        while self.slot[item_hash] is not None:
            if self.slot[item_hash] == item:
                return True
            item_hash = self.rehash(item_hash)
            if item_hash == start_hash:  # Full cycle, item not found
                return False
        return False

print("---------------- #2 ------------------")
mylist = HashList()
mylist.put(41)
mylist.put(67)
mylist.put(2)
mylist.put(32)
mylist.put(53)
mylist.put(123)
mylist.put(43)
print(mylist.contains(41))
print(mylist.contains(32))
print(mylist.contains(34))

class HashTable:
    """
    A HashTable implementation with key-value pairs.
    """
    def __init__(self, size=6):
        self.size = size
        self.map = [None] * self.size

    def get_hash(self, key):
        """Compute hash value from key."""
        return sum(ord(char) for char in str(key)) % self.size

    def add(self, key, value):
        """Insert a key-value pair into the hash table."""
        key_hash = self.get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.map[key_hash].append(key_value)

    def get(self, key):
        """Retrieve value associated with key."""
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for i, pair in enumerate(self.map[key_hash]):
                if pair[0] == key:
                    self.map[key_hash].pop(i)
                    return True
        return False

    def print_table(self):
        """Print the hash table contents."""
        print("--- Hash Table Contents ---")
        for item in self.map:
            if item is not None:
                print(item)

print("---------------- #3 ------------------")
h = HashTable()
h.add('Jane', '23')
h.add('Alex', '50')
h.add('Joe', '5')
h.add('Sally', '16')
h.add('Mason', '14')
h.add('Meg', '74')
h.add('Siri', '37')
h.add('Jason', '18')
h.add('Mia', '89')
h.add('Sara', '20')
h.print_table()
h.delete('Jane')
print("")
h.print_table()
print('Meg: ' + h.get('Meg'))

def sort_list(my_list):
    """
    Implement selection sort algorithm to sort a list.
    """
    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

print("---------------- #4 ------------------")
my_list = [23, 3, 54, 12, 34, 25, 56, 80, 68, 37, 76, 16, 21, 42, 39]
sort_list(my_list)
print(my_list)


################### Sources #########################
#                 youtube.com                       #
#              stackoverflow.com                    #
#Problem Solving with Algorithms and Data Structures#
#####################################################













