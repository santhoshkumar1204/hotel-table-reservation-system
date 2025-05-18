import hashlib
import os


class PersistentHashTable:
    def __init__(self, filename='login_data.txt', num_buckets=100):
        self.filename = filename
        self.num_buckets = num_buckets
        self.table = self.load_table()

    def hash_function(self, username):
        print(int(hashlib.sha256(username.encode()).hexdigest(), 16))
        return int(hashlib.sha256(username.encode()).hexdigest(), 16) % self.num_buckets

    def insert(self, username, password):
        index = self.hash_function(username)
        available = True
        # Check if username already exists
        for entry in self.table[index]:
            stored_username, _ = entry.split(':')
            if stored_username == username:
                available = False
        if available:
            # If not found, insert the new username and password
            self.table[index].append(f"{username}:{password}")
            self.save_table()
            return "successfully"
        else:
            return "already"

    def login(self, username, password):
        status = ""
        index = self.hash_function(username)
        for entry in self.table[index]:
            stored_username, stored_password = entry.split(':')
            if stored_username == username:
                if stored_password == password:
                    status = "successfully"
                else:
                    status = "invalid"
        return status

    def save_table(self):
        with open(self.filename, 'w') as f:
            for bucket in self.table:
                f.write(','.join(bucket) + '\n')

    def load_table(self):
        table = [[] for _ in range(self.num_buckets)]
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for i, line in enumerate(f):
                    if line.strip():
                        table[i] = line.strip().split(',')
        return table
