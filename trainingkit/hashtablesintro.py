hash_table_size = 8

hash_table = [None] * hash_table_size

def my_hash(s):
    s_bytes = s.encode()
    total = 0
    for b in s_bytes:
        total += b
    return total

def hash_index(s):
    h = my_hash(s)
    return h % hash_table_size

def put(key, value):
    index = hash_index(key)
    hash_table[index] = value

def get(key):
    index = hash_index(key)
    return hash_table[index]

def delete(key):
    index = hash_index(key)
    hash_table[index] = None

if __name__ == "__main__":
    # do stuff only when this file isn't imported

    put('Hello', 37)
    put('foobar', 128)
    put('cats', 'dogs')
    print(hash_table)

    print(get("hello")) # case doesn't matter in the current hash function

    delete('hello')
    print(get('hello'))