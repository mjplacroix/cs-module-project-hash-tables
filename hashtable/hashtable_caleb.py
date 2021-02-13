class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, hash='fnv1'):
        if capacity < MIN_CAPACITY:
            raise(ValueError(f'capacity must be at lest {MIN_CAPACITY}'))
        
        self.hash = self.__getattribute__(hash)

        self.capacity = capacity
        self._load_factor = 0.0
        self._storage = [HashTableEntry(None, None) for _ in range(capacity)]


    def get_num_slots(self) -> int:
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    @property
    def load_factor(self) -> float:
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self._load_factor


    @load_factor.setter
    def load_factor(self, value:float):
        if value < self._load_factor and value < 0.2 and self.capacity > MIN_CAPACITY:
            # shrunk and too many open slots; resize by half (no less than MIN_CAPACITY)
            self.resize(max((self.capacity + 1) // 2, MIN_CAPACITY))
        elif value > self._load_factor and value > 0.7:
            # grown and too many used slots; double size
            self.resize(self.capacity * 2)
        else:
            # new load_factor ok; update load_factor
            self._load_factor = value


    def fnv1(self, key) -> int:
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # string to list of character encodings
        key_codes = key.encode()

        # https://en.wikipedia.org/wiki/Fowler–Noll–Vo_hash_function#FNV-1_hash
        hash = 14695981039346656037
        for code in key_codes:
            hash = (hash * 1099511628211) ^ code

        return hash & 0xffffffffffffffff


    def djb2(self, key) -> int:
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # string to list of character encodings
        key_codes = key.encode()

        # http://www.cse.yorku.ca/~oz/hash.html
        hash = 5381
        for code in key_codes:
            hash = (((hash << 5) + hash) + code)

        return hash & 0xffffffff


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.hash(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if not isinstance(key, str):
            raise(TypeError('Keys must be strings.'))

        current_entry = self._storage[self.hash_index(key)]

        if current_entry.key is None:
            # empty bucket; set key and value
            current_entry.key = key
            current_entry.value = value
        else:
            # hash collision; traverse list
            while current_entry is not None:
                if key == current_entry.key:
                    # key exists; update value, return previous value
                    old_value = current_entry.value
                    current_entry.value = value
                    return old_value
                previous_entry = current_entry
                current_entry = current_entry.next
            # end of list and key not found; insert new entry
            previous_entry.next = HashTableEntry(key, value)
        
        # inserted new entry; update load_factor 
        self.load_factor += (1 / self.capacity)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if not isinstance(key, str):
            raise(TypeError('Keys must be strings.'))

        index = self.hash_index(key)
        current_entry = self._storage[index]
        value = None

        if key == current_entry.key:
            # found key, first entry; store value, erase entry
            value = current_entry.value
            if current_entry.next is None:
                # no more entries; erase current entry
                current_entry.key = current_entry.value = None
            else:
                # more entries; replace head with next
                self._storage[index] = current_entry.next
        else:
            # traverse remaining entries
            previous_entry = current_entry
            current_entry = current_entry.next
            while current_entry is not None:
                if key == current_entry.key:
                    # found key; store value, unlink entry
                    value = current_entry.value
                    previous_entry.next = current_entry.next
                    break
                previous_entry = current_entry
                current_entry = current_entry.next

        if value is not None:
            # deleted an entry; update load_factor
            self._load_factor -= (1 / self.capacity)
        else:
            # key not found
            print(f'Key not found: {key}')
        
        return value


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if not isinstance(key, str):
            raise(TypeError('Keys must be strings.'))

        current_entry = self._storage[self.hash_index(key)]

        while current_entry is not None:
            if key == current_entry.key:
                return current_entry.value
            current_entry = current_entry.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_storage = self._storage
        self.__init__(new_capacity, hash=self.hash.__name__)

        for bucket in old_storage:
            current_entry = bucket
            while current_entry is not None and current_entry.key is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")