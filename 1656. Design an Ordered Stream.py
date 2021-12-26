class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.output = []
        self.output.append(None)
        self.hashmap = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hashmap[idKey] = value
        if self.ptr not in self.hashmap:
            return []
        else:
            arr = []
            while self.ptr in self.hashmap:
                arr.append(self.hashmap[self.ptr])
                self.ptr += 1
                self.output.append(arr)
            return arr


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
