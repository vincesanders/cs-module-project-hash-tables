class Node:
    def __init__(self,key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key=None, value=None):
        if value is None:
            self.head = None
        else:
            self.head = Node(key, value)

    def __str__(self):
        return_string = '['
        if self.head is None:
            return return_string + 'None]'
        current = self.head
        while current.next is not None:
            return_string += f'({current.key}: {current.value}), '
            current = current.next
        return return_string + f'({current.key}: {current.value})' + ']'

    #returns the new head
    def add_to_head(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
        else:
            node = Node(key, value)
            node.next = self.head
            self.head = node
        return self.head

    def find_by_value(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    # returns value
    def find_by_key(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        current = self.head
        if current.key == key: #the head is to be deleted
            value = current.value
            self.head = current.next
            return value
        while current.next is not None:
            if current.next.key == key:
                #this is what we need to delete
                value = current.next.value
                current.next = current.next.next
                return value
            current = current.next
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = []
        for _ in range(capacity):
            self.storage.append(HashTableEntry(None, None))

    def __str__(self):
        return_str = '['
        for i in range(self.capacity - 1):
            return_str += f'{self.storage[i]}, '
        return return_str + f'{self.storage[self.capacity - 1]}]'

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash = 14695981039346656037
        prime = 1099511628211
        size = 2**64
        for c in key:
            hash = (hash * prime) % size
            hash = hash ^ ord(c)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            # <<5 shife bits left by 5 ex: 00000001 => 00100000
            # hash = (( hash << 5) + hash) + ord(c)
            hash = hash * 33 + ord(c)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        self.storage[index].add_to_head(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        return self.storage[index].delete(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        return self.storage[index].find_by_key(key)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # create a new hashtable
        new_hashtable = HashTable(new_capacity)
        # add values from old hashtable to new hashtable
        for hte in self.storage:
            # loop through values of hte (linked list)
            current = hte.head
            while current is not None:
                # add each value to new hashtable
                new_hashtable.put(current.key, current.value)
                current = current.next
        # make old hashtable = new hashtable
        self.capacity = new_hashtable.capacity
        self.storage = new_hashtable.storage




if __name__ == "__main__":
    ht = HashTable(8)

    print(ht)

    print(ht.djb2('xz'))
    print(ht.djb2('xy'))

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")

    print(ht)

    # ht.delete("key-2")
    # print(ht)
    # ht.delete("key-1")
    # print(ht)
    ht.delete("key-0")
    print(ht)

    print(ht.get_num_slots())

    ht.resize(16)

    print(ht.get_num_slots())
    print(ht)

    # print(ht)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
