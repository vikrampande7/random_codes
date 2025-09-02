class MyArray:
    def __init__(self):
        self.length = 0
        self.data = []

    def get_item(self, index):
        return self.data[index]

    def push_item(self, newItem):
        self.data.append(newItem)
        self.length += 1
        return self.length

    def delete_item(self):
        lastItem = self.data[self.length-1]
        self.data.pop()
        self.length -= 1
        print(f"deleted item: {lastItem}")
        return self.length


a = MyArray()
a.push_item('a')
a.push_item('b')
a.push_item('c')
print(a.get_item(0))
print(a.get_item(1))
print(a.get_item(2))
a.delete_item()

