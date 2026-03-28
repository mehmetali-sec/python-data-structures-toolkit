"""
Hash Map Implementation (with Separate Chaining)
-----------------------------------------------
A technical archive from my Freshman Year (2025).
Refactored for performance and readability in 2026.

This implementation uses separate chaining to handle hash collisions,
making it efficient for high-speed data lookups.
"""

class HashMap:
    def __init__(self, size=11):
        """
        Initializes the hash map. 
        A prime number size (like 11) is used to minimize collisions.
        """
        self.size = size
        self.slots = [[] for _ in range(size)]  # List of buckets for chaining
        self.count = 0

    def _hash(self, key):
        """Standard Python hash combined with modulo for indexing."""
        return hash(key) % self.size

    def put(self, key, value):
        """Inserts a new key-value pair or updates an existing one."""
        index = self._hash(key)
        bucket = self.slots[index]

        # Update if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Append new pair if key is unique
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        """Retrieves value for a key. Returns None if key doesn't exist."""
        index = self._hash(key)
        bucket = self.slots[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Removes a key and returns True if successful, False otherwise."""
        index = self._hash(key)
        bucket = self.slots[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return True
        return False

    # --- Advanced Pythonic Features ---
    # These allow using the class like a real dictionary: h["key"] = "value"

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.count

    def __repr__(self):
        """Returns a string representation of the hash map contents."""
        items = []
        for bucket in self.slots:
            for k, v in bucket:
                items.append(f"{k!r}: {v!r}")
        return "{" + ", ".join(items) + "}"


# --- Demo and Test Section ---
if __name__ == "__main__":
    print("--- Testing Hash Map with Chaining ---")
    h = HashMap()

    # Using standard methods
    h.put("bank_name", "Global Bank")
    
    # Using the new Pythonic shortcuts
    h["security_level"] = "High"
    h["soc_analyst"] = "Mehmet Ali"

    print(f"Current Map: {h}")
    print(f"Total Elements: {len(h)}")
    print(f"Retrieving 'soc_analyst': {h['soc_analyst']}")

    # Testing removal
    h.remove("bank_name")
    print(f"After removing bank_name: {h}")
