import hashlib

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

hash_table = HashTable(100)  
username=input("Username:")
password=input("Password:")
hash_table.insert(username, hash_password(password))

alice_password = hash_table.get(username)
if alice_password and alice_password == hash_password(password):
    print("Username and password is correct")
else:
    print("Invalid username or password")

