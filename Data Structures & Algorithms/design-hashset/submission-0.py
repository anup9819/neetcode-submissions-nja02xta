class MyHashSet:

    def __init__(self):
        self.arra = []

    def add(self, key: int) -> None:
        if key not in self.arra:
            self.arra.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.arra:
            self.arra.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.arra:
            return True
        else:
            return False
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)