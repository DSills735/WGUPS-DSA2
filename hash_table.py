


#Hash Table implementation, requirement A
class hash_table:
    def __init__(self, package_capacity = 40):
        self.table = []
        self.package_capacity = package_capacity
        for i in range(package_capacity):
            self.table.append([])

#hash insert function
    def table_add(self, key, package):
        bucket = hash(key) % len(self.table)
        #self.table[bucket].append(package)
        allbuckets = self.table[bucket]

        for keys in allbuckets:
            if keys[0] == key:
                keys[1] = package
                return True
        #key_item = [key, package]
        allbuckets.append([key, package])
        return True
#hash search function
    def hash_search(self, key):
        bucket = hash(key) % len(self.table)
        allbuckets = self.table[bucket]

        for keys in allbuckets:
            if keys[0] == key:
                return keys[1]
        return None
#remove from hash table
    def hash_remove(self, key):
        bucket = hash(key) % len(self.table)
        allbuckets = self.table[bucket]

        if key in allbuckets:
            allbuckets.remove(key)

    #check later if this needs to return none, idt it does










