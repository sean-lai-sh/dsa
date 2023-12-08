from lists import ArrayList


# Import relevant classes


class ArrayStack:
    def __init__(self):
        # Make an array and define self parameters
        self.data_arr = ArrayList()

    def pop(self):
        # return len(arr) - 1 value and remove it.
        if self.is_empty():
            raise Exception("Stack is empty")
        rev_item = self.data_arr.pop()
        return rev_item

    def push(self, item):
        # Add the item to the end of the item
        try:
            self.data_arr.append(item)
            return True
        except Exception:
            return False

    def top(self):
        # return len(arr) -1 value
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data_arr[-1]

    def __len__(self):
        return len(self.data_arr)

    def is_empty(self):
        return len(self) == 0
